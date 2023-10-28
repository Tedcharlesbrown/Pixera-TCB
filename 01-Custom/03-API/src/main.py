from api import Pixera, Methods

if __name__ == "__main__":
    ip = "127.0.0.1"  # Replace with your Pixera system's IP address
    port = 1401  # Replace with your Pixera system's port if different

    pixera = Pixera(ip, port)
    api = Methods

    # print(api.send())    
    # print(pixera.send("TCP",method=api.GET_API_REVISION, verbose=True))
    print(pixera.send(method=api.CLOSE_APP, params=["saveProject"], message=[True]))
    
    
    
    