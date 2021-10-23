import java.util.*;
import java.io.*;

public class Main {
    static int numOfCourses;
    static long curLength;
    static int[] ranges;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_18311_왕복\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfCourses = Integer.parseInt(st.nextToken());
        curLength = Long.parseLong(st.nextToken());

        long lengthOfTrack = 0;
        ranges = new int[numOfCourses];
        st = new StringTokenizer(br.readLine());
        for (int idx = 0; idx < numOfCourses; idx++) {
            int curValue = Integer.parseInt(st.nextToken());
            ranges[idx] = curValue;
            lengthOfTrack += curValue;
        }

        long[][] courseRanges = new long[numOfCourses][2];
        courseRanges[0][0] = 0;
        courseRanges[0][1] = ranges[0];

        for (int idx = 1; idx < numOfCourses; idx++) {
            courseRanges[idx][0] = courseRanges[idx - 1][1];
            courseRanges[idx][1] = courseRanges[idx - 1][1] + ranges[idx];
        }

        if (lengthOfTrack < curLength) {
            long diff = Math.abs(curLength - lengthOfTrack);
            curLength = lengthOfTrack - diff;
        }

        for (int idx = 0; idx < numOfCourses; idx++) {
            long start = courseRanges[idx][0];
            long end = courseRanges[idx][1];

            if (idx == numOfCourses - 1) {
                if (start <= curLength && curLength <= end) {
                    System.out.println(idx + 1);
                    return;
                }
            } else {
                if (start <= curLength && curLength < end) {
                    System.out.println(idx + 1);
                    return;
                }
            }
        }
    }
}