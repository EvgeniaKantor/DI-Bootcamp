import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)

salary = data['company']['employee']['payable']['salary']
print("Salary:", salary)

data['company']['employee']['birth_data'] = "1970-01-01"

with open('json_file', 'w') as file_obj:
    json.dump(data, file_obj, indent=4)

print("JSON dat saved to 'json_file' file")
print(data)