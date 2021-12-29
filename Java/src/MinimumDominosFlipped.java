import java.util.Arrays;
import java.util.function.IntConsumer;
import java.util.function.IntUnaryOperator;
import java.util.stream.IntStream;

public class MinimumDominosFlipped {
	public int minDominoRotations(int[] tops, int[] bottoms) {
        int[] topsCnt = new int[6]; 
        int[] bottomsCnt = new int[6]; 
        int[] total = new int[6]; 
        Arrays.fill(topsCnt, 0); 
        Arrays.fill(bottomsCnt, 0); 
        Arrays.fill(total, 0); 

        int n = tops.length;
        
        IntConsumer maps = (i) -> {
            topsCnt[tops[i] - 1]++; 
            bottomsCnt[bottoms[i] - 1]++;
            if (tops[i] == bottoms[i]){
                total[tops[i] - 1]++; 
            }else{
                total[tops[i] - 1]++; 
                total[bottoms[i] - 1]++; 
            }
        }; 
        
        
        IntStream.range(0, n).forEach(maps); 
        
        IntUnaryOperator  find = (i) -> (total[i] >= n) ?  Math.min(n - topsCnt[i], n - bottomsCnt[i]) : n + 1; 
        int res = IntStream.range(0, 6).map(find).min().orElse(n + 1);
        
        return (res < n + 1) ? res : -1; 
    }
}
