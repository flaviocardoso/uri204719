#include <iostream>
#include <cmath>

using namespace std;

int main(){
	double x1, x2, x, y1, y2, y, dis;
	
	cin >> x1 >> y1;
	cin >> x2 >> y2;
	
	std::cout.precision(4);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	x = pow((x2 - x1), 2);
	y = pow((y2 - y1), 2);
	
	dis = sqrt(x + y);	
	
	cout << dis << endl;
	return 0;
}

