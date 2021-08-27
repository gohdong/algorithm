import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        long a = s.nextInt();
        long b = s.nextInt();
        long c = s.nextInt();
        long total=a;

        for (int i =0;;i++  ) {
            if(b>=c){
                System.out.println(-1);
                break;
            }
            if(total < c*i ){
                System.out.println(i);
                break;
            }
            total +=b;
        }

    }
}

