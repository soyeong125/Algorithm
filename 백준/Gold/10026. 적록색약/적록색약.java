import java.util.*;
import java.io.*;
public class Main {
    static int n;
    static int m;
    static char[][] map;

    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static int res = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        map = new char[n][n];
        for(int i=0; i<n; i++){
            String s = sc.next();
            for(int j=0; j<n; j++){
                map[i][j] = s.charAt(j);
            }
        }

        //R!=G
        int res1 = 0;
        boolean[][] visited = new boolean[n][n];
        for(int i = 0 ; i < n ; i++){
            for (int j = 0 ; j < n ; j++){
                if(!visited[i][j]){
                    res1 += 1;
                    char v = map[i][j];
                    visited[i][j] = true;
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[]{i,j});

                    while(!q.isEmpty()){
                        int[] point = q.poll();
                        int x = point[0];
                        int y = point[1];

                        for(int k = 0 ; k < 4 ; k++){
                            int xx = x + dx[k];
                            int yy = y + dy[k];
                            if (0<=xx && xx<n && 0<=yy & yy<n && !visited[xx][yy]){
                                if(v == map[xx][yy]){
                                    visited[xx][yy] = true;
                                    q.add(new int[]{xx,yy});
                                }
                            }
                        }
                    }
                }
            }
        }
        int res2 = 0;
        visited = new boolean[n][n];
        for(int i = 0 ; i < n ; i++){
            for (int j = 0 ; j < n ; j++){
                if(!visited[i][j]){
                    res2 += 1;
                    char v = map[i][j];
                    visited[i][j] = true;
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[]{i,j});

                    while(!q.isEmpty()){
                        int[] point = q.poll();
                        int x = point[0];
                        int y = point[1];

                        for(int k = 0 ; k < 4 ; k++){
                            int xx = x + dx[k];
                            int yy = y + dy[k];
                            if (0<=xx && xx<n && 0<=yy & yy<n && !visited[xx][yy]){
                                if (v == 'R' || v == 'G'){
                                    if(map[xx][yy] == 'R' || map[xx][yy] == 'G'){
                                        visited[xx][yy] = true;
                                        q.add(new int[]{xx,yy});
                                    }
                                }
                                else{
                                    if(map[xx][yy] == v){
                                        visited[xx][yy] = true;
                                        q.add(new int[]{xx,yy});
                                    }
                                }
                            }
                        }
                    }
                }
            }


        }

        System.out.println(res1 + " " + res2);

    }
}
