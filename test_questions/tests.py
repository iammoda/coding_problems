
def printArray(array):

	list = []
	s_column, e_column = 0, len(array[0]) - 1
	s_row, e_row = 0, len(array) -1

	while e_row >= s_row:

		for col in range(s_column, e_column + 1):
			if e_row >= s_row:
				list.append(array[s_row][col])
		s_row +=1

		for col in reversed(range(s_column, e_column +1)):
			if e_row >= s_row:
				list.append(array[s_row][col])
		s_row +=1

	return list

def printArray(array):
	start_pointer = 0
	end_pointer = len(array)-1
	modified_list = []
	while end_pointer > start_pointer:
		modified_list.append(array[start_pointer])
		start_pointer +=1
		modified_list.append(array[end_pointer])
		end_pointer -=1
	return modified_list

def printArray(array):
	i = len(array) - 3
	while i >= 0:
		print (array[i])
		i = i-3
	



array = [[1,2,3],[4,5,6],[7,8,9]]

answer = printArray(array)

print(answer)
