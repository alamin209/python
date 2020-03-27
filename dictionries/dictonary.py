student={'alamin':'From mirzapur','Niyamot':'From Chardpur','Other':['antor','fromrangpur','polin','same'] }

# I Customized the build in  none to my messed
# print(student.get('dfd',' "Not Found"'))
# New Added items to the dictonay
# student['testitems']='the test'
# update example for single key
# student['Niyamot'] = 'the test'
# print(student.get('testitemsgg','Not Found '))
# print(student)
# multipule add and update example in python
# student.update({'alamin':'bachaler','test':'Newly added', })
# print(student)
# delete example in dictonreies
# del  student['Niyamot']
# print(student)
# good thing we can remove and also show the value using pop in python
# alamin =student.pop('alamin')
# print(student)
# print(alamin)
# key and value and items example is also given here
# print(student.keys())
# print(student.values())
# print(student.items())

for key ,value in student.items():
    print(key ,value)
for key, value in student.items():
        print(key)
for key, value in student.items():
     print( value)