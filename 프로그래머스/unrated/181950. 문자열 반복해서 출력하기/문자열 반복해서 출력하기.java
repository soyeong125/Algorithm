import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int num = sc.nextInt();
        String res = "";

        for (int i = 0; i < num; i++) {
            res += str;
        }
        
        System.out.println(res);
    }
}