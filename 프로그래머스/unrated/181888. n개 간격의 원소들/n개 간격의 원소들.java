import java.util.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        List<Integer> tmp = new ArrayList<Integer>();
        for (int i = 0 ; i < num_list.length ; i += n){
            tmp.add(num_list[i]);
        }
        int[] answer = new int[tmp.size()];
        for(int i = 0 ; i < tmp.size(); i++){
            answer[i] = tmp.get(i);
        }
        
        return answer;
    }
}