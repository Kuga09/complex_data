N=int(input())
list=[0,1]
i=0
i1=1
while i1 < N:
    i1=i1+i
    list.append(i1)
    i=i1-i
list1=[]
for p in range(0,len(list)):
        if list[p] % 2 == 0:
            a=list[p]*2
            list1.append(a)
        else:
            a=list[p]**2
            list1.append(a)  
#max=list1[len(list1)-1]
max=0
for d in range(0,len(list1)):
     if list1[d]>max:
          max=list1[d]
min=max
for d in range(0,len(list1)):
     if list1[d]<min:
          min=list1[d]
if len(list1)%2==0:
     b=len(list1)/2-1
     m=(list[b]+list[b+1])/2
else:
     b=int((len(list1)-1)/2)
     m=list[b]
print(list1)
print('Длина списка = ', len(list1))
print('Максимальный элемент = ', max)
print('Минимальный элемент = ', min)
print('Медианное значение = ', m)