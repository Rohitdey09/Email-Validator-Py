#Email address validity checker with python
import re
regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):
    if(re.search(regex,email)):
        print("Valid email")
    else:
        print("Invalid email")
if __name__=='__main__':
    email=input("Enter email address: ")
    check(email)

