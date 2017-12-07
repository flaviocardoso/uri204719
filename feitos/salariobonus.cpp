#include <iostream>
#include <string>

using namespace std;

int main(){
	string nome;
	double SF, VE, TM;
	
	cin >> nome;
	cin >> SF;
	cin >> VE;
	
	std::cout.precision(2);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	TM = SF + VE * 0.15;
	
	cout << "TOTAL = R$ " << TM << endl; 
	
	return 0;
}
