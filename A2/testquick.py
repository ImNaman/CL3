import unittest
from a2 import *

class Mytest(unittest.TestCase):
	def test1(self):
		try:			
			a=getdata("input1.xml")
			if a==None:
				self.fail("failed")
		except:
			self.fail("error loading file")
	def test2(self):
		self.assertEqual(getdata('input.xml'), [4 ,3, 2, 6, 5, 8])
unittest.main()
