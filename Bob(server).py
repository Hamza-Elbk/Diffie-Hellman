# server.py
import socket

class Server:
    def __init__(self, host="127.0.0.1", port=4444):
        self.host = host
        self.port = port
        self.b = 3  # private key
        self.g = 3  # generator
        self.p = 7  # prime modulus
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def calculate_key(self, base, exponent, modulus):
        return pow(base, exponent, modulus)
    
    def encrypt_decrypt(self, message, key):
        # Simple XOR encryption/decryption
        result = ""
        key_str = str(key)
        key_length = len(key_str)
        for i in range(len(message)):
            result += chr(ord(message[i]) ^ ord(key_str[i % key_length]))
        return result
    
    def start(self):
        try:
            # Setup server
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            print(f"[*] Server listening on {self.host}:{self.port}")
            
            # Accept connection
            conn, addr = self.socket.accept()
            print(f"[+] Connection from {addr}")
            
            # Send g and p
            conn.send(str(self.g).encode())
            conn.send(str(self.p).encode())
            
            # Calculate and exchange keys
            server_public = self.calculate_key(self.g, self.b, self.p)
            client_public = int(conn.recv(1024).decode())
            print(f"[*] Received client public key: {client_public}")
            
            conn.send(str(server_public).encode())
            shared_key = self.calculate_key(client_public, self.b, self.p)
            print(f"[*] Shared key calculated: {shared_key}")
            
            # Message loop
            while True:
                encrypted_data = conn.recv(1024).decode()
                if not encrypted_data:
                    break
                    
                print(f"[*] Received encrypted: {encrypted_data}")
                decrypted_data = self.encrypt_decrypt(encrypted_data, shared_key)
                print(f"[*] Decrypted message: {decrypted_data}")
                
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            self.socket.close()
            print("[*] Server shutdown")

if __name__ == "__main__":
    server = Server()
    server.start()
