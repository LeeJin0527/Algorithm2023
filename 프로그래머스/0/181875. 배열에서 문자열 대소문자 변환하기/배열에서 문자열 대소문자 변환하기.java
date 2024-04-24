import java.util.stream.IntStream;
import java.util.Arrays;

class Solution {
    public String[] solution(String[] strArr) {
        String[] answer = IntStream.range(0, strArr.length)
            .mapToObj(i -> (i % 2 == 0) ? strArr[i].toLowerCase() : strArr[i].toUpperCase())
            .toArray(String[]::new);
        
        return answer;
    }
}