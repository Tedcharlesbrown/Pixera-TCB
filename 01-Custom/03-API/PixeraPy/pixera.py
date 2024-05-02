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

            # Combine the header and the message
            full_message = header + message

            # Send the complete message
            if verbose: print("Sending:", full_message)
            s.sendall(full_message)

            # Receive the response
            data = s.recv(1024)
            if verbose: print("Received raw data:", data)

            # Find the beginning of the JSON part by locating the first '{' character
            json_start_index = data.find(b'{')

            # Only decode the JSON part
            if json_start_index != -1:
                json_data = data[json_start_index:].decode('utf-8')
                if verbose: print("Decoded JSON data:", json_data)
                return json_data
            else:
                if verbose: print("No JSON data found in the response.")
                return None


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

            # Convert the payload to a JSON string, append the '0xPX' delimiter, and encode it
            message = (json.dumps(payload) + '0xPX').encode()

            # Send the message
            if verbose: print("Sending:", message)
            s.sendall(message)

            # Receive the response
            data = s.recv(1024)
            if verbose: print("Received raw data:", data)

            # Attempt to decode the response safely
            try:
                decoded_data = data.decode('utf-8')
                if verbose: print("Decoded data:", decoded_data)
                return decoded_data
            except UnicodeDecodeError as e:
                if verbose: print("Decode error:", e)
                # Handle decoding error, return error message or None, depending on your error handling policy
                return "Error decoding response."
    
        
        
    def send_http(self, method=None, params=None, message=None, verbose=False):
        params_dict = self.create_params_dict(params, message)

        # Define the JSON-RPC request payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,  # Consistent ID for the JSON-RPC request
            "method": method,
            "params": params_dict
        }

        # Convert the payload to a JSON formatted string to calculate the correct content length
        json_payload = json.dumps(payload)

        # Define the headers for the HTTP POST request
        headers = {
            "Content-Type": "application/json",  # Corrected to 'application/json' for JSON-RPC
            "HOST": f"{self.IP_ADDRESS}:{self.PORT}",
            "Content-Length": str(len(json_payload)),  # The length of the JSON string in bytes
            "Expect": "100-continue",  # Corrected typo 'Except' to 'Expect'
            "Connection": "Keep-Alive"
        }

        # Send the HTTP POST request with headers
        if verbose: 
            print("Sending:", headers, payload)
        response = requests.post(f"http://{self.IP_ADDRESS}:{self.PORT}", headers=headers, data=json_payload)

        # Return the response data (can be modified to return other parts of the response if needed)
        if response.ok:
            return response.json()
        else:
            if verbose:
                print("Failed to receive valid response:", response.text)
            return None

    def send_direct(self, method=None, params=None, message=None, verbose=False):
        # Append ".Direct" to the method after "Pixera"
        methods = method.split('.')
        method = ""
        for section in methods:
            method += section
            if section == "Pixera":
                method += ".Direct"
            method += "."

        method = method.rstrip('.')  # Remove the trailing dot

        # Create or update params dictionary based on provided lists
        if params is not None and message is not None:
            try:
                params_dict = {params[i]: message[i] for i in range(len(params))}
            except IndexError:
                if verbose:
                    print("Error: 'message' list is shorter than 'params' list.")
                return "Parameter and message length mismatch."
        else:
            params_dict = self.create_params_dict(params, message)

        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # 10 seconds timeout
            s.connect((self.IP_ADDRESS, self.PORT))

            # Define the JSON-RPC request payload
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": method,
                "params": params_dict
            }

            # Serialize and encode the payload
            message = json.dumps(payload).encode()
            size = len(message)
            header = b"pxr1" + struct.pack("<I", size)
            message = header + message
            
            if verbose:
                print("Sending:", message)
            s.sendall(message)

            # Receive and decode the response
            data = s.recv(1024)
            try:
                data_start = data.decode('utf-8').rfind("{")
                data = data.decode('utf-8')[data_start:]
            except UnicodeDecodeError as e:
                if verbose:
                    print("Decode error:", e)
                return "Error decoding response."

        return data
    
    def return_array(self, input):
        output = input[1:-1].split(',')
        return output