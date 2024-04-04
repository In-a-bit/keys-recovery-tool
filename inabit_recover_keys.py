from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64


def decrypt_aes_gcm(encrypted_data, key, iv, tag):
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(iv, encrypted_data + tag, None)

def decrypt_file(encryptedfile: str, keyfile: str, outputfile: str) -> None:
    with open(encryptedfile, 'rb') as f:
        file_contents = f.read()

    # Extract IV (12 bytes) and tag (16 bytes)
    iv = file_contents[:12]
    tag = file_contents[12:28]
    encrypted_data = file_contents[28:]

    with open(keyfile, 'rb') as f:
        key = f.read()

    # Decrypt
    dec = decrypt_aes_gcm(encrypted_data, key, iv, tag)

    with open(outputfile, 'wb') as f:
        f.write(dec)

def decode_base64_file(input_path, output_path):
    with open(input_path, 'r') as file:
        base64_data = file.read()
    binary_data = base64.b64decode(base64_data)
    with open(output_path, 'wb') as file:
        file.write(binary_data)

def decode_all_base64_files():
    for file in os.listdir('files'):
        if file.endswith('.b64'):
            decode_base64_file('files/' + file, 'files/' + file[:-4])        

if '__main__' == __name__:
    print('convert base64 to binary file...')
    decode_all_base64_files()
    print('decrypting...')
    decrypt_file('files/wallet_key.enc', 'files/msk.key', 'files/wallet.key')
    decrypt_file('files/wallet.dat', 'files/wallet.key', 'files/wallet_dat.json')
    print('Done. Check your recovered wallet on files/wallet_dat.json file.')
  