import os
from os.path import expanduser
import json
import time

install_directory = "Documents/GitHub/bad-apple-wallpaper/"
user = "temmie"

for aaaa in range(0,6900):
	counter = 1
	

	with open(f"{install_directory}apple-counter.json", "r") as file:
		count = json.load(file)

	counter = count["counter"]

	os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///home/{user}/{install_directory}bad-apple/frame{counter}.png")

	saving_counter = {}
	saving_counter["counter"] = counter+1
	with open(f"{install_directory}apple-counter.json", "w") as file:
		json.dump(saving_counter, file)
	time.sleep(0.02)