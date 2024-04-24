import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        
        String[] answer = IntStream.range(0, todo_list.length)
            .filter(i -> !finished[i])
            .mapToObj(i -> todo_list[i])
            .collect(Collectors.toList())
            .toArray(String[]::new);
        return answer;
    }
}