import java.util.*;
import java.io.*;

public class Main {
    static String shortenedAddr;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_3107_IPv6\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        shortenedAddr = br.readLine();

        // 그룹의 숫자가 1개 이상 3개 이하인 경우 0 붙이기
        String[] parseBySingleSemi = shortenedAddr.split(":", -1);
        StringBuilder sb = new StringBuilder("");

        int lengthOfAddr = 0;
        for (int i = 0; i < parseBySingleSemi.length; i++) {
            String addrGroup = parseBySingleSemi[i];
            int curGroupSize = addrGroup.length();
            lengthOfAddr += curGroupSize;

            if (curGroupSize >= 1 && curGroupSize <= 3) {
                sb.setLength(0);
                // 0 붙이기
                for (int count = 1; count <= 4 - curGroupSize; count++) {
                    sb.append("0");
                    lengthOfAddr += 1;
                }
                parseBySingleSemi[i] = sb.append(addrGroup).toString();
            }
        }

        shortenedAddr = String.join(":", parseBySingleSemi);

        // 길이가 32 미만일 경우 :: 찾기
        if (lengthOfAddr < 32) {
            int idx = shortenedAddr.indexOf("::");
            if (idx != -1) {
                String leftAddr = null;
                String rightAddr = null;

                // :: 찾았을 경우 ::을 기준으로 나누기
                if (idx == 0) {
                    leftAddr = "";
                    rightAddr = shortenedAddr.substring(idx + 2);
                } else if (idx == shortenedAddr.length() - 2) {
                    leftAddr = shortenedAddr.substring(0, idx);
                    rightAddr = "";
                } else {
                    leftAddr = shortenedAddr.substring(0, idx);
                    rightAddr = shortenedAddr.substring(idx + 2);
                }

                // 필요한 갯수 만큼 0000 추가
                int zeroAppendTime = (32 - lengthOfAddr) / 4;
                List<String> zeroGroup = new ArrayList<>();
                for (int count = 1; count <= zeroAppendTime; count++) {
                    zeroGroup.add("0000");
                    lengthOfAddr += 4;
                }

                shortenedAddr = (leftAddr.equals("") ? leftAddr : leftAddr + ":") + String.join(":", zeroGroup)
                        + (rightAddr.equals("") ? rightAddr : ":" + rightAddr);
            }

        }

        // 나머지 부분 0추가
        parseBySingleSemi = shortenedAddr.split(":");
        if (lengthOfAddr < 32) {
            for (int idx = 0; idx < parseBySingleSemi.length; idx++) {
                if (parseBySingleSemi[idx].length() == 0) {
                    parseBySingleSemi[idx] = "0000";
                }
            }
        }

        shortenedAddr = String.join(":", parseBySingleSemi);

        System.out.println(shortenedAddr);
    }
}