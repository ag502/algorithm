import java.util.*;
import java.io.*;

public class Main {
    static int numOfStudents;
    static int numOfCompares;

    static Map<Integer, List<Integer>> heightRels;
    static int[] indegree;
    static StringBuilder sb = new StringBuilder("");

    static StringTokenizer st;

    public static void topologicalSort() {
        Queue<Integer> queue = new LinkedList<>();

        for (int student = 1; student <= numOfStudents; student++) {
            if (indegree[student] == 0) {
                queue.offer(student);
            }
        }

        while (!queue.isEmpty()) {
            int curStudent = queue.poll();
            sb.append(curStudent).append(" ");

            for (int nextStudent : heightRels.get(curStudent)) {
                indegree[nextStudent]--;

                if (indegree[nextStudent] == 0) {
                    queue.offer(nextStudent);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_2252_줄 세우기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfStudents = Integer.parseInt(st.nextToken());
        numOfCompares = Integer.parseInt(st.nextToken());

        // 키관계 초기화
        heightRels = new HashMap<>();
        for (int student = 1; student <= numOfStudents; student++) {
            heightRels.put(student, new ArrayList<>());
        }

        // 그래프 간선 추가
        indegree = new int[numOfStudents + 1];
        for (int i = 0; i < numOfCompares; i++) {
            st = new StringTokenizer(br.readLine());
            int tallStudent = Integer.parseInt(st.nextToken());
            int shortStudent = Integer.parseInt(st.nextToken());

            heightRels.computeIfPresent(tallStudent, (k, v) -> {
                v.add(shortStudent);
                indegree[shortStudent]++;
                return v;
            });
        }

        // 키순서 배열
        topologicalSort();
        System.out.println(sb.toString().trim());
    }
}