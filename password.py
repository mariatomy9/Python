def setpassword():
  n1=int(input("Set password:"))
  n2=int(input("Confirm password:"))
  if (n1==n2):
    print("Password is set")
    return n1
  else:
    print("Try again")
    return setpassword()


import time
print("Phone locked")
n=setpassword()
c1=4
while True:
  
  e=int(input("Enter password to unlock:"))
  if (e==n):
    print("Access permitted")
    break
  else:
    print('You have',c1,'more attempts')
    c1-=1
  if c1==-1:
    print("Try again,after 10 secs")
    time.sleep(10)
    c1=4
    
