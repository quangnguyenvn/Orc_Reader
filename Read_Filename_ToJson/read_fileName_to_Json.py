import os
import json
import simplejson
import sys

# Load config file
#with open("config.json") as json_data_file:
    #data = json.load(json_data_file)

json_file_name = sys.argv[1]
my_json = {};
#arr = os.listdir(data["Word_Img"])
arr = os.listdir("Word_Img\\")
for x in arr:
	my_json[str(x)] = ""
resultJSON = json.dumps(my_json, indent=4, sort_keys=True)
jsonFile = open("CA\\" + str(json_file_name) + ".json", "w")
jsonFile.write(resultJSON)
#print("done writing to " + data["CA"])
jsonFile.close()
