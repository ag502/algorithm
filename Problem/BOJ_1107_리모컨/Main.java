import java.util.*;
import java.io.*;

public class Main {
    static int targetChannel, lengthOfChannel, numOfBrokenBtns;
    static Set<Integer> buttons;
    static StringBuilder sb;
    static int answer;
    static boolean isPushNumber = false;
    static int minDiff = Integer.MAX_VALUE;

    public static void getChannel(int curButton, int targetLength) {
        sb.append(curButton);

        if (sb.length() < targetLength) {
            for (int button : buttons) {
                getChannel(button, targetLength);
            }
        }

        if (sb.length() == targetLength) {
            int curNumber = Integer.parseInt(sb.toString());
            int curDiff = Math.abs(targetChannel - curNumber);
            answer = Math.min(answer, curDiff + Integer.toString(curNumber).length());
        }
        sb.deleteCharAt(sb.length() - 1);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1107_리모컨\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        String channel = br.readLine();
        lengthOfChannel = channel.length();
        targetChannel = Integer.parseInt(channel);
        numOfBrokenBtns = Integer.parseInt(br.readLine());

        // 버튼 초기화
        buttons = new HashSet<>();
        for (int button = 0; button < 10; button++) {
            buttons.add(button);
        }
        // 고장난 버튼 제거
        if (numOfBrokenBtns != 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < numOfBrokenBtns; i++) {
                buttons.remove(Integer.parseInt(st.nextToken()));
            }
        }

        // 목표 채널이 100일때
        if (targetChannel == 100) {
            System.out.println(0);
            return;
        }

        answer = Math.abs(targetChannel - 100);
        // 목표채널과 가장 가까운 채널 구하기
        for (int length = 1; length <= 6; length++) {
            sb = new StringBuilder("");
            for (int button : buttons) {
                getChannel(button, length);

            }
        }

        System.out.println(answer);
    }
}