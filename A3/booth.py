bits=8
length=2*bits+1

def addbinary(a, b):
	c=0
	d=[0 for i in range(length)]
	i=length-1
	while i>=0:
		temp=a[i]+b[i]+c		
		d[i]=temp%2
		c=temp/2
		i-=1
	return d

def binaryToDecimal(b):
	print b
	temp =0
	i=len(b)-1
	j=0
	while i>=0:
		temp+=b[i]*pow(2, j)
		j+=1
		i-=1
	print temp
	return temp

def decimalToBinary(num):
	a=[0 for i in range(bits)]
	i=bits-1	
	while num!=0 and i>=0:
		a[i]=num%2
		num=num/2
		i-=1
	return a

def rightshift(a):
	i=length-1
	while i>=1:	
		a[i]=a[i-1]
		i-=1
	return a

def mybooth(a, b):
	num1=decimalToBinary(a)
	print num1
	num2=decimalToBinary(b)
	print num2
	x=decimalToBinary(-a)
	
	A=[0 for i in range(length)]
	S=[0 for i in range(length)]	
	P=[0 for i in range(bits)]
	
	for i in range(len(num2)):
        	P.append(num2[i])
   	P.append(0)

	for i in range(len(num1)):
		A[i]=num1[i]
		S[i]=x[i]

	print "A :", A
	print "S :", S
	print "P :", P

	for i in range(bits):
		print i, ")"
		if P[-1]==0 and P[-2]==0 or P[-1]==1 and P[-2]==1:
			P=rightshift(P)
			print P
		elif P[-2]==0 and P[-1]==1:
			P=addbinary(P, A)	
			print P
			P=rightshift(P)
			print P
		elif P[-2]==1 and P[-1]==0:
			P=addbinary(P, S)	
			print P
			P=rightshift(P)
			print P
	return P
			
