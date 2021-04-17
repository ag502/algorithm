import java.util.*;
        import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int year = Integer.parseInt(br.readLine());

        if (year % 4 == 0 && year % 100 != 0) {
            System.out.println(1);
            return;
        }
        if (year % 400 == 0) {
            System.out.println(1);
            return;
        }
        System.out.println(0);
    }
}
