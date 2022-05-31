#include <iostream>
#include <stdbool.h>
#include <vector>
#include <algorithm>

bool validateMaze(int maze[10][10]) {
	/*for(int i = 0; i<10; i++) {
		for(int j = 0; j<10; j++) {
			std::cout << maze[i][j];
		}
		std::cout << "\n";
	}*/

	std::vector<std::vector<int>> seen;
	std::vector<std::vector<int>> queue = {{0,0}};

	while (queue.size() > 0 ) {
		//std::cout << queue.size() << " line 18\n";

		std::vector<int> current = queue[0];
		queue.erase(queue.begin());
		//std::cout << queue.size() << " line 22\n";
		//std::cout << current[0] << " line 23 \n";
		//std::cout << current[1] << " line 24 \n";

		int x = current[0];
		int y = current[1];

		int xlen = 10;
		int ylen = 10;
		std::vector<int> goal = {xlen-1, ylen-1};

		seen.push_back({x,y});

		std::vector<std::vector<int>> directions = {{x+1, y}, {x-1, y}, {x, y+1}, {x, y-1}};

		for (auto testPosition: directions) {
			//std::cout << testPosition[0] << testPosition[1] << " testPosition\n";
			//std::cout << "for loop started/restarted\n";
			//std::cout << seen.size() << " Seen list\n";
			//std::cout << testPosition[0] << testPosition [1] << " Position\n";
			if (testPosition == goal) {
				//std::cout << "goal reached\n";
				return true;
			}
			else if (std::find(seen.begin(), seen.end(), testPosition) != seen.end()) {
				//std::cout << "Den retard if statementen funka faktisk" << "\n";
				//std::cout << "continue called line 45\n";
				continue;
			}
			else if (testPosition[0] < 0 || testPosition[1] < 0 || testPosition[0] > xlen-1 || testPosition[1] > ylen-1) {
				//std::cout << "continue called line 49\n";
				//std::cout << testPosition[0] << testPosition [1] << "\n";
				continue;
			}
			else if (maze[testPosition[0]][testPosition[1]] == 1) {
				//std::cout << queue.size() << " line 43\n";
				queue.push_back(testPosition);
				//std::cout << queue.size() << " line 55\n";
			}
		}
	}
	return false;
}

int main(){
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

	std::cout << validateMaze(maze) << "\n";
	return 0;
}