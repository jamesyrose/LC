
public class findDuplicateNumbers {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>(); 
        int curr; 
        for (int i = 0; i < nums.length; i++){
            curr = (nums[i] > 0) ? nums[i] : -nums[i];
            if (nums[curr - 1] < 0){
                res.add(curr);
            }
            nums[curr - 1] = -nums[curr - 1]; 
        }
        return res; 
            
    }
}
