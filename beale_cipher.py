def decrypt_beale(ciphertext, key_text):
words = key_text.split()

result = []
for num in ciphertext.split():
  if num.isdigit():
    index = int(num) - 1
    if index < len(words):
      result.append(words[index][0])
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
  ciphertext = input("Shkruaj tekstin per dekriptim:")
  decrypted = decrypt_beale(ciphertext, key_text)
  print("Decrypted:", decrypted)

else:
  print("Opsion i pavlefshem!")
