import json
import glob
import mysql.connector

# -----------------------------------
#  use glob
# -----------------------------------

#need pattern/path
pattern = "./data/*/*.json"
files = []
# list all files in data directory
for file in glob.glob(pattern):
    files.append(file)

#parse files
#make functn??
def readJson(file):
    with open(file) as parsed:
        parsed = json.load(file)
    return parsed
    

for file in files:
    inspect = readJson(file)
    print(inspect)