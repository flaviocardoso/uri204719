#include <iostream>

using namespace std;

int main(){
	int cp1, np1, cp2, np2;
	double vu1, vu2, valor;
	
	cin >> cp1 >> np1 >> vu1;
	cin >> cp2 >> np2 >> vu2;
	
	std::cout.precision(2);
	std:cout.setf(std::ios::fixed, std::ios::floatfield);
	
	valor = (np1 * vu1) + (np2 * vu2);
	
	cout << "VALOR A PAGAR: R$ " << valor << endl;
	
	return 0;
}
