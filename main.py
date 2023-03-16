from hashvalue import get_expected_hashvalue
from installer import compare_hash_values

def main():
  # Step 1: Get expected hash value
  expected_hash_value = get_expected_hashvalue()
  print(expected_hash_value)

  # Step 2: Download the VLC installer and compares hash values
  compare_hash_values(expected_hash_value)

main()