import org.w3c.dom.ls.LSOutput;

import java.util.*;
import java.io.*;


public class Main {
    static int numOfFiles;
    static HashMap<String, Integer> files = new HashMap<>();
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        numOfFiles = Integer.parseInt(br.readLine());

        for (int i = 0; i < numOfFiles; i++) {
            String fileName = br.readLine();
            String extension = fileName.split("\\.")[1];

            if (files.containsKey(extension)) {
                files.replace(extension, files.get(extension) + 1);
            } else {
                files.put(extension, 1);
            }
        }
        Object[] extensions = files.keySet().toArray();
        Arrays.sort(extensions);
        for (Object extension : extensions) {
            System.out.println(extension + " " + files.get((String)extension));
        }
    }
}
