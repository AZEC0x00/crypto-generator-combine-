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

### Installation
1. - Clone the Repository (if you haven't already):
   - ```bash
     git clone https://github.com/yourusername/bnb-wallet-brute-force.git
     cd bnb-wallet-brute-force
2. ### Install the Required Libraries:
   - ```bash
     pip install ecdsa requests
3. ### Set Up API Key:
   - Create a config.json file in the root directory of the project.
   - Add your BSC API key to the config.json file:
    ```bash
    {
     "api_key": "YOUR_BSC_API_KEY"
   }
1. ### Run the Script:
   ```bash
   python bnb_wallet.py

2. ### Monitor the Output:

The script will continuously generate private keys, derive BNB addresses, and check their balances.

If a wallet with a non-zero balance is found, the details will be logged and saved to found_wallets.txt.
### Example:
   ```bash
    2023-10-01 12:34:56 - INFO - Generated Private Key: 5f6d7a8b9c0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a
   2023-10-01 12:34:56 - INFO - Generated BNB Address: 0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
   2023-10-01 12:34:56 - INFO - Balance: 0.000000000000 BNB
   2023-10-01 12:34:58 - INFO - Wallet with balance found! Address: 0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b,
   Private Key: 5f6d7a8b9c0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a,
   Balance: 1.234567890000 BNB
