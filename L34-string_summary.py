#string

name= "Aditya"
# string indexing
print(name[1])
# string slicing
print(name[-1:0:-1])
# take user input
# name=input()
# take two user input
username,age=input().split(",")
print(username)
print(age)
# len function 
print(len(name))
# lower, upper, title method
print(username.lower())
print(username.upper())
print(username.title())
# find, replace, center method
print(username.center(len(name)+5,"*"))
print(name.find(username))
print(name.replace('h','H'))
# string are imutable

