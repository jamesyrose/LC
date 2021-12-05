class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        intervals = Arrays.copyOf(intervals, intervals.length + 1);
        intervals[intervals.length - 1] = newInterval;
        
        
        Arrays.sort(intervals, Comparator.comparing(o -> o[0]));
        
        ArrayList<int[]> res = new ArrayList<int[]>();
        // merge
        int idx = 1; 
        int[] curr = intervals[0]; 
        
        for (int[] i : intervals){
            if (curr[1] >= i[0]) {
                curr[1] = Math.max(curr[1], i[1]);
            }else{
                res.add(curr); 
                curr = i; 
            }
        }
        res.add(curr); // add last one
        
        int[][] ans  = new int[res.size()][2]; 
        int cnt = 0 ;
        for (int[] i: res){
            ans[cnt] =  i; 
            cnt ++;
        }
        
        return ans;
    }
}
