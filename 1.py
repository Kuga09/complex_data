input_data = open('input.txt','r') 
data = input_data.read() 
N=int(data)
fact_N=1
list=[]
for i in range(2,N+1):
    fact_N=fact_N*i
    list.append(fact_N)
output_data = open('output.txt','w')
output_data.write(str(fact_N))
output_data = open('output1.txt','w')
output_data.write(str(list))
input_data.close()
output_data.close()  