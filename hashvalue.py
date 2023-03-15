from bs4 import BeautifulSoup
import hashlib
import requests
import platform

def assign_file_url():
  """Get latest version & platform, add it to the url then return to the url"""
  bit = ""
  vlc_url = "https://www.videolan.org/vlc/download-windows.html"
  response = requests.get(vlc_url)
  response.raise_for_status()
  vlc_page = response.text

  soup = BeautifulSoup(vlc_page, "html.parser")
  version_tag = soup.find(name="span", id="downloadVersion")
  version = version_tag.getText().strip()

  if platform.machine().endswith("86") or platform.machine().endswith("32"):
    bit = "32"
  elif platform.machine().endswith("64"):
    bit = "64"

  url = f"http://download.videolan.org/pub/videolan/vlc/{version}/win{bit}/"
  return url

def get_expected_hashvalue():
  """Get and return expected hash value"""
  file_url = assign_file_url()
  response = requests.get(file_url)
  response.raise_for_status()

  file_content = response.content
  image_hash = hashlib.sha256(file_content).hexdigest()

  return image_hash

get_expected_hashvalue()