class Solution {
    static int dfs(int idx,int tmp,int[] numbers,int len,int target){
        if(idx == len){
            if(tmp == target){
                return 1;
            }
            return 0;
        }
        return dfs(idx+1,tmp+numbers[idx],numbers,len,target) + dfs(idx+1,tmp-numbers[idx],numbers,len,target);
    }
    
    
    
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        answer = dfs(0,0,numbers,numbers.length,target);
        
        return answer;
    }
}