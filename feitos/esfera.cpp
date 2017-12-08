#include <iostream>
#include <math.h>

using namespace std;

int main(){
	double pi = 3.14159, r, vol;
	
	cin >> r;
	
	std::cout.precision(3);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	vol = (4.0/3) * pi * pow(r, 3);
	
	cout << "VOLUME = " << vol << endl;	
	
	return 0;
}
