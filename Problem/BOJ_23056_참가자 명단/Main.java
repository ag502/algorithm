import java.util.*;
import java.io.*;

public class Main {
    static int totalNumOfClass;
    static int totalNumOfStudent;

    static StringTokenizer st;
    static Map<Integer, List<String>> playerInfo = new HashMap<>();

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_23056_참가자 명단\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        totalNumOfClass = Integer.parseInt(st.nextToken());
        totalNumOfStudent = Integer.parseInt(st.nextToken());

        // 학급별 학생 수 입력
        while (true) {
            st = new StringTokenizer(br.readLine());
            int classNumber = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            
            // 0 일때 입력 중지
            if (classNumber == 0) {
                break;
            }

            List<String> curClassStudents = playerInfo.getOrDefault(classNumber, new ArrayList<String>());
            if (curClassStudents.size() >= totalNumOfStudent) {
                continue;
            }
            curClassStudents.add(name);
            playerInfo.put(classNumber, curClassStudents);
        }

        Arrays.sort(playerInfo.keySet().toArray());

        for (Integer classNumber : playerInfo.keySet()) {
            List<String> curClassStudents = playerInfo.get(classNumber);
            Collections.sort(curClassStudents, new Comparator<String>(){
                @Override
                public int compare(String o1, String o2) {
                    if (o1.length() == o2.length()) {
                        return o1.compareTo(o2);
                    }
                    return o1.length() - o2.length();
                }
            });
        }

        for (Integer classNumber : playerInfo.keySet()) {
            if (classNumber % 2 != 0) {
                List<String> curClassStudents = playerInfo.get(classNumber);
                for (String name : curClassStudents) {
                    System.out.println(classNumber + " " + name);
                }
            }
        }

        for (Integer classNumber : playerInfo.keySet()) {
            if (classNumber % 2 == 0) {
                List<String> curClassStudents = playerInfo.get(classNumber);
                for (String name : curClassStudents) {
                    System.out.println(classNumber + " " + name);
                }
            }
        }
    }
}
