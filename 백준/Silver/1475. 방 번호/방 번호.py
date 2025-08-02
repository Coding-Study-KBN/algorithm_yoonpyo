import math
n=list(input())
dasom={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
for k  in n:
    if k=='9' or k=='6':
        if dasom["6"]<=dasom["9"]:
            dasom["6"]+=1
        else:
            dasom["9"]+=1
    else:
        dasom[k]+=1
print(max(dasom.values()))