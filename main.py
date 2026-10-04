import datetime
print("Hello i am chat Bot")
name=input("Please enter your name :")
print("Hello",name)
print("What would you like to know today?")
answer=input("Please choose one of the two option below : 1)Date or 2)time")
if answer=="1":
    print(datetime.datetime.now().date())
else:
    print(datetime.datetime.now().time())