/*
 * star_tree.jav
 * Created on: Nov 28, 2023
 * Author: Osipov
 */

public class Main {
	public static void main(String[] args) {
void printTriangle(int hight=7){
 int x, y;
 for(x = 0; x < hight; x++){
	for(y = 0; y < hight*2-1; y++){
	   if(x==hight-1||x+y==hight-1||y-x==hight-1)
	     System.out.println("*");
	   else
		 System.out.println(" ");
	}
	System.out.println("\n");
 }
}
}
}