#WRITTEN BY: Ted Charles Brown

import socket
import json
import struct
import requests

class Pixera:
    DEFAULT_PORT = 1400

    def __init__(self, ip_address="127.0.0.1", port=DEFAULT_PORT):
        self.IP_ADDRESS = ip_address
        self.PORT = port

    def send(self, array=[], protocol="TCP", port=DEFAULT_PORT, verbose=False,) -> str:
        """
        Send a message using the specified protocol.

        :param protocol: The protocol to use for sending the message. 
                         Options are "TCP", "TCP_DL", "HTTP", "DIRECT".
        :param method: The method to use.
        :param params: Parameters for the method.
        :param message: The message to send.
        :param verbose: Print the send message and the response.
        :return: Response data.
        """
        # Default values for method, params, and message
        method, params, message = None, None, None

        # Unpack the array based on its length
        if len(array) >= 1:
            method = array[0]
        if len(array) >= 2:
            params = array[1]
        if len(array) == 3:
            message = array[2]

        if method is None:
            method = 'Pixera.Utility.outputDebug'
            if params is None:
                params = ["message"]
            if message is None:
                message = ["Hello from Python!"]

        result = None

        self.PORT = port

        if protocol == "TCP":
            result = self.send_tcp(method, params, message, verbose)
        elif protocol == "TCP_DL":
            result = self.send_tcp_dl(method, params, message, verbose)
        elif protocol == "HTTP":
            result = self.send_http(method, params, message, verbose)
        elif protocol == "DIRECT":
            result = self.send_direct(method, params, message, verbose)

        if verbose:
            return result
        else: 
            result_index = result.rfind("result\":")
            result = result[result_index + 8:-1]
            return result
        
    def create_params_dict(self, params, message):
        if params is not None:
            # Check if params is a single string and split it if necessary
            if isinstance(params, str):
                params = params.split(',')

            # Trim whitespace from each parameter name
            params = [param.strip() for param in params]

            # Create and return the dictionary
            return {params[i]: message[i] for i in range(len(params))}

        
    def send_tcp(self, method=None, params=None, message=None, verbose=False):
        params_dict = self.create_params_dict(params, message)
                 
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the socket operations
            s.settimeout(10)  # 10 seconds timeout
            
            # Connect the socket to the server's address and port
            s.connect((self.IP_ADDRESS, self.PORT))

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

            message = header + message
            # Send the header and the message
            if verbose: print("Sending:", message)
            s.sendall(message)

            # Receive the response
            data = s.recv(1024)
            data_start = data.decode().rfind("{")
            data = data.decode()[data_start:]

        return data


    def send_tcp_dl(self, method=None, params=None, message=None, verbose=False):
        params_dict = self.create_params_dict(params, message)

        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the socket operations
            s.settimeout(10)  # 10 seconds timeout
            
            # Connect the socket to the server's address and port
            s.connect((self.IP_ADDRESS, self.PORT))

            # Define the JSON-RPC request payload
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": method,
                "params": params_dict
            }

            message = (json.dumps(payload) + '0xPX').encode()

            # Send the request with the "0xPX" delimiter at the end
            if verbose: print("Sending:", message)
            s.sendall(message)

            # Receive the response
            data = s.recv(1024)


        return data.decode()
    
        
        
    def send_http(self, method=None, params=None, message=None, verbose=False):
        params_dict = self.create_params_dict(params, message)

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
            "HOST": f"{self.IP_ADDRESS}:{self.PORT}",
            "Content-Length": str(len(str(payload))),  # The length of the payload in bytes
            "Except": "100-continue",
            "Connection": "Keep-Alive"
        }

        # Send the HTTP POST request with headers
        if verbose: print("Sending:", headers, payload)
        response = requests.post(f"http://{self.IP_ADDRESS}:{self.PORT}", headers=headers, json=payload)

        # Return the response data (can be modified to return other parts of the response if needed)
        return response.json()

    def send_direct(self, method=None, params=None, message=None, verbose=False):

        # append direct to the method
        methods = method.split('.')
        method = ""
        for section in methods:
            method += f"{section}"

            if section == "Pixera":
                method += ".Direct."
            else:
                method += "."
        method = method[:-1]

        params_dict = self.create_params_dict(params, message)

        if params is not None:
            # Convert the params and message lists to a dictionary
            try:
                params_dict = {params[i]: message[i] for i in range(len(params))}
            except:
                pass#TODO: handle this error - message index out of range
            
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the socket operations
            s.settimeout(10)  # 10 seconds timeout
            
            # Connect the socket to the server's address and port
            s.connect((self.IP_ADDRESS, self.PORT))

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

            message = header + message
            # Send the header and the message
            if verbose: print("Sending:", message)
            s.sendall(message)

            # Receive the response
            data = s.recv(1024)

            data_start = data.decode().rfind("{")
            data = data.decode()[data_start:]
            # data = data.decode()

        return data
    
    def return_array(self, input):
        output = input[1:-1].split(',')
        return output