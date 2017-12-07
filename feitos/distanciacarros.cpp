#include <iostream>
#include <math.h>

using namespace std;

int main(){
	
	int d;
	double tempo,velc1 = 60, velc2 = 90;
	
	cin >> d;
	
	tempo = d / (velc2 - velc1);
	
	cout << (tempo * 60) << " minutos" << endl;
	return 0;
}
