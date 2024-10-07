# crypto generator combine
Generators and search for wallets with balances of different cryptocurrencies 

### Overview
This Python script is designed to brute-force generate Binance Coin (BNB) wallet addresses and check their balances using the Binance Smart Chain (BSC) API. The script generates private keys, derives corresponding public keys and BNB addresses, and then checks the balance of each generated address. If a wallet with a non-zero balance is found, the details are saved to a file.

### Disclaimer: 
This script is intended for educational purposes only. Brute-forcing cryptocurrency wallets is generally considered unethical and may be illegal. Use this script responsibly and only on wallets you own or have explicit permission to test.

![image (4)](https://github.com/user-attachments/assets/e2fb5a4b-a7ff-4c3d-8ce0-bd16f3400b37)

- Features
- Private Key Generation: Generates random private keys using secure random number generation.

- Public Key Derivation: Derives public keys from private keys using the ECDSA algorithm.

- BNB Address Generation: Converts public keys to BNB addresses using SHA-256 and RIPEMD-160 hashing.

- Balance Checking: Checks the balance of generated BNB addresses using the BSC API.

- Logging: Logs generated private keys, BNB addresses, and balances for tracking.

- Found Wallets Saving: Saves details of wallets with non-zero balances to a file.

## Requirements
'Python 3.x'

'ecdsa library'

'requests library'
