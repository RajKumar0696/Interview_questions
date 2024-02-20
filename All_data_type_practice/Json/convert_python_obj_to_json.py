import json
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}

j_data = json.dumps(python_obj)
print(j_data)
