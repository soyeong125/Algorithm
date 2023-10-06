import java.util.*;
class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        //arr2가 크면 -1 arr1이 크면 1 같으면 0
        //배열의 길이가 다르다면 배열이 긴쪽이 크다
        if(arr1.length != arr2.length){
            answer = arr1.length > arr2.length ? 1 : -1;
        }
        //배열이 길이가 같으면 모든 원소의 합을 비교해서 다르면 큰쪽이 크고 같으면 같다
        else
        {
            int arr1_total = Arrays.stream(arr1).sum();
            int arr2_total = Arrays.stream(arr2).sum();
            if (arr1_total == arr2_total){
                answer = 0;
            }
            else{
                answer = arr1_total > arr2_total ? 1 : -1;
            }
        }
        
        return answer;
    }
}