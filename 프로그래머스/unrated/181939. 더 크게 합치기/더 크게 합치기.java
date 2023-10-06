class Solution {
    public int solution(int a, int b) {
        int tmp1 = Integer.parseInt(""+a+b);
        int tmp2 = Integer.parseInt(""+b+a);
        
        return tmp1>tmp2?tmp1:tmp2;
    }
}