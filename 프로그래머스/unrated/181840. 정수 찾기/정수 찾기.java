import java.util.*;
class Solution {
    public int solution(int[] num_list, int n) {
        boolean answer = Arrays.stream(num_list).anyMatch(i->i==n);
        return answer ? 1 : 0;
    }
}