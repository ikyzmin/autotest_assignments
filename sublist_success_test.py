import unittest
from lists import *

class TestList(unittest.TestCase):
	def test_sublist_success(self):
		self.assertEqual([1,2,3,4],sublist([1,2,3,4,5,6,7,8,9,10],5))		
if __name__ == '__main__':
	unittest.main()
