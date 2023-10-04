import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = Arrays.copyOf(arr,arr.length);

        if(k%2 ==0){
            for(int i = 0 ; i < arr.length; i++){
                answer[i] += k;
            }
        }
        else{
            for(int i = 0 ; i < arr.length ; i++){
                answer[i] *= k;
            }
        }
         return answer;
    }
}