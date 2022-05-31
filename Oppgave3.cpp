#include <iostream>
#include <stdbool.h>
#include <vector>
#include <algorithm>

bool validateMaze(int maze[10][10]) {
  
        //Bruker en vector av vectorer av integers. Dette var den letteste og mest brukbare måten å lage en nested liste med integers.
        //Vector er datatypen jeg hadde mest suksess med, de andre som f.eks. list og array hadde noen store problemer som ville blitt unødvendig komplisert å løst for hånd, når det finnes en bedre datatype.
  
        //Denne seen variabelen inneholder alle felter vi har sjekket, disse blir ignorert av loopen under. Dette er da en liste med alle elementer vi er ferdige med.
	std::vector<std::vector<int>> seen;

        //Dette er en liste med alle ruter som algoritmen under har funnet. Når den finner en ny, om den ikke er allerede i seen listen (blant annet krav) blir den lagt til her. Vi setter den by default til {0, 0}, så while loopen under starter øverst til venstre.
	std::vector<std::vector<int>> queue = {{0,0}};

        //While loopen kjører helt til queue sizen er tom. Da vil vi ha sjekket alle rutene vi klarte å nå. Om vi har en evig loop som kjører til den finner mål, vil den henge seg opp for alltid om den ikke finner mål, altså om mazen er ugyldig.
	while (queue.size() > 0 ) {
                //Her setter vi en current variabel. Denne blir overskrevet hver gang loopen kjører, og den inneholder koordinatene vi skal teste fra. Dette kan også sees på som hvor vi er i mazen. Vi setter den til 0 i queuen, altså den første
		std::vector<int> current = queue[0];
                //Her fjerner vi det første elementet. Dette og linjen over blir det samme som en list.pop() funksjon i python. Vi vil da fjerne elementet vi satt som main, siden den blir vi ferdig med nedover.
		queue.erase(queue.begin());
                
                //Vi setter x og y til hver sin index fra current variabelen. Dette er ikke nødvendig, men gjør det lettere å lese nedover
		int x = current[0];
		int y = current[1];

                //her har jeg hardcoda lengden, men dette kan også bli evaluert automatisk.
		int xlen = 10;
		int ylen = 10;
                //Her setter vi målet. Dette gjør jeg bare for å slippe å definere flere ganger under i for loopen.
		std::vector<int> goal = {xlen-1, ylen-1};
                
                //Her legger vi den vi kommer til å gå over i seen listen. Dette vil gjøre at den ikke blir evaluert flere ganger.
		seen.push_back({x,y});

                //Her definerer jeg en liste over alle mulige felter vi kan nå fra current
		std::vector<std::vector<int>> directions = {{x+1, y}, {x-1, y}, {x, y+1}, {x, y-1}};
                
                //Denne loopen looper over alle mulige directions. Den evaluerer alle hver for seg, en per loop.
		for (auto testPosition: directions) {
                        //Om posisjonen den nå evaluerer, en av directions, er på samme posisjon som målet/goal variabelen, return true. Om den kommer hit, er det garantert at mazen er løsbar, siden vi nettop fant en løsning.
			if (testPosition == goal) {
				return true;
			}
                        //Dette er en litt krunglete måte å gjøre det på, men koden under tester om variabelen testPosition er på noen plass i listen seen. Om den er dette, skal vi ignorere den, som beskrevet over der jeg definerte seen variabelen.
			else if (std::find(seen.begin(), seen.end(), testPosition) != seen.end()) {
				continue;
			}
                        //Her tester vi om plassen er utenfor mazen. Dette vil oppstå om plassen er høyere enn makslengden på mazen, så i dette tilfellet xlen og ylen. Vi må fjerne 1, siden indexer for vectorer i c++ starter på 0, ikke 1. Dette kan også oppstå om den er lavere enn 0, da er den utenfor mazen på motsatt side.
			else if (testPosition[0] < 0 || testPosition[1] < 0 || testPosition[0] > xlen-1 || testPosition[1] > ylen-1) {
				continue;
			}
                        //Hvis ingen av kravene over er oppfylt, tar vi en siste test. Her ser vi om verdien på koordinatene vi tester er lik 1. Om den er det, er dette et felt vi kan gå til. Da er dette et gyldig felt, så vi legger koordinatene til i queuen. Denne blir lagt til i slutten, så når vi endelig kommer dit, vil vi teste alle plassene rundt dette koordinatet.
			else if (maze[testPosition[0]][testPosition[1]] == 1) {
				queue.push_back(testPosition);
			}
		}
	}
        //Om vi aldri kom til return true, som bare kan oppstå når vi finner mål, og alle koordinatene i queuen er prøvd, returnerer vi false. Dette betyr at mazen ikke er valid.
	return false;
}

int main(){
        //Maze som skal valideres
	int maze[10][10] = {
		{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
		{1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
		{1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
		{0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
		{1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
		{1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
		{1, 0, 1, 0, 0, 0, 0, 0, 0, 1 },
		{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
		{1, 1, 0, 0, 0, 1, 1, 1, 0, 1 }
	};
        //Kaller funksjonen validateMaze med mazen over. Skriver også ut en ny linje for at det skal være lettere å se.
	std::cout << validateMaze(maze) << "\n";
	return 0;
}
