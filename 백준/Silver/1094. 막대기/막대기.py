bar=[64,32,16,8,4,2,1]
count=0
x=int(input())
for i in range(len(bar)):
    if x>=bar[i]:
        count+=1
        x-=bar[i]
    if x==0:
        break
print(count)
