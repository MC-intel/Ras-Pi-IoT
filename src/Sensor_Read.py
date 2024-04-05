import json
import datetime
import serial
import time
import pickle

refresh_rate = 10
multiplier = 10 # 20% sensors requires a multiplieresh_rate = 0.05
print("Running...")

def capture_data(port,baud):
    ser = serial.Serial(port,baud)

    try:
        with open("myresultsp.pickle", "rb") as ri:
            dic = pickle.load(ri)
    except:
        dic = {}
        dic["x"] = []
        dic["y"] = []
        
    ser.write(bytes("M 4\r\n", "utf-8")) # set display mode to show only CO2
    ser.write(bytes("K 2\r\n", "utf-8")) # set  operating mode
    ser.flushInput()

    while True:
        ser.write(bytes("Z\r\n", "utf-8"))
        resp = ser.read(10)
        resp = resp[:8]

        fltCo2 = float(resp[2:])
        data = fltCo2  * multiplier
        print(data)

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        if data != 0:
            dic["x"].append(timestamp)
            dic["y"].append(data)

        # convert the data to json and write to file
        with open("data.json", "w") as f:
            json.dump(dic, f)

        with open("myresultsp.pickle", "wb") as f:
            pickle.dump(dic, f)

        time.sleep(refresh_rate)
    
capture_data("/dev/ttyUSB0", 9600)
