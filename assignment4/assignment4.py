import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "e8u8jp",
        "typeId": "VITdevice",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: Name is  %s " % cmd.data['name'])
    print("Message received from IBM IoT Platform: Registration number is  %s" % cmd.data['reg'])

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
