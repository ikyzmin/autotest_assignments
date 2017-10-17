import unittest
from lists import *

class TestList(unittest.TestCase):
	def test_duplicate_success_incorrect(self):
		self.assertEqual([0,1,2,3,4,5,6,7,8,9],initList(10))	

if __name__ == '__main__':
	unittest.main()
