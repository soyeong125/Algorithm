class Solution {
    public int solution(int[] num_list) {
        //짝수번째가 홀수번째임
        int ans1 = 0;
        int ans2 = 0;
        
        for (int i = 0 ; i < num_list.length ;i++){
            if (i%2 == 0){
                ans1 += num_list[i];
            }
            else{
                ans2 += num_list[i];
            }
        }
            
        return ans1 >= ans2 ? ans1 : ans2;
        
    }
}