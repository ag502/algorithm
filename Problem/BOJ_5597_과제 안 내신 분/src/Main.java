import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> students = new HashSet<>();
        for (int std = 1; std <= 30; std++) {
            students.add(std);
        }

        for (int i = 0; i < 28; i++) {
            students.remove(Integer.parseInt(br.readLine()));
        }

        ArrayList<Integer> studentList = new ArrayList<>(students);
        Collections.sort(studentList);

        for (int student : studentList) {
            System.out.println(student);
        }
    }
}
