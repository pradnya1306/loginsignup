import re
import os
import json

# re module:-RegEx can be used to check if a string contains the specified search patter
# os module:-Python OS module provides the facility to establish the interaction between the user and the operating system
def storng_password(password):
    flag=True
    while flag==True:
    
        if len(password)>6 and len(password)<16:
            if re.findall("[@#$%&*!]", password):#findall-The findall() function returns a list containing all matches.
                if re.findall("[a-z]",password):
                    if re.findall("[A-Z]",password):
                        if re.findall("[0-9]",password):
                            print("your password is strong password")

                            return password
                            
                        else:
                            print(password,"At least password should contain one number")
                            password=input("enter your 1st password : ")
    
                    else:
                        print(password,"At least password should contain one Upper case letter")
                        password=input("enter your 1st password : ")
            
                else:
                    print(password,"At least password should contain one lower case letter")
                    password=input("enter your 1st password : ")
                
            else:
                print(password,"At least password should contain one special character")
                password=input("enter your 1st password : ")
            
        else:
                print(password,"At least password should length 6 to 16 digit")
                password=input("enter your 1st password :")

def checkpassword(a,password2):
    if password2==a:
        print("password created.")
    else:
        print("Both password are not same")
        password2=input("enter your confirm password : ")
        checkpassword(a,password2)


#*********code start from here***************

print("Welcome to login and sign up page")
login_signup=input("what you choose login or signup : ")

file=os.path.exists("user.json")

if file==False:
    
    if login_signup=="signup":
        user_name=input("enter your user name : ")
        password1=input("enter your 1st password : ")
        a=(storng_password(password1))
        print(a)
        password2=input("enter your confirm password : ")
        checkpassword(a,password2)
        print("congrats",user_name,"you are Signed  up Successfully.")
        
        description=input("Information about you :")
        date_of_birth=input("enter your date of birth (DD-MM-YYYY): ")
        hobbies=input("enter your hobies : ")
        gender=input("enter your gender (male or female) :")
        
        
        mylist=[]
        user={}
        list1=["username","password","description","dob","hobbies","gender"]
        list2=[user_name,a,description,date_of_birth,hobbies,gender]
        for i in range(len(list1)):
            user.update({list1[i]:list2[i]})
        mylist.append(user)

        with open ("user.json","a")as p:
            json.dump(mylist,p,indent=4,)
    print(user_name,"your account is successfully created")

elif file==True:
    if login_signup=="signup":
        user_name=input("enter your user name : ")
        password1=input("enter your 1st password : ")
        a=storng_password(password1)
        print(a)
        password2=input("enter your confirm password : ")
        checkpassword(a,password2)
        
        m=open("user.json","r")
        usname=m.read()
        if user_name in usname:
            print("This account is already exists")
        else:
            print("congrats",user_name,"you are Signed  up Successfully.")
            description=input("Information about you : ")
            date_of_birth=input("enter your date of birth : ")
            hobbies=input("enter your hobies : ")
            gender=input("enter your gender (male or female) :")
            
            user={}
            list1=["username","password","description","dob","hobbies","gender"]
            list2=[user_name,a,description,date_of_birth,hobbies,gender]
            for i in range(len(list1)):
                user.update({list1[i]:list2[i]})
            

            with open("user.json","r")as p:
                data=json.load(p)
                data.append(user)
                with open("user.json","w")as p:
                    json.dump(data,p,indent=4)

    elif login_signup=="login":
        login_name=input("enter the name : ")
        login_password=input("enter the password : ")
        with open("user.json","r")as p:
            data=json.load(p)

            for i in data :
    
                if i["username"]==login_name:
                    if i["password"]==login_password:
                            print("login successfully")
                
                            for x,y in i.items():
                                print("your",x,"is",y)
                            break
                    else:
                        print("password is incorrect")
                        break
            else:
                print("invalid account")
        