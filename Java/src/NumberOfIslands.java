class Solution {
    char[][] map;
    int count; 
    public int numIslands(char[][] grid) {
        /*
        Use DFS and mark islands as "0" to denote that they have been visited
        
        O(n * m) dfs, checks every position once
        */
        map = grid;
        count = 0; 
        
        
        for (int i = 0 ; i < map.length; i ++){
            for (int j = 0; j < map[0].length; j ++){
                if (dfs(i, j)){
                    count++;
                }
            }
        }
        return count;
        
    }
    
    private boolean dfs(int i, int j){
        if (i >= 0 && i < map.length && 
            j  >= 0 && j < map[0].length  
            && map[i][j] == '1'
           ){
            // if it gets in here, weve established the start of an island
            map[i][j] = '0';
            
            
            // rest do are attached to this island
            dfs(i + 1, j); 
            dfs(i, j + 1); 
            dfs(i - 1 , j); 
            dfs(i, j - 1); 
            return true;
        }else{
            return false;
        }
    
    }
}
