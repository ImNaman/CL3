import unittest

class search:
	arr=[]
	def __init__(self, array):
		self.arr=array
	def binary(self, low, high, el):
		if (low<high):			
			mid=int((low+high)/2)
			if self.arr[mid]==el:
				return mid;
			elif el<self.arr[mid]:
				return self.binary(low, mid-1,el )
			else:
				return self.binary(mid+1, high, el)
		else:
			return -1

class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(func("input1.txt", 3), True)
	def test2(self):
		self.assertEqual(func("input2.txt", -999), False)


def func(filename, num):
	a=[]
	try:
		with open(filename, 'r') as f:
			for line in f:
				a.append(int(line))
		a.sort()
		print a
		obj=search(a)
		indx=obj.binary(0, len(a)-1, num)
		if indx+1:
			print ("found at index", indx)
			return True
		else:
			print "Not found"
	except Exception as e:
		print "Error"
	return False

if __name__=='__main__':
	filename=raw_input("Enter input file name")
	num=input("Enter search element")
	func(filename, num)

print "--------------------------------------------"
print "Test Cases"
unittest.main()

