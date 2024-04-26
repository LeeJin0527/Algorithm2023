import java.util.stream.IntStream;
class Solution {
    public int solution(int[] numbers, int n) {
        int answer = IntStream.of(numbers)
            .reduce(0, (left, right) -> left <= n ? (left + right) : left);
        return answer;
    }
}