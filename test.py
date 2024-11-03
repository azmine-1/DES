import unittest
from des import DES
import os

class TestDES(unittest.TestCase):
    def setUp(self):
        self.key = b"TESTKEY1"
        self.des = DES(self.key)

    def test_basic_encryption_decryption(self):
        plaintext = b"Hello123"
        encrypted = self.des.encrypt(plaintext)
        decrypted = self.des.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_long_message(self):
        plaintext = b"This is a longer message that spans multiple blocks to test the DES implementation"
        encrypted = self.des.encrypt(plaintext)
        decrypted = self.des.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_empty_message(self):
        plaintext = b""
        encrypted = self.des.encrypt(plaintext)
        decrypted = self.des.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_binary_data(self):
        plaintext = os.urandom(100)  
        encrypted = self.des.encrypt(plaintext)
        decrypted = self.des.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_padding(self):
        #verify padding
        for length in range(1, 20):
            plaintext = b'A' * length
            encrypted = self.des.encrypt(plaintext)
            decrypted = self.des.decrypt(encrypted)
            self.assertEqual(plaintext, decrypted)

    def test_different_keys(self):
        plaintext = b"Hello, World!"
        key1 = b"TESTKEY1"
        key2 = b"TESTKEY2"
        
        des1 = DES(key1)
        des2 = DES(key2)
        
        encrypted1 = des1.encrypt(plaintext)
        encrypted2 = des2.encrypt(plaintext)
        self.assertNotEqual(encrypted1, encrypted2)
        self.assertEqual(plaintext, des1.decrypt(encrypted1))
        self.assertEqual(plaintext, des2.decrypt(encrypted2))

    def test_invalid_key_length(self):
        with self.assertRaises(ValueError):
            DES(b"SHORT")  # Key too short
        with self.assertRaises(ValueError):
            DES(b"TOOLONGKEY")  # Key too long

    def test_invalid_decrypt_input(self):
        with self.assertRaises(ValueError):
            self.des.decrypt(b"Invalid length")  

    def test_known_vectors(self):
        #what happens when the key is the same as the plaintext
        key = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF"
        plaintext = b"\x01\x23\x45\x67\x89\xAB\xCD\xE7"
        des = DES(key)
        encrypted = des.encrypt(plaintext)
        decrypted = des.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_multiple_blocks(self):
        #correct input intests
        plaintext = b"0123456789ABCDEF"
        encrypted = self.des.encrypt(plaintext)
        decrypted = self.des.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

def main():
    #demo
    key = b"TESTKEY1"
    des = DES(key)
    
    #using strings as input
    message = b"Hello, World! This is a test message."
    print("\nOriginal message:", message.decode())
    encrypted = des.encrypt(message)
    print("Encrypted (hex):", encrypted.hex())
    decrypted = des.decrypt(encrypted)
    print("Decrypted:", decrypted.decode())
    print("\nRunning unit tests...")
    unittest.main(argv=['dummy'])

if __name__ == '__main__':
    main()