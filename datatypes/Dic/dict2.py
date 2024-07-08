employee= {
  'name':'sanket',
   124:'id',
   'active':True,
   124:'id not change',
   'status':True
  }

  #get method:it will return value of specifed key

employee_method = employee.get('active')
print(employee_method)

#items() returns a list returing a tuple for each key and value pair
employee_method = employee.items()
print(employee_method)

#keys() return list containg keys
keys_method = employee.keys()
print(keys_method)

#values () list containg valus
values_method = employee.values()
print(values_method)

