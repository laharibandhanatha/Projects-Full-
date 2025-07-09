list1=list(map(int,input().split()))
sum1=0
list2=[]
for i in range(len(list1)-1,-1,-1):
    sum1+=list1[i]
    list2.append(list1[i])
print(list2,"sum=",sum1,"Average=",sum1/len(list1))