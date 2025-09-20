import csv

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