import socket
import json
import struct
import requests

IP_ADDRESS = "127.0.0.1"
PORT = 1401

GET_API_REVISION = 'Pixera.Utility.getApiRevision'
DEBUG_OUTPUT = 'Pixera.Utility.outputDebug'
TOGGLE_TRANSPORT = 'Pixera.Compound.toggleTransport'

getTimelinesSelected = 'Pixera.Timelines.getTimelinesSelected'
setCurrentTimeOfTimelineInSeconds = 'Pixera.Compound.setCurrentTimeOfTimelineInSeconds'

def send_TCP_dl(ip_address, port):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Set a timeout for the socket operations
        s.settimeout(10)  # 10 seconds timeout
        
        # Connect the socket to the server's address and port
        s.connect((IP_ADDRESS, PORT))

        # Define the JSON-RPC request payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "Pixera.Utility.getApiRevision"
        }

        # print("Sending:", payload)

        # Send the request with the "0xPX" delimiter at the end
        s.sendall((json.dumps(payload) + '0xPX').encode())

        # Receive the response
        data = s.recv(1024)


    return data.decode()

def send_TCP(method=None, params=None, message=None):
    if method is None:
        method = DEBUG_OUTPUT
        if params is None:
            params = ["message"]
        if message is None:
            message = ["Hello from Python!"]

    params_dict = {}

    if params is not None:
        # Convert the params and message lists to a dictionary
        params_dict = {params[i]: message[i] for i in range(len(params))}
        
    

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Set a timeout for the socket operations
        s.settimeout(10)  # 10 seconds timeout
        
        # Connect the socket to the server's address and port
        s.connect((IP_ADDRESS, PORT))

        # Define the JSON-RPC request payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params_dict
        }

        # Convert the payload to a JSON string and encode it
        message = json.dumps(payload).encode()

        # Calculate the size of the message
        size = len(message)

        # Construct the header
        # "pxr1" + 4-byte size (least significant byte first)
        header = b"pxr1" + struct.pack("<I", size)

        print("Sending:", payload)

        # Send the header and the message
        s.sendall(header + message)

        # Receive the response
        data = s.recv(1024)

        data_start = data.decode().rfind("{")
        data = data.decode()[data_start:]

    return data

def send_direct(method=None, params=None, message=None):
    if method is None:
        method = DEBUG_OUTPUT
        if params is None:
            params = ["message"]
        if message is None:
            message = ["Hello from Python!"]

    methods = method.split('.')
    method = ""
    for section in methods:
        method += f"{section}"

        if section == "Pixera":
            method += ".Direct."
        else:
            method += "."

    method = method[:-1]

    params_dict = {}

    if params is not None:
        # Convert the params and message lists to a dictionary
        params_dict = {params[i]: message[i] for i in range(len(params))}
        
    

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Set a timeout for the socket operations
        s.settimeout(10)  # 10 seconds timeout
        
        # Connect the socket to the server's address and port
        s.connect((IP_ADDRESS, PORT))

        # Define the JSON-RPC request payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params_dict
        }

        # Convert the payload to a JSON string and encode it
        message = json.dumps(payload).encode()

        # Calculate the size of the message
        size = len(message)

        # Construct the header
        # "pxr1" + 4-byte size (least significant byte first)
        header = b"pxr1" + struct.pack("<I", size)

        print("Sending:", payload)

        # Send the header and the message
        s.sendall(header + message)

        # Receive the response
        data = s.recv(1024)

        data_start = data.decode().rfind("{")
        data = data.decode()[data_start:]
        # data = data.decode()

    return data

def send_HTTP(method=None, params=None, message=None):
    if method is None:
        method = DEBUG_OUTPUT
        if params is None:
            params = ["message"]
        if message is None:
            message = ["Hello from Python!"]

    params_dict = {}
    if params is not None:
        # Convert the params and message lists to a dictionary
        params_dict = {params[i]: message[i] for i in range(len(params))}

    # Define the JSON-RPC request payload
    payload = {
        "jsonrpc": "2.0",
        "id": 1,  # Adjusted to match the provided ID
        "method": method,
        "params": params_dict
    }

    # Define the headers for the HTTP POST request to match the provided example
    headers = {
        "Content-Type": "text/xml; encoding=utf-8",
        "HOST": f"{ip}:{port}",
        "Content-Length": str(len(str(payload))),  # The length of the payload in bytes
        "Except": "100-continue",
        "Connection": "Keep-Alive"
    }

    print("Sending:", payload)

    # Send the HTTP POST request with headers
    response = requests.post(f"http://{ip}:{port}", headers=headers, json=payload)

    # Return the response data (can be modified to return other parts of the response if needed)
    return response.json()

def listen_to_udp(port):
    # Create a new UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the given port on all available network interfaces
    sock.bind(('0.0.0.0', port))

    print(f"Listening for UDP packets on port {port}...")

    while True:
        # Receive data (up to 65535 bytes, which is the maximum size of a UDP packet)
        data, addr = sock.recvfrom(65535)
        
        try:
            # Attempt to parse the data as JSON
            json_data = json.loads(data)
            print(f"Received JSON data from {addr}: {json_data}")
        except json.JSONDecodeError:
            print(f"Received non-JSON data from {addr}: {data.decode()}")


if __name__ == "__main__":
    ip = "127.0.0.1"  # Replace with your Pixera system's IP address
    port = 1401  # Replace with your Pixera system's port if different
    # result = send_HTTP()
    # result = send_TCP()
    # result = send_TCP_dl()

    #   handle registerParam(string instancePath);
    # => {"jsonrpc":"2.0", "id":681, "method":"Pixera.Direct.registerParam", "params":{"instancePath":"Abcd"}}
    # result = send_direct("Pixera.registerParam", ["instancePath"], ["Layer 1.Position.x"])
    # result = send_direct("Pixera.registerCamera", ["cameraName", "expectedFrequency"], ["Camera",1])

    listen_to_udp(1402)
    # if result:
        # print("Received:", result)
