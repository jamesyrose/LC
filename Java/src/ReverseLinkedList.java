/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        
        ListNode tmp; 
        ListNode nextNode = head.next;
        
        
        head.next = null; 
        tmp = nextNode.next; 
        nextNode.next = head; 
        head = nextNode; 
        nextNode = tmp; 
            
        while (tmp != null){
            tmp = nextNode.next; 
            nextNode.next = head;
            head = nextNode; 
            nextNode = tmp; 
            
        }
        return head;
    }
}
