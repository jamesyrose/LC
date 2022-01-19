
public class PolulatingNextRightPointers {
	public Node connect(Node root) {
        Queue<Node> q = new LinkedList<>();
        
        q.add(root); 
        
        Node curr; 
        Node next; 

        int n; 
        while (q.size() > 0){
            n = q.size(); 
            for (int i = 0; i < n; i++){
                curr = q.poll(); 
                next = q.peek(); 

                if (curr != null){
                    curr.next = (i != n - 1) ? next : null; 

                    if (curr.left != null){
                        q.add(curr.left); 
                    }
                    if (curr.right != null){
                        q.add(curr.right);     
                    }
                }
            
            }
        }
        return root; 
        
    }
}
