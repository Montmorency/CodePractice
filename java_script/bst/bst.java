public class Node {
  private int data;
  private Node left;
  private Node right;

  public Node(int data){
    this.data = data;
    left = null;
    right = null;
  }
}

public class BSTree{
  private Node root;
  public BinarySearchTree(){
    root = null;
  }

public boolean add(int value){
    if (root == null){
      root = Node(value);
      return true;}
    else{
      return root.add(value)}
  }
}
