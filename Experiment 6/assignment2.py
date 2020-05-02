while(1):
    n=int(input('Enter Size Of Array: '))
    if n>0 and n<1000:
        break
    else:
        print('Invalid Value Of n, Re-enter: ')
        continue
s=[]
for i in range(n):
    while(1):
        x=int(input('Enter Element: '))
        if x>0 and x<1000000000:
            s.append(x)
            break
        else:
            print('Invalid Value Of s, Re-enter: ')
            continue
def seq(s,n):
    s1, s2=[],[]
    h=dict.fromkeys(s,0)
    for i in range(n):
        h[s[i]]+=1
        if h[s[i]]==1:
            s1.append(s[i])
        elif h[s[i]]==2:
            s2.append(s[i])
        else:
            print(False)
            return
    s1.sort()
    s2.sort(reverse=True)
    print(True)
    print('Strictly Increasing Array: ', s1)
    print('Strictly Decreasing Array: ', s2)
    return
seq(s,n)