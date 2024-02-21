from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


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


if '__main__' == __name__:
    for eskFile in os.listdir('DoK2/'):
        print(eskFile)
        org, _ = eskFile.split('_')
        decrypt_file('DoK2/'+eskFile, 'DoK1/msk.key', org+'_sk.key')
        decrypt_file('DoK3/{}_wallet.dat'.format(org), org+'_sk.key', org+'_wallet.json')
        # NOTE: coin-address-map file is encrypted using MSK instead of ESK.
        decrypt_file('DoK3/{}_coin-address-map.enc'.format(org), 'DoK1/msk.key', org+'_coin-address-map.json')
