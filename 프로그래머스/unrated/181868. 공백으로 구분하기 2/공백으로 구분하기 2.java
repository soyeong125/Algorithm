import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        for (String s : my_string.split(" ")){
            if (!s.equals("")){
                answer.add(s);
            }         
        }
        
        String[] new_answer = new String[answer.size()];
        for(int i = 0 ; i < answer.size() ; i++){
            new_answer[i] = answer.get(i);
        }
        return new_answer;
    }
}
