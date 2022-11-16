# Q3). Write a program in Python for, How to find all pairs in array of integers whose
#  sum is equal to given number.
def printPairs(arr, n, sum):
	# count = 0
	# Consider all possible
	# pairs and check their sums
	for i in range(0, n ):
		for j in range(i + 1, n ):
			if (arr[i] + arr[j] == sum):
				print(arr[i],arr[j],sep=" ")
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)
