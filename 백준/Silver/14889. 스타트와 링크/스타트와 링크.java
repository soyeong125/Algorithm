import java.util.*;
import java.io.*;
public class Main {
    static int n;
    static int m;
    static int[][] arr;
    static int[] team;
    static boolean[] visited ;
    static int res = Integer.MAX_VALUE;

    static void dfs(int idx, int cnt){
        if(cnt == n/2){
            //팀을 다 정했으니 능력치 계산
            int score1 = 0;
            int score2 = 0;
            for(int i = 0 ; i < n ; i++){
                if (visited[i]){
                    for(int j = i+1; j < n; j++){
                        if(visited[j] && i!=j){
                            score1 += arr[i][j] + arr[j][i];
                        }
                    }
                }

                if(!visited[i]){
                    for(int j = i+1; j < n; j++){
                        if(!visited[j] && i!=j){
                            score2 += arr[i][j] + arr[j][i];
                        }
                    }
                }
            }

            res = Math.min(res, Math.abs(score1-score2));
            return;
        }

        for(int j = idx + 1; j < n ; j++){
            if(!visited[j]){
                visited[j] = true;
                dfs(j,cnt+1);
                visited[j] = false;
            }
        }

    }


    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n][n]; //능력치 입력 받기
        team = new int[n]; //무슨 팀인지 저장할 예정

        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < n ; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        visited = new boolean[n];

        for (int i = 1 ; i < n ; i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(i,1);
                visited[i] = false;
            }
        }

        System.out.println(res);
    }
}
