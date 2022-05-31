def bestPath(matrix):
    #Henter ut x og y lengden på matrisen og lagrer dem. Dette er ikke nødvendig men gjør koden mer oversiktelig
    xlen = len(matrix)    # row
	ylen = len(matrix[0]) # column

    #Her looper vi gjennom arrayen, først på x aksen, også på y aksen. 2 nested for loops på denne måten gjør at vi går igjennom alle elementene i 2D arrayen.
	for x in range(0, xlen):
		for y in range(0, ylen):
            #Om vi er på y 0 og x 0 vil vi hoppe over dette elementet.
			if y == 0 and x == 0:
				continue
            #Her sjekker vi om x er 0. Dette betyr at vi er helt inntil kanten på matrixen. Om vi er det, har vi ikke noe valg, så vi velger den eneste vi kan nå, som er på koordinatet x, y-1. Dette vil si at det er på samme x akse som elementet valgt av loopen, men den er 1 y verdi mindre.
			elif x == 0:
				matrix[x][y] += matrix[x][y-1]
            #Her sjekker vi motsatt, om den er intill y-veggen, legger vi til den som er mot x.
			elif y == 0:
				matrix[x][y] += matrix[x-1][y]
            #Om vi faktisk har noen valg som ikke bryter reglene, vil vi velge det laveste. Om verdien på koordinatet x-1, y er lavest, velger vi den. Om ikke, betyr det at x, y-1 er enten lavere eller den samme verdien, og da velger vi bare den.
			else:
				if matrix[x-1][y] < matrix[x][y-1]:
					matrix[x][y] += matrix[x-1][y]
				else:
					matrix[x][y] += matrix[x][y-1]
    #Etter vi er ferdig med hele loopen, vil verdien av det siste elementet, altså nederst i høyre hjørne være summen vår. Denne returnerer vi.
	return matrix[ylen-1][xlen-1]

#Inverse funksjonen reverserer alle verdiene ved å gange de med -1. Dette vil da si at de største tallene blir de minste, og de minste tallene blir de største.
def inverse(matrix):
	xlen = len(matrix[0])
	ylen = len(matrix)

	for x in range(0, xlen):
		for y in range(0, ylen):
			matrix[x][y] = -1*matrix[x][y]
	return matrix

#For å finne den værste pathen benytter vi oss egentlig bare av funksjonen for best path. bestPath fungerer ved at den alltid velger det laveste tallet når den har et valg. Vi kan da reversere hva slags tall er de laveste og høyeste, ved inverse funksjonen. Når vi kjører bestPath funksjonen på denne motsatte matrixen, vil vi få det laveste tallet. Det eneste vi trenger å gjøre da er å reversere det vi fikk ut, som mest sannsynelig er et negativt tall (Om vi regner med at alle tall i matrixen originalt var positive) som vi da kan gange med -1 igjen. Dette vil reversere tallet på nytt og vi vil få ett positivt tall. Dette er summen av den "værste" pathen, altså den med høyest kostnad. Når vi kjører bestPath funksjonen på denne motsatte matrixen, vil vi få det laveste tallet. Det eneste vi trenger å gjøre da er å reversere det vi fikk ut, som mest sannsynelig er et negativt tall (Om vi regner med at alle tall i matrixen originalt var positive) som vi da kan gange med -1 igjen. Dette vil reversere tallet på nytt og vi vil få ett positivt tall. Dette er summen av den "værste" pathen, altså den med høyest kostnad. 
def worstPath(matrix):
	return -1*bestPath(inverse(matrix))

#Array som testes
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

#Kaller funksjon for å finne best path
print(bestPath(array1))
