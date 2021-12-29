import java.util.Arrays;

public class CellsWithOddValues {
    public int oddCells(int m, int n, int[][] indices) {
        int[] row = new int[m]; 
        int[] col = new int[n]; 
        Arrays.fill(row, 0); 
        Arrays.fill(col, 0); 
        for(int[] val : indices){
            row[val[0]]++; 
            col[val[1]]++; 
        }
        
        int odds =(int) Arrays.stream(col).filter(x -> x % 2 == 1).count(); 
        int evens = n - odds; 
    
        
        
        int ans =  Arrays.stream(row).map(x -> {
            if ( x % 2 == 0){
                return odds;
            }else{
                return evens; 
            }
        }).sum();
        
        return ans;

    }
}
