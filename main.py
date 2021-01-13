L=[]
a=input('Enter numbers to be added to list: ')
L=list(map(int,a.split()))
for i in range(len(L)-1):
  for j in range(len(L)-i-1):
    if L[j]>L[j+1]:
      L[j],L[j+1]=L[j+1],L[j]
print('Sorted List:',L)
