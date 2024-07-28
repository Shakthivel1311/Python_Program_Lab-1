people=[
   {"name":"john","age":30,"blood_group":"A+"},
   {"name":"jane smith","age":25,"blood_group":"B-"},
   {"name":"emily davis","age":40,"blood_group":"O+"},
   {"name":"Michaele brown","age":35,"blood_group":"AB-"},
   {"name":"William Jhonson","age":28,"blood_group":"A-"},
   {"name":"Emma Wilsson ","age":22,"blood_group":"B+"},
   {"name":"Oliver Martinez","age":33,"blood_group":"O-"},

   {"name":"Sofia Anderson","age":27,"blood_group":"AB+"},
   {"name":"james Thomas","age":45,"blood_group":"A+"},
   {"name":"Isabella Lee","age":38,"blood_group":"B-"},
]
for person in people:
   print("name",person["name"])
   print("age",person["age"])
   print("blood_group",person["blood_group"])
   print("\n-----------------------------")