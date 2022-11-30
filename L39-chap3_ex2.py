# Exercise-WATCH COCO
# Ask User's name and age
# if user's name start with('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# else print 'sorr, you cannot waych coco'

# solution 
user_name= input("Enter your name:- ")
user_age= input("Enter your age:- ")
user_age=int(user_age)
if user_age >=10 and (user_name[0]=='a' or user_name[0]=='A'):
    print("You can watch coco")
else:
    print("you cannot eatch coco")
