
public class FindCheapestFlightsWithinKStops {
    int[] prices; 
    int[] copy; 
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        prices = new int[n];

        Arrays.fill(prices,  Integer.MAX_VALUE); 

        prices[src] = 0; 

        copy = Arrays.copyOf(prices, prices.length);
        
        
        IntStream.range(0, k + 1)
            .forEach(x -> {
                copy = Arrays.copyOf(prices, prices.length);
                Arrays.stream(flights)
                    .filter(s -> prices[s[0]] !=  Integer.MAX_VALUE)
                    .forEach( f -> {
                        copy[f[1]] = Math.min(copy[f[1]], prices[f[0]] + f[2]);
                });
                prices = Arrays.copyOf(copy, prices.length);
            });
            return prices[dst] != Integer.MAX_VALUE ? prices[dst] : -1; 
    }
    
}
