letter=[[-1]*15 for i in range(5)]
for i in range(5):
    l=input()
    for k in range(len(l)):
        letter[i][k]=l[k]
answer=''
for i in range(15):
    for j in range(5):
        if letter[j][i]!=-1:
            answer+=letter[j][i]
print(answer)