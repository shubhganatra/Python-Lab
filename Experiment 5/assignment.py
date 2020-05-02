list=[]
sum=0
while sum>=0:
    a=int(input('Enter A Number: '))
    if a>1000 or a<-1000:
        print('Invalid Number, Enter Again')
        continue
    list.append(a)
    sum=sum+a
    print('List Of Numbers Entered: ',list)
    print('Sum Of Numbers In List: ',sum)