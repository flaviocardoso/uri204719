#include <iostream>

using namespace std;

int main(){
	
	double a, b, c, media;
	
	cin >> a;
	cin >> b;
	cin >> c;
	
	std::cout.precision(1);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	media = (a * 0.2 + b * 0.3 + c * 0.5);
	
	cout << "MEDIA = " << media << endl;
	
	return 0;
}
