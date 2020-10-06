import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "lntrcs"
deviceType = "raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        i = cmd.data['command']
        if i=='MEDICINE':
                print("Time to take medicine")
                
        elif i=='EMERGENCY':
                print("Emergency! Need your help!!")
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

#Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
       
        data = { '8:00' : 'Omeprazole', '12:00' : 'Atenolol', '5:00' : 'Istamet', '7:30': 'Metformin'}   #print (data)
        def myOnPublishCallback():
            print ( '8:00 : Omeprazole', '12:00 : Atenolol', '5:00 : Istamet', '7:30 : Metformin')

        success = deviceCli.publishEvent("Medication", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback
#Disconnect the device and application from the cloud
deviceCli.disconnect()
