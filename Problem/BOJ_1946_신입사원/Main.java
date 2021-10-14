import java.util.*;
import java.io.*;

class Interviewer {
    int first;
    int second;

    public Interviewer(int first, int second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public String toString() {
        return first + " // " + second;
    }
}

public class Main {
    static int numOfInterviewers;
    static Interviewer[] interviewerInfo;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1946_신입사원\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        int testCase = Integer.parseInt(br.readLine());
        for (int test = 0; test < testCase; test++) {
            numOfInterviewers = Integer.parseInt(br.readLine());
            interviewerInfo = new Interviewer[numOfInterviewers];

            // 1차 2차 면접 점수 입력
            for (int person = 0; person < numOfInterviewers; person++) {
                st = new StringTokenizer(br.readLine());
                int first = Integer.parseInt(st.nextToken());
                int second = Integer.parseInt(st.nextToken());
                interviewerInfo[person] = new Interviewer(first, second);
            }

            // 1차 순위 정렬
            Arrays.sort(interviewerInfo, (a, b) -> b.first - a.first);

            // 뽑는 인원 count
            int answer = 1;
            int secondMinScore = interviewerInfo[numOfInterviewers - 1].second;
            for (int i = numOfInterviewers - 2; i >= 0; i--) {
                if (interviewerInfo[i].second < secondMinScore) {
                    secondMinScore = interviewerInfo[i].second;
                    answer += 1;
                }
            }

            System.out.println(answer);
        }
    }
}