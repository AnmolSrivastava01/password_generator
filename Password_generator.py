import random

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321!@#$%^&*()_"
while True:
    pass_lenght=int(input("enter the lenght"))
    pass_count=int(input("enter the lenght"))
    for i in range(pass_count):
        pasword=""
        for j in range(pass_lenght):
            pass_char=random.choice(characters)
            pasword=pasword+pass_char
        print("the generated password is",pasword) 
    repeat=input("do u need more")
    if repeat=="no" or "NO":
        break
    
print("OK")
