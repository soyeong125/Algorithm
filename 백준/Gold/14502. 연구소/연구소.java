import java.util.*;
import java.io.*;
public class Main {
    static int n;
    static int m;
    static int[][] map;

    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static int res = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        map = new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                map[i][j] = sc.nextInt();
            }
        }

        dfs(0);
        System.out.println(res);

    }

    static void dfs(int wallCnt){
        if(wallCnt == 3){
            bfs();
            return;
        }

        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < m ; j++){
                if(map[i][j] == 0){
                    map[i][j] = 1;
                    dfs(wallCnt+1);
                    map[i][j] = 0;
                }
            }
        }
    }

    static void bfs(){
        Queue<int[]> q = new LinkedList<>();
        for(int i = 0 ; i<n ; i++){
            for(int j = 0 ; j < m ; j++){
                if(map[i][j] == 2){
                    q.add(new int[]{i,j});
                }
            }
        }

        int[][] copyMap = new int[n][m];

        for(int i = 0 ; i < n ; i++){
            copyMap[i] = map[i].clone();
        }

        while(!q.isEmpty()){
            int[] point = q.poll();
            int x = point[0];
            int y = point[1];

            for(int k = 0 ; k < 4 ; k++){
                int xx = x + dx[k];
                int yy = y + dy[k];
                if (0<=xx && xx< n && 0<=yy && yy<m){
                    if(copyMap[xx][yy] == 0){
                        q.add(new int[]{xx,yy});
                        copyMap[xx][yy] = 2;
                    }
                }
            }
        }

        int safe_zone = 0;
        for(int i = 0 ; i < n ; i++){
            for (int j = 0 ; j < m ; j++){
                if (copyMap[i][j] == 0){
                    safe_zone ++;
                }
            }
        }
        res = Math.max(res,safe_zone);
    }


}