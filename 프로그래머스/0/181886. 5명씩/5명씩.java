import java.util.stream.IntStream;
import java.util.stream.Collectors;
class Solution {
    public String[] solution(String[] names) {
        String[] answer = IntStream.range(0, names.length)
            .filter(i -> (i % 5 == 0))
            .mapToObj(i -> names[i])
            .collect(Collectors.toList())
            .toArray(String[]::new);
        
        return answer;
    }
}