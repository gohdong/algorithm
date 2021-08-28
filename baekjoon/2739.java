import java.util.*;

class Main{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		int i;
		int a = s.nextInt();

		for(i=1;i<=9;i++){
			System.out.printf("%d * %d = %d\n",a,i,a*i);
		}
	}
}