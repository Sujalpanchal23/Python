#example 1
'''a = 10
b = 5
c = a/b
print(c, type(c))

result = int(c)
print(result, type(result))


print(int(10/5))

print(int(input("Enter the value of a :"))+ int(input("Enter the value of b :")))
print(float(input("Enter the value of a : ")) * int(input("Enter the value of b :")))

'''
'''
a = 100
b = float(a)
print(b,type(b))
#output
#100.0 <class 'float'>

a = 100
b = bool(a)
print(b, type(b))
#output
#True <class 'bool'>

a = 0
b = bool(a)
print(b,type(b))
#output
#False <class 'bool'>


a = 100
print(str(a), type(str(a)))
#output
#100 <class 'str'>

a = 100
b = str(a)
print(b, type(str(a)))
#output
#100 <class 'str'>

a = 100
b = complex(a)
print(b, type(b))
#output
#(100+0j) <class 'complex'>

a = 0
b = complex(a)
print(b, type(b))
#output
#0j <class 'complex'>
'''
'''
#converting float into integer
a = 29392.232
b = int(a)
print(b, type(b))
#output
#29392 <class 'int'>

a = 29392.232
b = bool(a)
print(b, type(b))
#output
#True <class 'bool'>

a = 0.0
print(bool(a), type(a))
#output
#False <class 'float'>

a = 1010.1
b = complex(a)
print(b, type(b))
#output
#(1010.1+0j) <class 'complex'>

a = 0.0
print(complex(a), type(a))
#output
#0j <class 'float'>

a = 218.21
b = str(a)
print(str(b), type(b))
#output
#218.21 <class 'str'>

#converting boolean into int
print(int(True))
print(int(False))
#output
#1
#0

#converting boolean into float
print(float(True))
print(float(False))
#output
#1.0
#0.0


#converting boolean into complex
print(complex(True))
print(complex(False))
#output
#(1+0j)
#0j

#converting boolean into string
print(str(True))
print(str(False))
#output
#True
#False
'''
#converting Complex into int
'''a = 23+23j
b = a.real
print(b, type(b))
c = int(b)
print(c, type(c))
#output
#23.0 <class 'float'>
#23 <class 'int'>

#another method to convert complex into int
print(int(23+3j.real))
print(int(23+3j.imag))
#output
#23 (.real answer)
#26 (.imag answer)

#converting Complex into float
print(float(23+3j.real))
print(float(23+3j.imag))
#output
#23.0 <class 'float'>
#26.0

#converting Complex into bool
print(bool(23+3j.real))
print(bool(23+3j.imag))
print(bool(0+0j.real))
print(bool(0+0j.imag))
#True
#True
#False
#False


#converting Complex into str
print(str(23+3j.real))
print(str(23+3j.imag))
#output
#23.0
#26.0
'''

'''a = 23+3j
b = a.real
print(b, type(b))
print(int(23+3j.imag))'''

#comverting string to int
a = 23+3j
b = a.real
print(b, type(b))
















































