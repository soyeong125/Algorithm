import java.util.*;

class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = arr.clone();
        int l = arr.length;
        if(l%2 == 0){
            for (int i = 1 ; i < answer.length ; i+=2){
                answer[i] += n;
            }
        }
        else{
            for (int i = 0 ; i < answer.length ; i+=2){
                answer[i] +=n;
            }
        }
        return answer;
    }
}