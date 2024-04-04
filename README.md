# keys-recovery-tool

Keys Recovery Tool for inabit wallets

# Decrypt File Using AES-GCM Algorithm

This Python script allows you to decrypt your wallet.dat file and restore your wallet private key or mnemonic seed. The script uses the AES-GCM algorithm to decrypt the encrypted file. You need to provide the encrypted file, encrypted key and the key file to decrypt the file.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `cryptography`
- 3 Encrypted files in base64 format: wallet_key.enc.b64, msk.key.b64, wallet.dat.b64 for decryption.

## Usage

### 1. Installation of Required Packages

Before executing the script, ensure you have installed the necessary Python packages.
If the cryptography package is not installed, you can install it using pip:

```bash
pip install cryptography
```

2. File Preparation
   Before decrypting the encrypted file, you need to make sure you have the following files in place:

Encrypted File (wallet.dat.b64): The file you want to decrypt.
Encrypted Key File (wallet_key.enc.b64): The key file required for decryption.
Key File (msk.key.b64): The key file required for decrypt the key file.

the files should be placed in a "files" folder in the root directory of the project.

```bash
cd keys-recovery-tool
mkdir files
```

Place the encrypted file (wallet.dat.b64), encrypted key file (wallet_key.enc.b64), and key file (msk.key.b64) in the "files" folder.

extension. 3. Running the Script
You can run the script by executing the following command in your terminal or command prompt:

```bash
python3 decrypt_file.py
```

The script will decrypt the encrypted file, and save a new file named "wallet_dat.json" in the "files" folder.
