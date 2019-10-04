import java.util.ArrayList;

public class Solution {
    private ArrayList<Point []> locations = new ArrayList<>();

    class Point {
        private int x = 0;
        private int y = 0;

        Point (int x, int y) {
            this.x = x;
            this.y = y;
        }

        private int getX() {return x; }
        private int getY() {return y; }
        private void setX(int x) {this.x = x; }
        private void setY(int y) {this.y = y; }
    }

    private Point move(Point p, String dir) {
        Point temp = new Point(p.getX(), p.getY());
        int x = temp.getX();
        int y = temp.getY();

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
        temp.setX(x);
        temp.setY(y);

        return temp;
    }

    private boolean isSamePoint(Point p1, Point p2) {
        return p1.getX() == p2.getX() && p1.getY() == p2.getY();
    }

    public int solution(String dirs) {
        String[] directions = dirs.split("");
        Point currentPosition = new Point(0, 0);

        for(int i = 0; i < directions.length; i++) {
            Point nextPosition = move(currentPosition, directions[i]);
            int nextX = nextPosition.getX();
            int nextY = nextPosition.getY();

            if (nextX < -5 || nextX > 5 || nextY < -5 || nextY > 5) {
                continue;
            }

            nextPosition.setX(nextX);
            nextPosition.setY(nextY);

            int j;
            for(j = 0; j < locations.size(); j++) {
                if((isSamePoint(currentPosition, locations.get(j)[0]) && isSamePoint(nextPosition, locations.get(j)[1])) ||
                        (isSamePoint(currentPosition, locations.get(j)[1]) && isSamePoint(nextPosition, locations.get(j)[0]))) {
//                    System.out.println("RUN");
                    break;
                }
            }
            if (j >= locations.size()) {
                Point[] moved = new Point[2];
                moved[0] = currentPosition;
                moved[1] = nextPosition;
                locations.add(moved);
            }
            currentPosition = nextPosition;
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
