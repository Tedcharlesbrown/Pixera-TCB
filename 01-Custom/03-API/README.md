# Pixera Python API
## PixeraPy

Made by Ted Charles Brown

### Usage
```
from PixeraPy import Pixera, API
ip = "127.0.0.1"  # Replace with your Pixera system's IP address
port = 1400  # Replace with your Pixera system's port if different

pixera = Pixera(ip, port)
api = API()
```

#### Examples
```
from time import sleep
# ----------------------------- DEFAULT DEBUGGING ---------------------------- #
output = pixera.send()
print(output)
sleep(1)
# ----------------------------- VERBOSE DEBUGGING ---------------------------- #
output = pixera.send(api.outputDebug("Hello from Python!"), verbose=True)
print(output)
sleep(1)
# ---------------------------- CHANGING API METHOD --------------------------- #
output = pixera.send(api.getApiRevision(), protocol="TCP_DL", port=1401, verbose=True)
print(output)
sleep(1)
# ------------------------- ACCESSING CONTROL MODULES ------------------------ #
output = pixera.send(["NewModule.Test"])
print(output)
sleep(1)
# ---------------------------- MULTIPLE PARAMETERS --------------------------- #
pixera.send(api.setTransportModeOnTimeline("Timeline 1", 1))
sleep(1)
pixera.send(api.setTransportModeOnTimeline("Timeline 1", 0))
sleep(1)
# ----------------------------- HANDLING HANDLES ----------------------------- #
screens = pixera.return_array(pixera.send(api.getScreens()))
for screen in screens:
    output = pixera.send(api.Screen().getName(int(screen)), verbose=True)
    print(output)
    sleep(1)


# ------------------------------- MANUAL INPUT ------------------------------- #
output = pixera.send(["Pixera.Utility.outputDebug", ["message"], ["Hello from Python!"]], verbose=True)
print(output)
```