# python-pub

## Crypto: indistinguishability experiments

- Private-key encryption schemes: [cipher.py](cipher.py)
- PrivK experiment driver: [privk-eav.py](privk-eav.py)
  - Adv for Shift cipher in ECB mode: [mallory.py](mallory.py)
  - Adv for Shift cipher with unbalanced keys: [mallory2.py](mallory2.py)
  - Adv for Vigenère cipher with unbalanced keys: [mallory3.py](mallory3.py)
  - Adv for OTP with computed last bit: [mallory4.py](mallory4.py)
  - Adv for two-time pad: [mallory5.py](mallory5.py)
  - Adv for quasi-OTP: [mallory6.py](mallory6.py)

## Constraint solving with Z3

- [The strange case of Prof. Pinna](pinna-case.py)
- [Socrates is mortal](socrates-is-mortal.py)
- [Halloween at the Science Palace](halloween-science-palace.py)
- [Halloween party](halloween-party.py)
