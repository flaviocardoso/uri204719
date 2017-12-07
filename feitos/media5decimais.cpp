#include <iostream>

using namespace std;

int main(){
	
	double a, b, media;
	
	cin >> a;
	cin >> b;
	
	std::cout.precision(5);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	media = ((3.5/11) * a) + (b * (7.5/11));
	
	cout << "MEDIA = " << media << endl;
	
	return 0;	
}

// 5.0 7.1 MEDIA = 6.43182
// 0.0 7.1 MEDIA = 4.84091
// 10.0 10.0 MEDIA = 10.00000
