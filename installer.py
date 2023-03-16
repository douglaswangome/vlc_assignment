from hashvalue import get_software_info
import hashlib
import os
import subprocess
import requests

def compare_hash_values(expected_hash_value):
  """Compares the expected hash value with the installer hash value"""
  bit = get_software_info()[0]
  version = get_software_info()[1]
  file_url = f"http://download.videolan.org/pub/videolan/vlc/{version}/win{bit}/vlc-{version}-win{bit}.exe"

  response = requests.get(file_url)
  response.raise_for_status()

  file_location = os.path.join(os.path.expanduser("~"), "Downloads", f"vlc-{version}-win{bit}.exe")
  file_content = response.content

  with open(file_location, "wb") as file:
    file.write(file_content)

  actual_hash_value = hashlib.sha256(file_content).hexdigest()

  if actual_hash_value == expected_hash_value:
    return True, file_location
  return False

def silent_installer():
  """Installs a program silently through the executable file"""
  install = compare_hash_values()[0]

  if install:
    file_location = compare_hash_values()[1]

    # install the program using the exe file
    subprocess.run([file_location, "/S"])
    # script used to remove the installer from your computer
    # os.remove(file_location)