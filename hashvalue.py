from bs4 import BeautifulSoup
import hashlib
import requests
import platform

def get_software_info():
  """Get the VLC latest version info and the number of bits your comoputer runs on"""
  # Get the amount of bits
  bit = ""

  if platform.machine().endswith("86") or platform.machine().endswith("32"):
    bit = "32"
  elif platform.machine().endswith("64"):
    bit = "64"

  # Get latest version
  vlc_url = "https://www.videolan.org/vlc/download-windows.html"
  response = requests.get(vlc_url)
  response.raise_for_status()
  vlc_page = response.text

  soup = BeautifulSoup(vlc_page, "html.parser")
  version_tag = soup.find(name="span", id="downloadVersion")
  version = version_tag.getText().strip()

  return bit, version

def get_expected_hashvalue():
  """Get and return expected hash value"""
  bit = get_software_info()[0]
  version = get_software_info()[1]

  file_url = f"http://download.videolan.org/pub/videolan/vlc/{version}/win{bit}/vlc-{version}-win{bit}.exe.sha256"
  response = requests.get(file_url)
  response.raise_for_status()

  file_content = response.content
  image_hash = hashlib.sha256(file_content).hexdigest()

  return image_hash

get_expected_hashvalue()