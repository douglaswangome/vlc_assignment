from bs4 import BeautifulSoup
import requests
import platform

def assign_target_url():
  bit = ""
  vlc_url = "https://www.videolan.org/vlc/download-windows.html"
  response = requests.get(vlc_url)
  vlc_page = response.text

  soup = BeautifulSoup(vlc_page, "html.parser")
  version_tag = soup.find(name="span", id="downloadVersion")
  version = version_tag.getText().strip()

  if platform.machine().endswith("86") or platform.machine().endswith("32"):
    bit = "32"
  elif platform.machine().endswith("64"):
    bit = "64"

  target_url = f"http://download.videolan.org/pub/videolan/vlc/{version}/win{bit}/"
  return target_url

def get_expected_hashvalue():
  print(assign_target_url())

get_expected_hashvalue()