import java.util.*;

class Solution {
    public List<String> solution(String my_string) {
        List<String> answer = new ArrayList<>();
        for (String s : my_string.split(" ")){
            if (!s.equals("")){
                answer.add(s);
            }         
        }
            
        return answer;
    }
}
