import random
randlist=['AMERICA','QATAR','INDIA','BRITAIN','AUSTRALIA','ARGENTINA','FRANCE','BRAZIL','JAMAICA','NEW ZEALAND']
randch=random.choice(randlist)
f=''
for i in randch:
    if i==' ':
        f+=' '
    else:
        f+='-'
print(f)
while f.count('-')>0:
    inp=input('Enter your letter:')
    if inp in randch:
        l3=[]
        l1=list(f)
        l2=list(randch)
        for i in randch:
            if i==inp:
                index=l2.index(i)
                l3.append(index)
                l2[index]=1
        for j in l3:
            l1[j]=inp
        m=''
        for k in l1:
            m+=k
        f=m
    else:
        print('Sorry that letter is not there in the word. Please try again.')
    print(f)
        
