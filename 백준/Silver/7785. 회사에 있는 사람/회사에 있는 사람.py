n=int(input())
company={}
for i in range(n):
    name,log=map(str,input().split())
    if log=="enter":
        company[name]=1
    else:
        del company[name]
print("\n".join(sorted(company.keys(), reverse=True)))