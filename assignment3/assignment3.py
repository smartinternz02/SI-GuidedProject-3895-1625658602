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
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="lighton"):
        print("LIGHT ON")
    elif (m=="lightoff"):
        print("LIGHT OFF");
    elif(m=="tapopen"):
        print("WATER TAP OPEN")
    elif(m=="tapclose"):
        print("WATER TAP CLOSED")
            

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    level=random.randint(-20,125)
    intensity=random.randint(0,100)
    myData={'water_tank_level':level, 'light_intensity':intensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
