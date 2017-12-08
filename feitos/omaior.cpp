#include <iostream>

using namespace std;

int main(){
	int a, b, c, omaior;
	
	cin >> a >> b >> c;
	
	if(a > b){
		if(a > c){
			omaior = a;
		}else{
			omaior = c;
		}
	}else{
		if(b > c){
			omaior = b;
		}else{
			omaior = c;
		}
	}	
	
	
	
	cout << omaior << " eh o maior" << endl;
	
	return 0;
}
