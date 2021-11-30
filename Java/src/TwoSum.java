
import java.util.Arrays;
import java.util.HashMap;				


public class TwoSum {

	public static void main(String[] args) {
        int[] nums = new int[]{2,7,11,15}; 
        int target = 9;
        int[] ans = twoSum(nums, target);
        int[] act = new int[] {0, 1};
        if (Arrays.equals(ans,  act)) {
        	System.out.println("Pass");
        }
	}
	
    public static int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(); 
        int cnt = 0; 
        for (int n : nums){
            map.put(n, cnt);
            cnt ++; 
        }
        cnt = 0; 
        for (int n :nums){
            if (map.keySet().contains(target - n)){
                int idx = map.get(target - n);
                if (idx != cnt){
                    int[] out = new int[]{cnt, idx};
                    return out;
                }
            }
            cnt++; 
        }
        int[] out = new int[2];
        return out;
    }
}
