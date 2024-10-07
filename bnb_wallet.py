import os
import ecdsa
import hashlib
import requests
import time
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API key from a configuration file or environment variable
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    API_KEY = config['api_key']
except (FileNotFoundError, KeyError):
    logging.error("API key not found. Please ensure 'config.json' exists and contains 'api_key'.")
    exit(1)

# Function to create a private key
def generate_private_key():
    return os.urandom(32).hex()

# Function to generate a public key from the private key
def private_key_to_public_key(private_key):
    try:
        pk_bytes = bytes.fromhex(private_key)
        sk = ecdsa.SigningKey.from_string(pk_bytes, curve=ecdsa.SECP256k1)
        vk = sk.verifying_key
        public_key = b'\x04' + vk.to_string()  # Uncompressed public key
        return public_key
    except Exception as e:
        logging.error(f"Error generating public key: {e}")
        return None

# Generate a BNB wallet address from the public key
def public_key_to_bnb_address(public_key):
    try:
        sha256_bpk = hashlib.sha256(public_key).digest()
        ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
        return '0x' + ripemd160_bpk.hex()
    except Exception as e:
        logging.error(f"Error generating BNB address: {e}")
        return None

# Function to check balance via BNB API (replace with a valid BSC API endpoint)
def check_balance(bnb_address):
    url = f'https://api.bscscan.com/api?module=account&action=balance&address={bnb_address}&apikey={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        if data['status'] == '1':
            balance = int(data['result'])
            return balance
        else:
            return 0
    except requests.exceptions.RequestException as e:
        logging.error(f"Error checking balance: {e}")
        return 0
    except (KeyError, ValueError) as e:
        logging.error(f"Error parsing API response: {e}")
        return 0

# Main brute-force loop
def brute_force_bnb_wallet():
    while True:
        # Step 1: Generate private key and derive public key and address
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        if not public_key:
            continue
        bnb_address = public_key_to_bnb_address(public_key)
        if not bnb_address:
            continue

        # Log private key and BNB address
        logging.info(f"Generated Private Key: {private_key}")
        logging.info(f"Generated BNB Address: {bnb_address}")

        # Step 2: Check the balance of the generated wallet
        balance = check_balance(bnb_address)
        balance_bnb = balance / 1e18  # Convert balance to BNB
        logging.info(f"Balance: {balance_bnb} BNB")

        # Step 3: If balance > 0.000000000001, save the details
        if balance_bnb > 0.000000000001:
            logging.info(f"Wallet with balance found! Address: {bnb_address}, Private Key: {private_key}")
            with open('found_wallets.txt', 'a') as f:
                f.write(f"Address: {bnb_address}, Private Key: {private_key}, Balance: {balance_bnb} BNB\n")

        # Step 4: Sleep to avoid overloading the API
        time.sleep(2)

if __name__ == "__main__":
    brute_force_bnb_wallet()