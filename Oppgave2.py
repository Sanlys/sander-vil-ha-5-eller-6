#Dette er fordi jeg ikke har noe lyst til å bruke tuples, jeg syntes lister er bedre å jobbe med. Grunnen til try except blokken er fordi list() ikke vil ta inn enkelte verdier. en tuple med kun en verdi vil returnere kun ett tall. f.eks. (5) = 5. Å kjøre list(5) vil ikke fungere fordi den forventer flere verdier. Derfor har jeg en edgecase for dette, som vil returnere verdien i en array. Dette er så bestPath koden ikke gjør noe rart når vi prøver å nå f.eks. 5[0], som da ikke fungerer.
def tupleToList(tuple):
	try:
		return list(tuple)
	except:
		return [tuple]

def bestPath(matrix):
    #Vi setter row til lengden av matrisen. Vi trenger ikke vite columns.
	rows = len(matrix)
    #Her looper vi gjennom alle rows.
	for row in range(0, rows):
        #Siden hver row øker med 1, kan vi bare sette lengden på columns til å være row+1.
		for column in range(0,row+1):
            #Om den har lengde på 0, er vi på første row. Her kan vi ikke gjøre noe, siden det er ingen verdier over.
			if row == 0:
				continue
            #Her ser vi om det bare er ett alternativ. Om det er det, velger vi dette alternativet.
			elif row == 1 and column == 0:
				matrix[row][column] += matrix[0][0]
            #Her oppdaterer vi feltet i matrisen spesifisert på row og column variabelen. Den plusser på den minste av den som er over, enten den rett over eller den over og til siden.
			elif column == 0:
				matrix[row][column] += min(matrix[row-1][column], matrix[row-1][column+1])
            #Om tallet er ytterst, vil vi legge til det eneste vi kan nå herfra. Det vil da bli en over og en column til siden
			elif column == len(matrix[row])-1:
				matrix[row][column] += matrix[row-1][column-1]
            #Her gjør vi det samme som over, men ser om den er nest ytters. Om den er det, velger vi den laveste av de to vi kan nå.
            elif column == len(matrix[row])-2:
				matrix[row][column] += min(matrix[row-1][column-1], matrix[row-1][column])
            #Om vi har muligheten til å velge mellom 3 verdier, velger vi da den laveste.
            else:
				matrix[row][column] += min(matrix[row-1][column-1], matrix[row-1][column], matrix[row-1][column+1])
	return min(matrix[-1])

#Her har jeg samme ide som Oppgave 1,
def inverse(matrix):
	for i in matrix:
		for j in i:
			matrix[i][j] = -1*matrix[i][j]
	return matrix

#Her gjør jeg nøyaktig det samme som i Oppgave 1
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

#Dette er for å lage matrisen
matrix = []
for i in tuples:
	matrix.append(tupleToList(i))

#Kaller bestPath med matrisen vi lagde, og printer resultatet for å se lavest mulig valg
print(bestPath(matrix))
