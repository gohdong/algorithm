import java.util.*;

class Main{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		int i,j;
		int a = s.nextInt();

		for(i=a;i>0;i--){
			for(j=0;j<i;j++){
				System.out.print("*");
			}
			System.out.println();
		}
	}
}