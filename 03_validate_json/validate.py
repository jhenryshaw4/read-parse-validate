import glob
import json

# -----------------------------------
#  validate json
# -----------------------------------

def removeQuotes(string):
    pass

def validate(salary):
    try:
        key = ['id']
        key = ["position"]
        key = ["created_at"]
        key = ["created_meta"]
        key = ["updated_at"]
        key = ["updated_meta"]
        key = ["meta"]
        key = ["name"]
        key = ["title"]
        key = ["department_name"]
        key = ["regular"]
        key = ["retro"]
        key = ["other"]
        key = ["overtime"]
        key = ["injured"]
        key = ["detail"]
        key = ["quinn"]
        key = ["total_earnings"]
        key = ["zip"]
    except Exception as e:
        return False
    return

# -----------------------------------
#  parse json function
# -----------------------------------

# load file and parse json
def readJson(file):
    with open(file) as p:
        return json.load(p)


# -----------------------------------
#  loop files, parse, validate
# -----------------------------------

pattern = "./data/*/*.json"
#* gives everything
#.json just gives json files
data =[]
for file in glob.glob(pattern):
    data.append(file)

for file in data:
    salaries = readJson(file)

    #validate here
    for salary in salaries:
        print("file:", file, "-validation:", validate(salary))