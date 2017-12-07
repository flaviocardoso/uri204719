#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){
	double PI = 3.14159;
	double area, r;
	
	cin >> r;	
	
	area = r * r * PI;
	
	std::cout.precision(4);	
	
	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
	
	cout << "A=" << area << endl;
	
	return 0;
}
