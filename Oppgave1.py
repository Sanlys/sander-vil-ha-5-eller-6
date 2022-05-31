def bestPath(matrix):
	xlen = len(matrix)    # row
	ylen = len(matrix[0]) # column

	for x in range(0, xlen):
		for y in range(0, ylen):
			if y == 0 and x == 0:
				continue
			elif x == 0:
				matrix[x][y] += matrix[x][y-1]
			elif y == 0:
				matrix[x][y] += matrix[x-1][y]
			else:
				if matrix[x-1][y] < matrix[x][y-1]:
					matrix[x][y] += matrix[x-1][y]
				else:
					matrix[x][y] += matrix[x][y-1]
	return matrix[ylen-1][xlen-1]

def inverse(matrix):
	xlen = len(matrix[0])
	ylen = len(matrix)

	for x in range(0, xlen):
		for y in range(0, ylen):
			matrix[x][y] = -1*matrix[x][y]
	return matrix

def worstPath(matrix):
	return -1*bestPath(inverse(matrix))

array1 = [
	[ 1, 8, 921, 238, 366, 938, 246, 940, 736, 585 ] ,
	[ 36, 9, 161, 717, 224, 489, 141, 160, 496, 838 ] ,
	[ 389, 22, 766, 19, 498, 655, 727, 130, 279, 392 ] ,
	[ 667, 220, 1, 581, 468, 96, 495, 169, 134, 14 ] ,
	[ 279, 30, 786, 780, 306, 533, 498, 637, 344, 599 ] ,
	[ 896, 224, 521, 948, 467, 208, 791, 371, 739, 48 ] ,
	[ 505, 592, 465, 586, 714, 540, 758, 488, 130, 609 ] ,
	[ 190, 851, 153, 433, 644, 444, 441, 401, 666, 118 ] ,
	[ 432, 662, 497, 926, 646, 686, 722, 196, 60, 854 ] ,
	[ 494, 818, 815, 355, 63, 778, 914, 812, 900, 999 ]
]

print(worstPath(array1))