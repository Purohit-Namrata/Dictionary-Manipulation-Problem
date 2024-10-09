
def returnSum(myDict):

	list = []
	d=myDict
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)
	for i in d:
		d[i]=final
	
	return d

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
