# Secure Socket Communication with Diffie-Hellman

A simple implementation of socket-based communication between a server and client using the Diffie-Hellman key exchange algorithm and XOR encryption. This project demonstrates basic concepts of secure communication and key exchange protocols.

## Features

- Socket-based client-server communication
- Diffie-Hellman key exchange implementation
- Simple XOR encryption/decryption
- Clean console output with status indicators
- Error handling and graceful shutdown

## Requirements

- Python 3.6+
- No external dependencies required

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/secure-socket-communication.git
cd secure-socket-communication
```

## Usage

1. Start the server:
```bash
python server.py
```

2. In a separate terminal, start the client:
```bash
python client.py
```

3. Type messages in the client terminal to send them to the server
4. Type 'exit' to close the connection

## Project Structure

```
secure-socket-communication/
├── server.py     # Server implementation
├── client.py     # Client implementation
└── README.md     # This file
```

## Implementation Details

### Server
- Listens on localhost (127.0.0.1) port 4444
- Generates and shares Diffie-Hellman parameters (g, p)
- Uses private key b = 3
- Handles multiple message exchanges
- Decrypts received messages using shared key

### Client
- Connects to server on localhost:4444
- Uses private key a = 5
- Calculates shared secret using server's public key
- Encrypts messages before sending
- Provides interactive message input

### Security Notes
- This is a demonstration project and should not be used in production
- The implementation uses small prime numbers for demonstration
- XOR encryption is not cryptographically secure
- The key exchange parameters are hardcoded

## Console Output Format

The program uses the following indicators in console output:
- `[*]` Information and status messages
- `[+]` Successful operations
- `[!]` Errors and warnings

Example output:
```
[*] Server listening on 127.0.0.1:4444
[+] Connection from ('127.0.0.1', 52431)
[*] Received client public key: 5
[*] Shared key calculated: 3
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This code is for educational purposes only. It demonstrates basic concepts of secure communication but should not be used in production environments without significant security improvements.

## Contact

Your Name - [@gogo gaga](https://github.com/HamzaBika)

Reference Link: [Demystifying Diffie-Hellman key exchange and explaining how it works](https://www.comparitech.com/blog/information-security/diffie-hellman-key-exchange/)
