#include <iostream>

using namespace std;

int fat(int n){
	int f;
	for(f = 1; n > 1; --n){
		f = f * n;
	}
	
	return f;	
}

int main(){
	/*int a, b, sum;
	
	cin >> a >> b;
	sum = a + b;
	
	cout << "X = " << sum << endl;*/
	
	int k = 0;
	long int NP = 100000;
	int i = 1;
	int N;
	
	cin >> N;
	
	//cout << fat(n);
	
	if (N > 0){
		while((N <= NP) && (N >= 1)){
			//cout << "Fatorial(" << i << ") = " <<  fat(i) << endl;
			if(fat(i) > N){
				N = N - fat(--i);
				cout << "N restantes " << N << endl;
				cout << "FAT(" << i << ")" << " = " << fat(i) << endl;
				k = k + 1;
				i = 1;	
			}else{
				i = i + 1;
			}		
			//i = i + 1;	
			//NP = NP - 1;
		}
	}else{
		k = 1;
	}
	
	
	
	cout << k << endl;
	
	return 0;
}


