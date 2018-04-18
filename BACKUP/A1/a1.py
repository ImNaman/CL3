import unittest

def binary_search(arr,low,high,key):
	
	if(low<=high):
	
		mid = int(low + (high - low)/2)
		
		if arr[mid]==key:
			return mid+1
		
		elif(key<arr[mid]):
			return binary_search(arr,low,mid-1,key)			

		elif(key>arr[mid]):
			return binary_search(arr,mid+1,high,key)

	else:
		return -1
	
arr = []

size=int(input('Enter Count: '))

for i in range(size):
	temp=int(input('Enter Element'))
	arr.append(temp)

arr.sort()
print(arr)

result=binary_search(arr,0,size-1,3)

if result != -1:
    print (result)
else:
    print ("Element is not present in array")



class MyTest(unittest.TestCase):
	def test_positive(self):
		self.assertEqual(binary_search([10,20,30,40,50],0,5,40),4)
	def test_negative(self):
		self.assertEqual(binary_search([10,20,30,40,50],0,5,4),-1)
unittest.main()    
