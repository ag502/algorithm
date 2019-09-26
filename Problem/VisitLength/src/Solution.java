import java.util.ArrayList;

public class Solution {
    private ArrayList<int [][]> locations = new ArrayList<>();
    private int[] location = new int[2];

    private int[] move(int x, int y, String dir) {
        switch (dir) {
            case "U":
                y += 1;
                break;
            case "D":
                y -= 1;
                break;
            case "R":
                x += 1;
                break;
            case "L":
                x -= 1;
                break;
            default:
                break;
        }
        location[0] = x;
        location[1] = y;
        return location;
    }

    private boolean isSameArray(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) {
            return false;
        }
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }

    public int solution(String dirs) {
        String[] directions = dirs.split("");
        int x, y;
        int[] currentLocation = {0, 0};

        for (int i = 0; i < directions.length; i++) {
            int[] nextLocation = move(currentLocation[0], currentLocation[1], directions[i]);
            int tempX = nextLocation[0];
            int tempY = nextLocation[1];
            if (tempX > 5 || tempX < -5 || tempY > 5 || tempY < -5) {
                continue;
            } else {
                x = tempX;
                y = tempY;
                int j;
                for (j = 0; j < locations.size(); j++) {
                    if (isSameArray(locations.get(j)[0], currentLocation) && isSameArray(locations.get(j)[1], nextLocation) ||
                        isSameArray(locations.get(j)[0], nextLocation) && isSameArray(locations.get(j)[1], currentLocation)) {
                        break;
                    }
                }
                int[] movedLocation = {x, y};
                if (j >= locations.size()) {
                    int[] [] movedLocations = {currentLocation, movedLocation};
                    locations.add(movedLocations);
                }
                currentLocation = movedLocation;
            }
        }

        for(int[][] a: locations) {
            System.out.print("[");
            for(int k = 0; k < a.length; k++) {
                for(int z = 0; z < a[k].length; z++) {
                    System.out.print(a[k][z]);
                    System.out.print(",");
                }
            }
            System.out.print("]");
        }
        return locations.size();
    }

    public static void main(String[] args) {
        System.out.println(new Solution().solution("ULURRDLLU"));
        System.out.println(new Solution().solution("LULLLLLLU"));
        System.out.println(new Solution().solution("UUUUUUUUUUU"));
        System.out.println(new Solution().solution("LDRULDRU"));
        System.out.println(new Solution().solution("LDRUURDLR"));
    }
}
