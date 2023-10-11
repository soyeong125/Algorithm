import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    static int n;
    static int m;
    static int[] arr;
    static int[] op_arr = new int[4];
    static List<Integer> opList = new ArrayList<>();
    static boolean[] visited;
    static HashMap<Integer, String> ops;

    static int max_res = Integer.MIN_VALUE;
    static int min_res = Integer.MAX_VALUE;

    static void dfs(int start, int end, int cnt) {
        if (cnt == n) {
            max_res = Math.max(start, max_res);
            min_res = Math.min(start, min_res);
            return;
        }

        for (int i = 0; i < m; i++) {
            if (!visited[i]) {
                visited[i] = true;
                String o = ops.get(opList.get(i));
                int tmp = 0;
                switch (o) {
                    case "+":
                        tmp = start + end;
                        break;
                    case "-":
                        tmp = start - end;
                        break;
                    case "x":
                        tmp = start * end;
                        break;
                    case "/":
                        if (start < 0) {
                            tmp = (Math.abs(start) / end) * -1;
                        } else {
                            tmp = start / end;
                        }
                        break;
                }
                int tmp_end = end;
                if (cnt + 1 < n) {
                    end = arr[cnt + 1];
                }
                dfs(tmp, end, cnt + 1);

                end = tmp_end;
                visited[i] = false;
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

        ops = new HashMap<>() {
            {
                put(0, "+");
                put(1, "-");
                put(2, "x");
                put(3, "/");

            }
        };

        for (int i = 0; i < 4; i++) {
            op_arr[i] = sc.nextInt();
            if (op_arr[i] > 0) {
                int tmp = 0;
                while (tmp < op_arr[i]) {
                    opList.add(i);
                    tmp += 1;
                }
            }
        }

        m = opList.size();
        visited = new boolean[m];

        dfs(arr[0], arr[1], 1);

        System.out.println(max_res);
        System.out.println(min_res);
    }
}
