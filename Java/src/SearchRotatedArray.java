
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;				


public class SearchRotatedArray {

	public static void main(String[] args) {
        int[] nums = new int[]{4,5,6,7,0,1,2}; 
        int target = 1; 
        int ans = search(nums, target);
        int act = 5;
        if (ans == act) {
        	System.out.println("Pass");
        }
	}
	
    public static int search(int[] nums, int target) {
    	int l = 0;
    	int r = nums.length - 1; 
    	int mid = Math.floorDiv(r, 2);
    	if (r == 0) {
    		if (nums[0] == target) {
    			return 0;
    		}
    	}
    	while (r > l) {
    		if (nums[l] == target) {
    			return l; 
    		}else if (nums[r] == target) {
    			return r;
    		}else if (nums[mid] == target) {
    			return mid;
    		}else {
    			if ((nums[mid] > nums[r] && target < nums[r] ) || 
    					(nums[mid] > nums[l] && target > nums[mid]) || 
    					(nums[mid] < target && target  < nums[r]) ) {
    				l = mid + 1; 
    			}else {
    				r = mid - 1;
    			}
    			mid = l + Math.floorDiv(r - l , 2);
    		}

    	}
    		
        return -1; 
    }
}
