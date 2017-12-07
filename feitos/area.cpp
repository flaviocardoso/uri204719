#include <iostream>
#include <math.h>

using namespace std;

int main(){
	
	double a, b, c, pi = 3.14159, areaT, areaC, areaTP, areaQ, areaR;
	
	cin >> a >> b >> c;
	
	std::cout.precision(3);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	areaT = (a * c) / 2;
	areaC = pi * pow(c, 2);
	areaTP = (a + b) * c / 2;
	areaQ = b * b;
	areaR = a * b;
	
	cout << "TRIANGULO: " << areaT << endl;
	cout << "CIRCULO: " << areaC << endl;
    	cout << "TRAPEZIO: " << areaTP << endl;
	cout << "QUADRADO: " << areaQ << endl;
	cout << "RETANGULO: " << areaR << endl;
	
	return 0;
}
