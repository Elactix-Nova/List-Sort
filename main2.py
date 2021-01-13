L=[]
LVal=[]
LSorted=[]
Ind=0
a=input('Enter strings to be added to list: ')
L=a.split()
for I in L:
  Val=0
  for J in I:
    Val+=ord(J)
  LVal.append(Val)
LValSorted=LVal.copy()
for i in range(len(LValSorted)-1):
  for j in range(len(LValSorted)-i-1):
    if LValSorted[j]>LValSorted[j+1]:
      LValSorted[j],LValSorted[j+1]=LValSorted[j+1],LValSorted[j]
for k in LValSorted:
  Ind=LVal.index(k)
  LSorted.append(L[Ind])
print('Sorted List:',LSorted)
