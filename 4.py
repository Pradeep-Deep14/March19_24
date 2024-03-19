a={}
a={(1,2,4):8,(4,2,1):10,(1,2):12}
sum=0
for k in a:
    sum += a[k]
print(len(a)+sum)