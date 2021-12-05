/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    HashMap<Node, Node> conv = new HashMap<Node, Node>();

    public Node cloneGraph(Node node) {
        // Add all the nodes to conv using dfs O(n) where n is number of nodes
        dfs(node);
        
        // maps the neighbors back; 
        for (Node n : conv.keySet()){
            for (Node neigh: n.neighbors){
                conv.get(n).neighbors.add(conv.get(neigh));
            }
        }
        
        
        return conv.get(node);
    }
    
    private void dfs(Node node){
        if (node != null && !conv.containsKey(node)){
            conv.put(node, new Node(node.val));
            
            for (Node n: node.neighbors){
                dfs(n);
            }
        }
        
    }
}
