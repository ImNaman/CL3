bits = 8
length = 2*bits+1

def addBinary(a,b):
    c = 0
    d = [0 for i in range(len(a))]
    i = len(a)-1
    while i>=0:
        temp = a[i] + b[i] + c
        d[i] = temp%2
        c = temp/2
        i-=1
    return d

def rightShift(a):
    i = length-1
    while i>=1:
        a[i] = a[i-1]
        i-=1
    return a    

def binaryToDecimal(b):
    temp = 0
    print (b)
    i = len(b) -1
    i2 = i
    j=0
    if b[0]==1:
        while i2>=1:
            if b[i2]==0:
                b[i2]=1
            else:
                b[i2]=0
            i2-=1

        t = [0 for i in range(length-1)]
        t[-1]=1
        print t
        print b
        b = addBinary(b,t)
    while i>=0:
        temp = temp + b[i]*pow(2,j)
        j+=1
        i-=1
    print (temp)
    if temp > (pow(2,len(b)-1)):
        temp = pow(2,len(b)-1) - temp
    print ("*********",temp)
    print ("Binary: ",b)
    return temp         


def decimalToBinary(num):  
    a = []
    for i in range(bits):
        a.append(0)
        
    i = bits-1
    while num!=0 and i>=0:
        a[i]=(num%2)
        num=num/2
        i-=1        
    return a
   
def MyBooths(num1,num2):
    print("in my booths")
    a = decimalToBinary(num1)
    print a
    b = decimalToBinary(num2)
    print b
    x = decimalToBinary(-num1)
    print x
    
    print('\n')    
    A = [0 for i in range(length)]
    S = [0 for i in range(length)]
    P = [0 for i in range(bits)]
   
    print "A = ",A
    print "S = ",S
    print "P = ",P
    
    print('\n')
    
    for i in range(len(b)):
        P.append(b[i])
    P.append(0)
    
    print "P = ",P
    print('\n')    
   
    for i in range(len(a)):
        A[i]=(a[i])
        S[i]=(x[i])
          
    print "A = ",A
    print "S = ",S
    print "P = ",P
    print P[-1]
    print('\n')
    
    for i in range(bits):
    	print('\n')
	
        print i,")"
        if P[-1]==0 and P[-2]==0 or P[-1]==1 and P[-2]==1:
            P = rightShift(P)
            print P
        elif P[-2]==1 and P[-1]==0:
            P = addBinary(P,S)
            print P
            P = rightShift(P)
            print P
        elif P[-2]==0 and P[-1]==1:        
            P = addBinary(P,A)
            print P
            P = rightShift(P)
            print P
    
    return P

#MyBooths(2,3)
#print(binaryToDecimal(0011))
