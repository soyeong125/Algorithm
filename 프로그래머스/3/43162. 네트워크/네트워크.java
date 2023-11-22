import java.util.*;

class Solution {  
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] chk = new boolean[n];
        
        for(int i = 0 ; i < n ; i++){
            if(!chk[i]){
                dfs(i,computers,chk);
                answer++;
            }
        }
        
        return answer;
    }
    
    void dfs (int start, int[][] computers, boolean[] chk){
        chk[start] = true;
        for(int i = 0 ; i < chk.length ; i++){
            if(computers[start][i] == 1 && !chk[i]){
                dfs(i,computers,chk);
            }
        }
    }
}