star_index=[]
count2=0
count3=0
result=[]
j=0;l=0
for i in range(8):
    row=input()
    count1=row.count('*')
    if(count1>1):
        count2=count2+1
        result.append('invalid')
        star_index.clear() 
    elif(count2==0):
        star_index.append(row.index('*'))

r=list(dict.fromkeys(star_index))
if(len(star_index)!=len(r)):
    result.append('invalid')
    star_index.clear()
    
while(l<=len(star_index)-1):
    x=1
    for m in range(8):
        a=star_index[l]+x
        b=star_index[l]-x
        index1=l+x
        index2=l-x
        if(a==8):
            break
        if(a>=0 and index1>=0 and a<=7 and index1<=7):
            if(star_index[index1]==a):
                result.append('invalid')
                star_index.clear()
                break
            if(index2>=0 and index2<=7):
                if(star_index[index2]==a):
                    result.append('invalid')
                    star_index.clear()
                    break
        if(b>=0 and index2>=0 and b<=7 and index2<=7):
            if(star_index[index2]==b):
                result.append('invalid')
                star_index.clear()
                break
            if(index1>=0 and index1<=7):
                if(star_index[index1]==b):
                    result.append('invalid')
                    star_index.clear()
                    break
        x=x+1
    l=l+1
if 'invalid' in result:
    print('invalid')
else:
    print('valid')  
