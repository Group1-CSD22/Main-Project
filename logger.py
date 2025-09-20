import threading
from time import sleep

from pynput.keyboard import Listener
import datetime
import csv

key_data={"Backspace":0,
          "Ctrl":0,
          "Alt":0,
          "Shift":0,
          "Caps":0,
          "Tab":0,
          "Esc":0,
          "Enter":0,
          "Space":0}


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    curr = str(datetime.datetime.now().strftime("%H:%M:%S"))
    with open("log.csv", 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([curr, letter])
        f.flush()

def read_from_file(data):
    with open("log.csv", 'r') as f:
        reader = csv.reader(f)
        for key in reader:
            if (key[1] == "Key.backspace"):
                data["Backspace"]=data["Backspace"]+1
            elif (key[1] == "Key.ctrl"):
                data["Ctrl"]=data["Ctrl"]+1
            elif (key[1] == "Key.esc"):
                data["Esc"]=data["Esc"]+1
            elif (key[1] == "Key.alt" or key[1] == "Key.alt_r"):
                data["Alt"]=data["Alt"]+1
            elif (key[1] == "Key.caps_lock"):
                data["Caps"]=data["Caps"]+1
            elif (key[1] == "Key.tab"):
                data["Tab"]=data["Tab"]+1
            elif (key[1] == "Key.shift"):
                data["Shift"]=data["Shift"]+1
            elif (key[1] == "Key.enter"):
                data["Enter"]=data["Enter"]+1
            elif (key[1] == "Key.space"):
                data["Space"]=data["Space"]+1
    return data

def clear_file():
    with open("log.csv", 'w') as f:
        writer = csv.writer(f)


# Collecting events until stopped

def thread1():
    print("start t1")
    try:
        with Listener(on_press=write_to_file) as l:
            l.join()
    except:
        print("finished")

def thread2():
     print("start t2")
     while(True):
        key_data=read_from_file(key_data)
        clear_file()
        for keys, values in key_data.items():
            print(keys,":",values)
        sleep(10)

t1 = threading.Thread(target=thread1())
t2= threading.Thread(target=thread2())

t1.start()
t2.start()

t1.join()
t2.join()
