from pynput.keyboard import Listener
import datetime
import csv
import csv_read as rf

def write_to_file(key):

    letter = str(key)
    letter = letter.replace("'", "")
    curr = str(datetime.datetime.now().strftime("%H:%M:%S"))
    with open("log.csv", 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([curr, letter])
        f.flush()

# Collecting events until stopped
key_data={"Backspace":0,
          "Ctrl":0,
          "Alt":0,
          "Shift":0,
          "Caps":0,
          "Tab":0,
          "Esc":0,
          "Enter":0,
          "Space":0}
try:
    with Listener(on_press=write_to_file) as l:
        l.join()
except:
    print("Finished")
finally:
    key_data=rf.read_from_file(key_data)
    rf.clear_file()
    for keys, values in key_data.items():
        print(keys,":",values)

