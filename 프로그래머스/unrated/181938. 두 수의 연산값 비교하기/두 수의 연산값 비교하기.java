class Solution {
    public int solution(int a, int b) {
        int tmp1 = Integer.parseInt(""+a+b);
        int tmp2 = 2 * a * b;
        
        return tmp1 >= tmp2 ? tmp1 : tmp2;
    }
}