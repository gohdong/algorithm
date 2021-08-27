import java.util.*;

class Main{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		int i,j;
		int a = s.nextInt();

		for(i=0;i<a;i++){
			for(j=0;j<(a-i-1);j++){
				System.out.print(" ");
			}
			for(j=0;j<i+1;j++){
				System.out.print("*");
			}
			System.out.println();
		}
	}
}