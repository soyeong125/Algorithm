import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    static int n;
    
    static boolean check(String tmp){
        List<String> list = Arrays.stream(tmp.split("")).collect(Collectors.toList());
        int m = tmp.length();
        for(int i = 1 ; i <= m/2 ; i++){ //갯수
            for(int j = 0 ; j <= m-(i*2) ; j++){ //시작점
                if(list.subList(j,j+i).equals(list.subList(j+i,j+i+i))){
                    return false;
                }
            }
        }

        return true;
    }

    static void dfs(int cnt, String tmp){
        if(cnt == n){
            System.out.println(tmp);
            System.exit(0);
        }

        String tmp2 = tmp;
        for(int i = 1 ; i < 4 ; i++) {
            tmp += i + "";
            if (cnt == 0) {
                dfs(cnt + 1, tmp);
            } else {
                if (check(tmp)) {
                    dfs(cnt + 1, tmp);
                } else {
                    tmp = tmp2;
                    continue;
                }
                tmp = tmp2;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        dfs(0,"");
        
    }
}
