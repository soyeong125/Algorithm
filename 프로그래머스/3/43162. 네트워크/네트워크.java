import java.util.*;

class Solution {
    
    static int[] visited;
    static Map<Integer, List<Integer>> map = new HashMap<>();
    
    void check(int start){
        if(map.get(start) == null){
            return;
        }
        for(Integer v : map.get(start)){
            if(visited[v] == 0){
                visited[v] = 1;
                check(v);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        for(int i = 0 ; i < n ; i++){
            for(int j = i+1 ; j < n ; j++){
                    if(!map.containsKey(i)){
                        map.put(i, new ArrayList<>());
                    }
                    if(!map.containsKey(j)){
                        map.put(j, new ArrayList<>());
                    }
                    if(computers[i][j] == 1){
                        map.get(i).add(j);
                        map.get(j).add(i);
                    }
                }
            }   
        
        visited = new int[n];
        
        for(int i = 0 ; i < n ; i++){
            if(visited[i] == 1)
                continue;
            visited[i] = 1;
            answer += 1;
            check(i);
            
        }
        
        return answer;
    }
}