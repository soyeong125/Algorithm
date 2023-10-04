class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String start = my_string.substring(0,s);
        String end = my_string.substring(s+overwrite_string.length());
        
        answer = start + overwrite_string + end;
        
        return answer;
    }
}