def diffie_hellman(g,a,p) :
    #g: Base (generator)
    #a: Private key
    #p: Prime modulus
    return g**a%p
def cypher(s, key):
    # Convert string to bytes
    b = bytes(s, "utf-8")
    # XOR each byte with the key
    # NOTE : the key in our situation should not be up to 1 byte  == 0<p<10 
    encrypted_bytes = bytes([byte ^ key for byte in b]) 
    # Convert back to string for readability
    return encrypted_bytes.decode("utf-8", errors="ignore")
