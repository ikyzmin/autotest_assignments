
def initList(m):
	"""
	>>> initList(5)
	[0, 1, 2, 3, 4]
	""" 
	testList = []
	for i in range(0,m):
		testList.append(i)
	return testList

def duplicate(testList, a):
	"""
	Error in duplicate
	>>> duplicate([0,1,2,3,4,5],3)
	[0, 1, 1, 2, 3, 3, 4, 4, 5, 5]	
	>>>
	"""
	resultList = []
	for i in testList:
		resultList.append(i)
		if i>=a:
			resultList.append(i)
	return resultList

def sublist(testList,b):
	"""
	>>> sublist([0,1,2,3,4,5],3)
	[0, 1, 2]
	"""
	resultList=[]
	for i in testList:
		if i<b:
			resultList.append(i)
	return resultList

if __name__ == "__main__":
    import doctest
    doctest.testmod()

