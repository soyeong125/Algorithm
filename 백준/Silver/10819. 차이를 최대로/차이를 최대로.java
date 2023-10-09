import java.util.*;
import java.io.*;
public class Main {
    static int n;
    static int[] arr;
    static int[] visited ;
    static int res = Integer.MIN_VALUE;

    static void dfs (int cnt){
        if(cnt == n){
            int[] new_arr = new int[n];
            for(int i = 0 ; i < n ; i++){
                new_arr[visited[i]-1] = arr[i];
            }

            int tmp = 0 ;
            for(int i = 0 ; i < n-1 ;i++){
                tmp += Math.abs(new_arr[i] - new_arr[i+1]);
            }
            res = Math.max(tmp,res);
            return;
        }

        for (int i = 0 ; i < n ; i++){
            if(visited[i] == 0){
                visited[i] = cnt + 1;
                dfs(cnt + 1);
                visited[i] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        for(int i = 0 ; i < n ; i++){
            int tmp = sc.nextInt();
            arr[i] = tmp;

        }

        visited = new int[n];

        dfs(0);

        System.out.println(res);
    }
}
