def upperlower(string1):
    upp=low=0
    for c in string1:
        if(c>='A' and c<='Z'):
            upp+=1
        elif(c>='a' and c<='z'):
            low+=1
    print('number of upper :',upp)
    print('nuber of lower :',low)

a=input('enter the string : ')
upperlower(a)

