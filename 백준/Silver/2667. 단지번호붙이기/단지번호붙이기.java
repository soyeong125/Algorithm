import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        boolean[][] visited = new boolean[n][n];
        List<Integer> reslist = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                arr[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == 1 && !visited[i][j]) {
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[]{i, j});
                    visited[i][j] = true;
                    int tmp_cnt = 1;

                    while (!q.isEmpty()) {
                        int[] point = q.poll();
                        int x = point[0];
                        int y = point[1];

                        for (int k = 0; k < 4; k++) {
                            int xx = x + dx[k];
                            int yy = y + dy[k];
                            if (xx >= 0 && xx < n && yy >= 0 && yy < n && !visited[xx][yy] && arr[xx][yy] == 1) {
                                q.add(new int[]{xx, yy});
                                visited[xx][yy] = true;
                                tmp_cnt++;
                            }
                        }
                    }
                    reslist.add(tmp_cnt);
                }
            }
        }

        Collections.sort(reslist);
        System.out.println(reslist.size());
        for (int i : reslist) {
            System.out.println(i);
        }
    }
}
