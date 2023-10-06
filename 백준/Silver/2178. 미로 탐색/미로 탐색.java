import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] map = new int[n][m];
        //전체 사각형 입력 받기
        for(int i=0; i<n; i++){
            String input = sc.next();
            for(int j=0; j<m; j++){
                map[i][j] = input.charAt(j)-'0';
            }
        }

        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        int res = n*m;

        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new LinkedList<>();
        visited[0][0] = false;
        q.add(new int[]{0,0,1});

        while(!q.isEmpty()){
            int[] point = q.poll();
            int x = point[0];
            int y = point[1];
            int cnt = point[2];
            if (x == (n-1) && y == (m-1)){
                res = Math.min(res,cnt);
                break;
            }

            for(int k = 0 ; k < 4; k++){
                int xx = x + dx[k];
                int yy = y + dy[k];
                if (0<=xx && xx<n && 0<=yy && yy<m){
                    if(!visited[xx][yy] && map[xx][yy] == 1){
                        visited[xx][yy] = true;
                        q.add(new int[]{xx,yy,cnt+1});
                    }
                }
            }
        }

        System.out.println(res);

    }
}