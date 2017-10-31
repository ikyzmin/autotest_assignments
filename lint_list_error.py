
initList(m):
	testList = []
	for i in range(0,m):
		testList.append(i)
	return testList

def duplicate(testList, a):
	resultList = []
	for i in testList:
		resultList.append(i)
		if i>=a:
			resultList.append(i)
	return resultList

def sublist(testList,b):
	resultList=[]
	for i in testList:
		if i<b:
			resultList.append(i)
	return resultList


