users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
count = 0
for key, data in users.items():
    count = 0
    print key
    for i in data:
        count += 1
        letterCount = len(i['first_name']) + len(i['last_name'])
        print count, "-", i['first_name'], i['last_name'], "-", letterCount
