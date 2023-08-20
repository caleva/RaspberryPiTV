import paho.mqtt.client as mqtt
import json
import cec

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("TV_STATE")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def message_TV_STATE(client, userdata, message):
    mess = json.loads(message.payload.decode())


    if mess.get("State") == True:
        print(True)
    elif mess.get("State") == False:
        print(False)


cec.init()

 tv = cec.Device(cec.CECDEVICE_TV)
 tv.power_on()



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.message_callback_add("TV_STATE", message_TV_STATE)

client.connect("192.168.1.29", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()