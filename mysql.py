
import MySQLdb

import paho.mqtt.client as paho
import time,random

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
client = paho.Client()
#client.username_pw_set("ab2017", "abx")
client.on_publish = on_publish
#client.connect("broker.mqttdashboard.com", 1883)
#client.connect("iot.eclipse.org",1883);
#client.connect("54.89.221.74",1883);
client.connect("localhost",1883);
client.loop_start()
while True:
    sicaklik = random.randint(0,100)
    (rc, mid) = client.publish("ab2017/temp", str(sicaklik), qos=1)
    conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="abx",
                  db="iotdb")
    x = conn.cursor()
    try:
       x.execute("""INSERT INTO olcumler VALUES (%s,%s)""",(5,sicaklik))
       conn.commit()
    except:
       conn.rollback()
    conn.close()
    time.sleep(10)
    
