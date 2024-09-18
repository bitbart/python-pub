# python-pub

## Constraint solving with Z3

- [The strange case of Prof. Pinna](z3/pinna-case.py)
- [Socrates is mortal](z3/socrates-is-mortal.py)
- [Halloween at the Science Palace](z3/halloween-science-palace.py)
- [Halloween party](z3/halloween-party.py)

## Property-based testing

- Remove least element from a list: [1](hypothesis/remove_smallest1.py), [2](hypothesis/remove_smallest2.py), [3](hypothesis/remove_smallest3.py), [4](hypothesis/remove_smallest4.py), [5](hypothesis/remove_smallest5.py), [6](hypothesis/remove_smallest6.py)
- [Maximum of 3 numbers](hypothesis/max3.py)
- [Dictionary](hypothesis/dict.py)
- [Hash table](hypothesis/hash.py)

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
