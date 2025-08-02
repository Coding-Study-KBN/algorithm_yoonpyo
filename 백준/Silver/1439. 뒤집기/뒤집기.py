s=list(input())
cnt0=0 
cnt1=0
if s[0]=='1':
    cnt0+=1
else:
    cnt1+=1
for i in range(len(s)-1): # 두번째 숫자부터 비교
    if s[i]!=s[i+1]:
        if s[i+1]=='1': # 두번째 숫자가 0이면
            cnt0+=1
        else: # 두번째 숫자가 1이면
            cnt1+=1
print(min(cnt0,cnt1))