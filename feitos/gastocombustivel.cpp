#include <iostream>

using namespace std;

int main(){
	int tempo, v_media, dis;
	double litro, dis_litro = 12.0;
	
	cin >> tempo;
	cin >> v_media;
	
	dis = tempo * v_media;
	
	std::cout.precision(3);
	std::cout.setf(std::ios::fixed, std::ios::floatfield);
	
	litro = dis / dis_litro;	
	
	cout << litro << endl;
	
	return 0;
}
