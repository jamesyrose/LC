import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

import com.sun.xml.internal.bind.v2.schemagen.xmlschema.List;

public class NumberOfProvinces {
    HashSet<Integer> visited; 
    HashMap<Integer, List<Integer>> mp; 
    int n; 
    int cnt; 
    
    public int findCircleNum(int[][] isConnected) {
        cnt = 0; 
        visited = new HashSet<>(); 
        mp = new HashMap<>(); 
        n = isConnected.length;
        
        List<Integer> tmp;
        for (int i = 0; i < n; i ++){
            for (int j = 0; j < n; j++){
                if (isConnected[i][j] == 1){
                    tmp = mp.getOrDefault(i, new ArrayList<>()); 
                    tmp.add(j);
                    mp.put(i, tmp);                    
                }
                
            }
        }
        
        for (int i = 0; i < n; i ++){
            if (!visited.contains(i)){
                dfs(i);
                cnt++; 
            }
        }
        return cnt; 
    }
    
    public void dfs(int node){
        if  (!visited.contains(node)){
            visited.add(node); 
            for (int i : mp.get(node)){
                dfs(i); 
            }
        }
    }
}