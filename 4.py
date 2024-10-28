input_data = open('input.txt','r') 
data = input_data.read() 
N=int(data)
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
output_data = open('output1.txt','w')
output_data.write(str(list))
output_data.write(" ")
output_data.write(str(list1))
output_data.write(" ")
output_data.write('Длинна списка ='+str(list1))
input_data.close()
output_data.close()  
