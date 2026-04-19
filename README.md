# Beale Cipher & Grille Cipher 

Ky projekt përmban implementimin e dy algoritmeve klasike të kriptografisë:
- Beale Cipher
- Grille Cipher (Cardan Grille)

Qëllimi i projektit është të demonstrojë mënyrën e enkriptimit dhe dekriptimit të mesazheve.

## 1.Beale Cipher

## Përshkrimi
Beale Cipher është një metodë ku çdo shkronjë e mesazhit zëvendësohet me pozicionin e një fjale nga një tekst çelës (key text), bazuar në shkronjën e parë të asaj fjale.

### Si funksionon?
- Merr një tekst çelës (key text)
- Ndërton një mapping:
    - shkronja → lista e pozicioneve të fjalëve që fillojnë me atë shkronjë
- Gjatë enkriptimit:
    - çdo shkronjë zëvendësohet me numrin e parë të disponueshëm
- Gjatë dekriptimit:
    - çdo numër kthehet në shkronjën e parë të fjalës përkatëse
---
### Shembull 
- Zgjedh opsionin e deshiruar
- === Beale Cipher ===
    - 1. Encrypt
    - 2. Decrypt
    - Zgjedh opsionin (1/2): 1
- Shkruaj tekstin celes (key text): This is your favorite album from Elita 5
- Shkruaj tekstin per enkriptim: Pershendetje
- Encrypted: p 7 r s h 7 n d 7 1 j 7
Me pas dekriptimi 
- === Beale Cipher ===
    - 1. Encrypt
    - 2. Decrypt
    - Zgjedh opsionin (1/2): 2
- Shkruaj tekstin celes (key text): This is your favorite album from Elita 5
- Shkruaje tekstin per dekriptim:p 7 r s h 7 n d 7 1 j 7
- Decrypted: pershendetje
---
### Funksionet:
- encrypt_beale(plaintext, key_text)
- decrypt_beale(ciphertext, key_text)

## 2.Grille Cipher (Cardan Grille)

## Përshkrimi
Grille Cipher përdor një matricë (grid) me vrima (1 = vrima), e cila rrotullohet për të vendosur karakteret e mesazhit në pozicione të ndryshme.

### Si funksionon?
- Gjenerohet një matricë (grille) me vrima
- Mesazhi vendoset në vrima
- Matrica rrotullohet 4 herë (0°, 90°, 180°, 270°)
- Teksti final merret duke lexuar matricën
---

### Shembull
- Jep madhesine e matrices ((numer cift)p.sh. 4) -> jep numrin e deshiruar 6 ne kete rast
- Paraqiten opsionet
-  --- GRILLE CIPHER ---
    - 1.Encrypt
    - 2. Decrypt
    - 3. Exit
    - Zgjedh: 1
-  Mesazhi: This is my project    
- Encrypted (string):  Tshis XXXXXrXXoXXmXXy X iXXXXpXjecXt
Ne rastin tjeter 
- --- GRILLE CIPHER ---
    - 1.Encrypt
    - 2. Decrypt
    - 3. Exit
    - Zgjedh: 2
- Shkruaj cipher text: Tshis XXXXXrXXoXXmXXy X iXXXXpXjecXt
- Decrypted: This is my projectXXXXXX
---
### Funksionet:
- generate_grille(size)
- rotate(grille)
- encrypt(message, grille)
- decrypt(cipher_text, grille)

## Si ta përdorësh

### 1.Ekzekuto programin:
python beale_cipher.py ose grille_cipher.py
### 2.Zgjedh opsionin:
Beale Cipher:
- 1 → Encrypt
- 2 → Decrypt

Grille Cipher:
- 1 → Encrypt
- 2 → Decrypt
- 3 → Exit
---
### Kufizime
- Beale Cipher:
    - Përdor gjithmonë indeksin e parë (jo random)
- Grille Cipher:
    - Mesazhi mund të mbushet me X nëse është më i shkurtër
    - Duhet e njëjta grille për dekriptim