
public class MiniumumNumberOfTaps {
    int[] rr; 
    int res;
    int curr;
    int tmp;
    public int minTaps(int n, int[] ranges) {
        rr = new int[n + 1]; 
        res = 0; 
        curr = 0; 
        tmp = 0;
        
        IntStream.range(0, ranges.length).forEach(i -> {
          rr[Math.max(0, i - ranges[i])] = Math.max(
              Math.min(n, i + ranges[i]),
              rr[i]
          );
        });
        

        
        IntConsumer findRange = (i) -> {
            tmp = Math.max(rr[i], tmp); 
            if (curr == i){
                res++; 
                curr = tmp; 
            }
        };
        
        IntStream.range(0, n).forEach(findRange);

        return curr == n ? res : -1; 
    }
}