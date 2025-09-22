student= {
    "name":"Shreya",
    "age":22,
    "city":"Pune"
}

print(student["name"])
print(student.get("city"))

student["grade"]="A" #add new key:vale
print(student)

student["age"]=23 #update existing data
print(student)

student.pop("city") #to remove
del student["age"]  #to delete by key
print(student)

for key, value in student.items():
    print(key, ":", value)

