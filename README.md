# python-pub

## Crypto: indistinguishability experiments

- Private-key encryption schemes: [privk-crypto/cipher.py](cipher.py)
- PrivK experiment driver: [privk-crypto/privk-eav.py](privk-eav.py)
  - Adv randomly guessing: [privk-crypto/mallory0.py](mallory0.py)
  - Adv for Shift cipher in ECB mode: [privk-crypto/mallory1.py](mallory1.py)
  - Adv for Shift cipher with unbalanced keys: [privk-crypto/mallory2.py](mallory2.py)
  - Adv for Vigenère cipher with unbalanced keys: [privk-crypto/mallory3.py](mallory3.py)
  - Adv for OTP with computed last bit: [privk-crypto/mallory4.py](mallory4.py)
  - Adv for two-time pad: [privk-crypto/mallory5.py](mallory5.py)
  - Adv for quasi-OTP: [privk-crypto/mallory6.py](mallory6.py)

## Constraint solving with Z3

- [The strange case of Prof. Pinna](z3/pinna-case.py)
- [Socrates is mortal](z3/socrates-is-mortal.py)
- [Halloween at the Science Palace](z3/halloween-science-palace.py)
- [Halloween party](z3/halloween-party.py)
