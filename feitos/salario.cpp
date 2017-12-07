#include <iostream>

using namespace std;

int main(){
	
	int N, H;
	double VH, S;
	
	cin >> N;
	cin >> H;
	cin >> VH;
	
	cout << "NUMBER = " << N << endl;
	
	std::cout.precision(2);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	S = H * VH;
	
	cout << "SALARY = U$ " << S << endl;	
	
	return 0;
}
