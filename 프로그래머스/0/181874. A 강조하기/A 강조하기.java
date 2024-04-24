import java.util.stream.Collectors;
class Solution {
    public String solution(String myString) {
        
        String answer = myString.chars()
            .mapToObj(c -> (char)c)
            .map(c -> (c == 'a' || c == 'A') ? 'A' : Character.toLowerCase(c))
            .map(String::valueOf)
            .collect(Collectors.joining());
            
        return answer;
    }
}