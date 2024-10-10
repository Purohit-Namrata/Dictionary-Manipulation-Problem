def returnSum(myDict):
    total_sum = sum(myDict.values())  # Calculate the sum directly
    for key in myDict:
        myDict[key] = total_sum  # Update each key with the total sum
    return myDict

my_dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(my_dict))
