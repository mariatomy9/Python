oldnum=input()
length=len(oldnum)
while length%3!=0:
    oldnum='0'+oldnum
    length+=1




numlist=list(oldnum)
a=length//3

for i in range(1,a):
    numlist.insert((3*i)+(i-1),',')
num=''
for i in numlist:
    num+=i





def add(list1,suffix,num_name):
    numb_dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    s1=list1[0]
    
    if int(s1[0]) in numb_dict and int(s1[0])!=0 :
        num_name+=' '+numb_dict.get(int(s1[0]))
        num_name+=' hundred'
    s23=s1[1]+s1[2]
    
    for i in numb_dict:
        
        if int(s23)==i:
            num_name+=' '+numb_dict.get(i)
            break
        elif int(s23)>=i and (int(s23)-i)<=9 and i>19:
            num_name+=' '+numb_dict.get(i)
            break
    a=int(s23)-i
    
    if a==0:
        pass
    else:
        num_name+=' '+numb_dict.get(a)
    num_name+=' '+suffix

    return num_name



num_name=''
numlist=num.split(',')


while len(numlist)>0:
    lendict={1:'',2:'thousand',3:'million',4:'billion'}
    length=len(numlist)
    suffix=lendict.get(length)

    num_name=add(numlist,suffix,num_name)
    k=numlist.pop(0)


print(num_name)
    









    
