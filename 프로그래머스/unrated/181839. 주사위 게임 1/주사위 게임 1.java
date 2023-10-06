class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        //둘다 홀수라면
        if(a%2 != 0 && b%2 != 0){
            answer = (a*a) + (b*b);
        }
        //둘다 짝수라면
        else if(a%2 == 0 && b%2 == 0){
            answer = Math.abs(a-b);
        }        
        //둘중 하나만 홀수라면
        else{
            answer = 2 * (a+b);
        }
        
        return answer;
    }
}