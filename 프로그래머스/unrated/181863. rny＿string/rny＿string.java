class Solution {
    public String solution(String rny_string) {
        String answer = "";
        String[] ch = rny_string.split("");
        for(String s : ch){
            if(s.equals("m")){
                answer += "rn";
            }
            else{
                answer += s;
            }
        }
        return answer;
    }
}
// class Solution {
//     public String solution(String rny_string) {
//         String answer = rny_string;
//         String[] arr = answer.split("");
//         for(int i = 0 ; i <= arr.length-1 ; i++) {
//             if (arr[i].equals("m")) {
//                 arr[i] = "rn";
//             }
//         }
//         answer =  String.join("",arr);
//         return answer;
//     }
// }