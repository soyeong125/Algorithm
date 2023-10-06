class Solution {
    public String[] solution(String[] names) {
        int l = names.length % 5 == 0 ? names.length / 5 : names.length / 5 + 1;
        String[] answer = new String[l];
        int idx = 0;
        for(int i = 0 ; i < names.length ; i += 5){
            answer[idx] = names[i];
            idx +=1;
        }
        return answer;
    }
}