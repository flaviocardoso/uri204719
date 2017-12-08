#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

main(){
	int i = 0;
	char resp[100];
	char nome[] = "FLAVIO";
	
	
	do
	{
		scanf("%s", resp);		
		strcpy(resp, strupr(resp));
		//printf("%s", resp);
	}
	while(strcmp(resp, nome) != 0);	

	
	
	printf("Teste run ok");
	
	return 0;
}
