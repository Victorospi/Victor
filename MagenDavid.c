/*
 * MagenDaviv.c
 *
 *  Created on: Nov 28, 2023
 *      Author: Osipov
 */
#include <stdio.h>
void printMagenDavid();
int main(){
	printMagenDavid();
	return 0;
}
void printMagenDavid()
{
	int x, y, hight = 20;
	int temp = -hight/3-1;
	int forFinalTRG = hight/3;
	for(x = 0; x < hight; x++)
		{
			for(y = 0; y < hight*2-1; y++)
			{
				if(x==hight-1||(x+y>=hight-1&&y-x<hight))printf("*");
				else if(x>=hight/3&&y>temp&&y<(hight*2-1)-temp-1)printf("*");
				else printf(" ");
			}
			temp++;
			printf("\n");
		}
	int i,j;
	int temptwo = forFinalTRG;
	for(i=0; i<forFinalTRG; i++)
	{
		for(j=0; j<hight*2-1; j++)
		{
			if(j>hight-temptwo&&j<hight+temptwo)
			{
				printf("*");
			}
			else printf(" ");
		}
		printf("\n");
		temptwo--;
	}
}