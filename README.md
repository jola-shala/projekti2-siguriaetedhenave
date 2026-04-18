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