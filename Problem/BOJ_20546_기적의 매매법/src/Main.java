import java.util.*;
import java.io.*;

public class Main {
    // 준현
    static int[] person1 = new int[2];
    // 성민
    static int[] person2 = new int[2];
    static int[] stocks = new int[14];
    static StringTokenizer st;
    public static void main(String[] args) throws IOException{
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int curMoney = Integer.parseInt(br.readLine());
        person1[0] = curMoney;
        person2[0] = curMoney;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < stocks.length; i++) {
            stocks[i]= Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < stocks.length; i++) {
            if (person1[0] >= stocks[i]) {
                int curAvailable = person1[0] / stocks[i];
                person1[0] -= stocks[i] * curAvailable;
                person1[1] += curAvailable;
            }
        }

        boolean isBuy = false;
        boolean isSell = false;
        for (int i = 2; i < stocks.length; i++) {
            if (isBuy) {
                if (person2[0] >= stocks[i]) {
                    int curAvailable = person2[0] / stocks[i];
//                    System.out.println(stocks[i - 2] + " " + stocks[i - 1] + " " + stocks[i]);
//                    System.out.println(i + " " + curAvailable);
                    person2[0] -= stocks[i] * curAvailable;
                    person2[1] += curAvailable;
                }
            }
            if (isSell) {
                if (person2[1] != 0) {
                    person2[0] += person2[1] * stocks[i];
                    person2[1] = 0;
                }
            }
            if (stocks[i - 2] > stocks[i - 1] && stocks[i - 1] > stocks[i]) {
                isBuy = true;
            } else {
                isBuy = false;
            }
            if (stocks[i - 2] < stocks[i - 1] && stocks[i - 1] < stocks[i]) {
                isSell = true;
            } else {
                isSell = false;
            }
        }

        int person1Money = person1[0] + stocks[13] * person1[1];
        int person2Money = person2[0] + stocks[13] * person2[1];

        if (person1Money < person2Money) {
            System.out.println("TIMING");
        } else if (person1Money > person2Money) {
            System.out.println("BNP");
        } else {
            System.out.println("SAMESAME");
        }
    }
}
