import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    static int n;
    static int[] arr;
    static int[] op_arr = new int[4];
    static int max_res = Integer.MIN_VALUE;
    static int min_res = Integer.MAX_VALUE;

    static void dfs(int num, int cnt) {
        if (cnt == n) {
            max_res = Math.max(num, max_res);
            min_res = Math.min(num, min_res);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (op_arr[i] > 0) {
                op_arr[i] -= 1;

                switch(i){
                    case 0: dfs(num + arr[cnt] , cnt +1); break;
                    case 1: dfs(num - arr[cnt] , cnt +1); break;
                    case 2: dfs(num * arr[cnt] , cnt +1); break;
                    case 3: dfs(num / arr[cnt] , cnt +1); break;
                }

                op_arr[i] += 1;

            }
        }

    }


    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }


        for (int i = 0; i < 4; i++) {
            op_arr[i] = sc.nextInt();
        }

        dfs(arr[0],1);

        System.out.println(max_res);
        System.out.println(min_res);
    }
}
