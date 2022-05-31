def tupleToList(tuple):
	try:
		return list(tuple)
	except:
		return [tuple]

def bestPath(matrix):
	rows = len(matrix)
	for row in range(0, rows):
		for column in range(0,row+1):
			if row == 0:
				continue
			elif row == 1 and column == 0:
				matrix[row][column] += matrix[0][0]
			elif column == 0:
				matrix[row][column] += min(matrix[row-1][column], matrix[row-1][column+1])
			elif column == 0:
				matrix[row][column] += min(matrix[row-1][column], matrix[row-1][column+1])
			elif column == len(matrix[row])-1:
				matrix[row][column] += matrix[row-1][column-1]
			elif column == len(matrix[row])-2:
				matrix[row][column] += min(matrix[row-1][column-1], matrix[row-1][column])
			else:
				matrix[row][column] += min(matrix[row-1][column-1], matrix[row-1][column], matrix[row-1][column+1])
	return min(matrix[-1])


def inverse(matrix):
	for i in matrix:
		for j in i:
			matrix[i][j] = -1*matrix[i][j]
	return matrix

def worstPath(matrix):
	return -1*bestPath(inverse(matrix))

tuples = (
	(0),
	(2, 4 ),
	(0, 5, 6 ),
	(7, 2, 9, 10 ),
	(25, 11, 1, 0, 5 ),
	(1, 88, 51, 88, 61, 4 ),
	(93, 12, 73, 36, 71, 65, 34 ),
	(233, 5, 2, 1, 6, 7, 55, 1 ),
	(16, 111, 213, 9, 23, 433, 1, 34, 13 ),
	(5, 23, 453, 789, 123, 200, 212, 345, 556, 99 )
)

matrix = []
for i in tuples:
	matrix.append(tupleToList(i))

print(bestPath(matrix))