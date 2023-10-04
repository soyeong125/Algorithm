class Solution {
    public int solution(int[] date1, int[] date2) {
        int answer = 0;
        //연도 비교
        if (date1[0] < date2[0]){
            answer = 1;
        }
        else if (date1[0] > date2[0]){
            answer = 0;
        }
        else{
            //월 비교
            if(date1[1] < date2[1]){
                answer = 1;
            }
            else if (date1[1] > date2[1]){
                answer = 0;
            }
            else{
                //일 비교
                if (date1[2] < date2[2]){
                    answer = 1;
                }
                else if(date1[2] >= date2[2]){
                    answer = 0;
                }
            }
        }
        return answer;
    }
}