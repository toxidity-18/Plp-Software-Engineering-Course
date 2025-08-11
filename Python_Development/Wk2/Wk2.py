# Creating a list .
list_a = [1,2,3,4,5] # int
list_b = ['sam','kam'] # strings 
list_c = ['sam',2,4.5] # str and int 
list_d = [True] # bool
list_e = [1,2,['sam',False],3.4] # nested list 
# Accessing elements in a list .
list_a[0] # 1
list_b[1] # 'kam'
list_c[2] # 4.5
list_d[0] # True
list_e[2][0] # 'sam'
# Slicing elements in a list .
list_f = [1,'sam',3.5,'kam',[1,True],False]
list_f[0] # 1
list_f[2:5] # 3.5, 'kam',[1,True]
list_f[-3] # 'kam'
list_f[2:] # 3.5,'kam',[1,True],False
# Adding elements in a list .
# append()
numbers = [1,2,3,4]
numbers.append(5) # [1,2,3,4,5]
#extend()
prime_num=[2,3,5]
even_num=[0,2,4,6]
even_num.extend(prime_num) # [0,2,4,6,2,3,5]
