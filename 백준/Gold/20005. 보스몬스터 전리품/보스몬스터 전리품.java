import java.util.*;
import java.io.*;



public class Main {
    static int n;
    static int m;
    static int p;
    static char[][] board;
    static int bx;
    static int by;
    static int bhp;
    static Map<Character,int[]> player;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    static int bfs(int x,int y){
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        q.add(new int[]{x,y,0});
        visited[x][y] = true;

        while (q.size() > 0) {
            int[] point = q.poll();
            int px = point[0];
            int py = point[1];
            int cnt = point[2];
            if(board[px][py] == 'B'){
                return cnt;
            }

            for(int i = 0 ; i < 4 ; i++){
                int pxx = px + dx[i];
                int pyy = py + dy[i];
                if (pxx < 0 || pxx >= n || pyy < 0 || pyy >= m){
                    continue;
                }
                if (!visited[pxx][pyy] && board[pxx][pyy] != 'X'){
                    visited[pxx][pyy] = true;
                    q.add(new int[]{pxx,pyy,cnt+1});
                }
            }
        }
        return -1;
    }


    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        p = sc.nextInt();
        board = new char[n][m];
        player = new HashMap<>();
        for(int i = 0 ; i < n ; i++){
            String s = sc.next();
            for(int j = 0 ; j < m; j++){
                board[i][j] = s.charAt(j);
                if(board[i][j] == 'B'){
                    bx = i;
                    by = j;
                }
                else if(board[i][j] != '.' && board[i][j] != 'X'){
                    player.put(board[i][j],new int[]{i,j,0,0});
                }
            }
        }
        for(int i = 0 ; i < p ; i++){
            char c = sc.next().charAt(0);
            int chp = sc.nextInt();
            int[] tmp = player.get(c);
            tmp[2] = chp;
            tmp[3] = bfs(tmp[0],tmp[1]);
            if (tmp[3] == -1){
                player.remove(c);
            }
        }
        bhp = sc.nextInt();

        while (bhp > 0){
            int atk = 0;
            int cnt = 0;
            for(Map.Entry<Character,int[]> entry : player.entrySet()){
                int[] val = entry.getValue();
                if(val[3] > 0){
                    val[3] -= 1;
                }
                else{
                    atk += val[2];
                    cnt += 1 ;
                }
            }
            if(atk >= bhp){
                System.out.println(cnt);
                break;
            }
            else{
                bhp -= atk;
            }
        }
    }
}
