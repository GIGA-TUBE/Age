import simplejson as json
import os
import time

running = True
while running:
    if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
        old_file = open("./ages.json", "r+")
        data = json.loads(old_file.read())
        print("Current age is", data["age"], "-- adding a year.")
        data["age"] = data["age"] + 1
        print("New age is", data["age"])
    else:
        old_file = open("./ages.json", "w+")
        data = {"name": "Venka", "age": 27}
        print("No file found, setting default age to", data["age"])

    old_file.seek(0)
    old_file.write(json.dumps(data))
    time.sleep(1)