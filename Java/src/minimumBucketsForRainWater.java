import java.util.Arrays;

public class minimumBucketsForRainWater {
    public int minimumBuckets(String street) {
        boolean l = false; 
        boolean r = false; 
        int count = 0; 
        char[] schar = street.toCharArray(); 
        int[] filled = new int[street.length()]; 
        Arrays.fill(filled, 0); 
        for (int i = 0; i< street.length(); i++){
            if (filled[i] == 1){
                continue; 
            }
            if (schar[i] == 'H'){
                // check both sides, choose right
                l = (i > 0 && schar[i -1 ] == '.'); 
                r = (i < street.length() - 1 && schar[i + 1] == '.' ); 
                if (r){
                    filled[i] = 1; 
                    filled[Math.min(street.length() - 1, i + 1)] = 1; 
                    filled[Math.min(street.length() - 1, i + 2)] = 1; 
                    count++; 
                }else if (l){
                    filled[i] = 1; 
                    filled[Math.max(0, i - 1)] = 1; 
                    count++;
                }else{
                    return -1;
                }
                
            }   
                
        }
        return count; 
            
    }
}
