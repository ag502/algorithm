import java.util.*;
import java.io.*;

public class Main {
    static int numOfWords;

    public static boolean isSlumps(String str) {
        if (str.length() == 0) {
            return false;
        }
        if (str.charAt(0) != 'D' && str.charAt(0) != 'E') {
            return false;
        }
        if (str.charAt(1) != 'F') {
            return false;
        }

        int curIdx = -1;
        for (int i = 2; i < str.length(); i++) {
            if (str.charAt(i) != 'F') {
                curIdx = i;
                break;
            }
        }
        if (curIdx == -1) {
            return false;
        }

        if (curIdx == str.length() - 1 && str.charAt(curIdx) == 'G') {
            return true;
        } else {
            return isSlumps(str.substring(curIdx));
        }
    }

    public static boolean isSlimps(String str) {
        // 길이가 2 미만일때
        if (str.length() < 2) {
            return false;
        }
        // A로 시작하지 않으면 false
        if (str.charAt(0) != 'A') {
            return false;
        }
        // 길이가 2일 경우
        if (str.length() == 2) {
            return str.charAt(0) == 'A' && str.charAt(1) == 'H';
        } else {
            // C로 끝나지 않는 경우
            if (str.charAt(str.length() - 1) != 'C') {
                return false;
            } else {
                // AB로 시작하는 경우
                int abIdx = str.indexOf("AB");
                if (abIdx == 0) {
                    return isSlimps(str.substring(2, str.length() - 1));
                }
                // A로 시작하는 경우
                int aIdx = str.indexOf("A");
                if (aIdx == 0) {
                    return isSlumps(str.substring(1, str.length() - 1));
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14906_스러피\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfWords = Integer.parseInt(br.readLine());

        boolean isFind;
        System.out.println("SLURPYS OUTPUT");
        for (int i = 0; i < numOfWords; i++) {
            isFind = false;
            String originalStr = br.readLine();

            if (originalStr.charAt(0) != 'A') {
                System.out.println("NO");
                continue;
            }

            // H로 쪼개기
            int hIdx = originalStr.indexOf("H");
            while (hIdx != -1) {
                String slimp = originalStr.substring(0, hIdx + 1);
                String slump = originalStr.substring(hIdx + 1);

                if (isSlimps(slimp) && isSlumps(slump)) {
                    System.out.println("YES");
                    isFind = true;
                    break;
                }

                hIdx = originalStr.indexOf("H", hIdx + 1);
            }

            if (isFind) {
                continue;
            }

            // C로 쪼개기
            int cIdx = originalStr.indexOf("C");
            while (cIdx != -1) {
                String slimp = originalStr.substring(0, cIdx + 1);
                String slump = originalStr.substring(cIdx + 1);

                if (isSlimps(slimp) && isSlumps(slump)) {
                    System.out.println("YES");
                    isFind = true;
                    break;
                }

                cIdx = originalStr.indexOf("C", cIdx + 1);
            }

            if (!isFind) {
                System.out.println("NO");
            }
        }
        System.out.println("END OF OUTPUT");
    }
}