#include <iostream>

using namespace std;

int main(){
	int dis;
	double com, cm;
	
	cin >> dis;
	cin >> com;
	
	std::cout.precision(3);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	cm = dis / com;
	
	cout << cm << " km/l" << endl;
}
