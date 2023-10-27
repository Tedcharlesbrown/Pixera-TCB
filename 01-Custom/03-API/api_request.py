import socket
import json
import struct

IP_ADDRESS = "127.0.0.1"
PORT = 1401

GET_API_REVISION = 'Pixera.Utility.getApiRevision'
DEBUG_OUTPUT = 'Pixera.Utility.outputDebug'
TOGGLE_TRANSPORT = 'Pixera.Compound.toggleTransport'

getTimelinesSelected = 'Pixera.Timelines.getTimelinesSelected'
setCurrentTimeOfTimelineInSeconds = 'Pixera.Compound.setCurrentTimeOfTimelineInSeconds'

def send_JSON_TCP_dl(ip_address, port):
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

def send_JSON_TCP(method=None, params=None, message=None):
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
            "id": 25,
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


if __name__ == "__main__":
    ip = "127.0.0.1"  # Replace with your Pixera system's IP address
    port = 1401  # Replace with your Pixera system's port if different
    # result = send_JSON_TCP()
    # result = send_JSON_TCP(method="getApiRevision")
    # result = send_JSON_TCP(method=GET_API_REVISION)
    # result = send_JSON_TCP(method=TOGGLE_TRANSPORT, params=["timelineName"], message=["Timeline 1"])
    # result = send_JSON_TCP(method=getTimelinesSelected)
    result = send_JSON_TCP(method="Pixera.Timelines.getTimelineAtIndex", params=["index"], message=[6334283394240457]) #Timeline 1
    # result = send_JSON_TCP(method="Pixera.Timelines.getTimelineAtIndex", params=["index"], message=[6207985371032950]) #Pre-Show Check
    # result = send_JSON_TCP(method=setCurrentTimeOfTimelineInSeconds, params=["timelineName","time"], message=["6334283394240457",1])
    # result = send_JSON_TCP(method=setCurrentTimeOfTimelineInSeconds, params=["timelineName","time"], message=["Timeline 1",1])
    if result:
        print("Received:", result)
