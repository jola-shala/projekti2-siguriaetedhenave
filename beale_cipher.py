import random 

def encrypt_beale(plaintext, key_text):
    words = key_text.split()
    mapping = {}

    for i, word in enumerate(words):
        first_letter = word[0].lower()
        if first_letter not in mapping:
            mapping[first_letter] = []
        mapping[first_letter].append(i + 1)

    result = []
    for char in plaintext.lower():
        if char in mapping:
            result.append(str(random.choice(mapping[char])))
        else:
            result.append(char)

    return " ".join(result)


def decrypt_beale(ciphertext, key_text):
  words = key_text.split()
  result = []

  for num in ciphertext.split():
    if num.isdigit():
      index = int(num) - 1
      if index < len(words):
        result.append(words[index][0].lower())
    else:
      result.append(num)
      
  return "".join(result)

if __name__ == "__main__":
  print("=== Beale Cipher ===")
  print("1. Encrypt")
  print("2. Decrypt")

choice = input("Zgjedh opsionin (1/2): ")
key_text = input("Shkruaj tekstin celes (key text): ")

if choice == "1":
  plaintext = input("Shkruaj tekstin per enkriptim: ")
  encrypted = encrypt_beale(plaintext, key_text)
  print("Encrypted:", encrypted)

elif choice == "2":
  ciphertext = input("Shkruaje tekstin per dekriptim:")
  decrypted = decrypt_beale(ciphertext, key_text)
  print("Decrypted:", decrypted)

else:
  print("Opsion i pavlefshem!")


