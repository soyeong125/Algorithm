class Solution {
    static int N;
    static int T;
    static int A = 0;
    
    static void dfs(int idx,int tmp,int[] numbers){
        if(idx == N){
            if(tmp == T){
                A +=1 ;
            }
            return;
        }
        dfs(idx+1,tmp+numbers[idx],numbers);
        dfs(idx+1,tmp-numbers[idx],numbers);
    }
    
    
    
    public int solution(int[] numbers, int target) {
        int answer = 0;
        N = numbers.length;
        T = target;
        
        dfs(0,0,numbers);
        
        answer = A;
        
        return answer;
    }
}