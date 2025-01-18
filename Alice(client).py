import socket

class Client:
    def __init__(self, host="127.0.0.1", port=4444):
        self.host = host
        self.port = port
        self.a = 5  # private key
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
            # Connect to server
            self.socket.connect((self.host, self.port))
            print("[+] Connected to server")
            
            # Receive g and p
            g = int(self.socket.recv(1).decode())
            p = int(self.socket.recv(1).decode())
            print(f"[*] Received g={g}, p={p}")
            
            # Calculate and exchange keys
            client_public = self.calculate_key(g, self.a, p)
            self.socket.send(str(client_public).encode())
            
            server_public = int(self.socket.recv(1024).decode())
            print(f"[*] Received server public key: {server_public}")
            
            shared_key = self.calculate_key(server_public, self.a, p)
            print(f"[*] Shared key calculated: {shared_key}")
            
            # Message loop
            while True:
                message = input("Enter message (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    break
                    
                encrypted_message = self.encrypt_decrypt(message, shared_key)
                print(f"[*] Encrypted message: {encrypted_message}")
                self.socket.send(encrypted_message.encode())
                
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            self.socket.close()
            print("[*] Connection closed")

if __name__ == "__main__":
    client = Client()
    client.start()