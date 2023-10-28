import socket
import json
import struct
import requests

class Pixera:

    def __init__(self, ip_address="127.0.0.1", port=1401):
        self.IP_ADDRESS = ip_address
        self.PORT = port

    #     self.setup_constants()

    # def setup_constants(self):
    #     self.GET_API_REVISION = 'Pixera.Utility.getApiRevision'
    #     self.DEBUG_OUTPUT = 'Pixera.Utility.outputDebug'
    #     self.TOGGLE_TRANSPORT = 'Pixera.Compound.toggleTransport'
    #     self.GET_TIMELINE_SELECTED = 'Pixera.Timelines.getTimelinesSelected'
    #     self.SET_CURRENT_TIME_OF_TIMELINE_IN_SECONDS = 'Pixera.Compound.setCurrentTimeOfTimelineInSeconds'
    
    def send(self, protocol="TCP", method=None, params=None, message=None, verbose=False) -> str:
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
        if method is None:
            method = 'Pixera.Utility.outputDebug'
            if params is None:
                params = ["message"]
            if message is None:
                message = ["Hello from Python!"]

        result = None

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
        
    def send_tcp(self, method=None, params=None, message=None, verbose=False):
        params_dict = {}
        if params is not None:
            # Convert the params and message lists to a dictionary
            params_dict = {params[i]: message[i] for i in range(len(params))}
            
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
        params_dict = {}
        if params is not None:
            # Convert the params and message lists to a dictionary
            params_dict = {params[i]: message[i] for i in range(len(params))}
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
        if method is None:
            method = 'Pixera.Utility.outputDebug'
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

        params_dict = {}

        if params is not None:
            # Convert the params and message lists to a dictionary
            params_dict = {params[i]: message[i] for i in range(len(params))}
            
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
    

    def get_methods(self, input_path, output_path):
        """
        Parses a file to extract the formatted strings and converts them into a specified format.
        """
        with open(input_path, 'r') as f:
            lines = f.readlines()

        methods = []
        for line in lines:
            if line.startswith('`'):
                method_name = line.strip().strip('`')
                methods.append(method_name)

        # Convert to the desired format
        formatted_strings = []
        for method in methods:
            # Convert camel case to uppercase with underscores
            formatted_name = ''.join(['_' + i if i.isupper() else i for i in method.split(".")[-1]]).lstrip('_').upper()
            formatted_string = f'{formatted_name} = "{method}"'
            formatted_strings.append(formatted_string)

        with open(output_path, 'w') as f:
            f.write("class Methods:\n")
            for line in formatted_strings:
                f.write(f"    {line}\n")