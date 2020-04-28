#include<iostream>
#include<stack>
using namespace std;


static int count=0;





class Node {
   	public:
 	int key;
	Node *left;
	Node *right;
public:
	Node(int key) {
	this->key = key;
	left=NULL;
	right=NULL;
	}		
};


Node *minValueNode(Node* node) 
{ 
    Node* current = node; 
    while (current && current->left != NULL) 
        current = current->left; 
  
    return current; 
} 

class BinaryTree {
	public:
  Node* root;
public:
	BinaryTree(){
		root=NULL;
	}
 void addNode(int key) {
		Node* newNode = new Node(key);
		if (root == NULL) {
			root = newNode;
		}
		 else {
			Node* focusNode = root;
			Node* parent;
			while (true) {
				parent = focusNode;
				
				if (key < focusNode->key) {
					focusNode = focusNode->left;

					if (focusNode == NULL) {

						parent->left = newNode;
						return; 

					}
			} 
			else { 

					focusNode = focusNode->right;

					if (focusNode == NULL) {

						parent->right = newNode;
						return; 
					}
				}
			}
		}

	}




void Postorder(Node* node) 
{ 
    if (node == NULL) 
        return; 
		 
   Postorder(node->left);  
    Postorder(node->right); 
    cout << node->key<< " "; 
}

void Inorder(Node* node) 
{ 
    if (node == NULL) 
        return; 
  
   Inorder(node->left); 
    cout << node->key << " "; 
   Inorder(node->right); 
}


void Preorder( Node* node) 
{ 
    if (node == NULL) 
        return; 
 
    cout << node->key << " "; 
   Preorder(node->left);  
    Preorder(node->right); 
}  

int counter(Node* node) 
{ 
    if (node->left == NULL || node->right==NULL) {
        count++;
		return count; 
}
  else{
   counter(node->left); 
   counter(node->right);
}
}





void inOrder1(Node *root) 
{ 
    stack<Node *> s; 
    Node *curr = root; 

    while (curr != NULL || s.empty() == false) 
    { 
        while (curr !=  NULL) 
        { 

            s.push(curr); 
            curr = curr->left; 
        } 
  
      
        curr = s.top(); 
        s.pop(); 
  
        cout << curr->key << " "; 
  
        curr = curr->right; 
  
    } 
} 


void iterativePreorder(Node *root) 
{ 
    if (root == NULL) 
       return; 
  
    stack<Node *> nodeStack; 
    nodeStack.push(root); 
  
while (nodeStack.empty() == false) 
    { 
        struct Node *node = nodeStack.top(); 
       cout<<node->key<<" "; 
        nodeStack.pop(); 
  
        if (node->right) 
            nodeStack.push(node->right); 
        if (node->left) 
            nodeStack.push(node->left); 
    } 
} 



int maxDepth(Node* node)  
{  
    if (node == NULL)  
        return 0;  
    else
    {  
        int lDepth = maxDepth(node->left);  
        int rDepth = maxDepth(node->right);  
      
        if (lDepth > rDepth)  
            return(lDepth + 1);  
        else return(rDepth + 1);  
    }  
}





Node* deleteNode(Node* root, int key) 
{ 

    if (root == NULL) return root; 
  
    if (key < root->key) 
        root->left = deleteNode(root->left, key); 
  
    else if (key > root->key) 
        root->right = deleteNode(root->right, key); 
  
    else
    { 
       
        if (root->left == NULL) 
        { 
            Node *temp = root->right; 
            delete root; 
            return temp; 
        } 
        else if (root->right == NULL) 
        { 
            Node *temp = root->left; 
            delete root; 
            return temp; 
        } 
  
        Node* temp = minValueNode(root->right); 
        root->key = temp->key; 
  
        root->right = deleteNode(root->right, temp->key); 
    } 
    return root; 
} 



void printLevelOrder(Node* root)  
{  
    int h = maxDepth(root);  
    int i;  
    for (i = 1; i <= h; i++)  
        printGivenLevel(root, i);  
}  
  
void printGivenLevel(Node* root, int level)  
{  
    if (root == NULL)  
        return;  
    if (level == 1)  
        cout << root->key << " ";  
    else if (level > 1)  
    {  
        printGivenLevel(root->left, level-1);  
        printGivenLevel(root->right, level-1);  
    }  
}  


};

	
	   int main() {
       BinaryTree theTree;
		theTree.addNode(50);

		theTree.addNode(25);

		theTree.addNode(15);

		theTree.addNode(30);

		theTree.addNode(75);

		theTree.addNode(85);
		
		theTree.addNode(65);
		
		cout<<"Postorder:"<<endl;
		theTree.Postorder(theTree.root);
		
		
		cout<<endl<<"Inorder:"<<endl;
		theTree.Inorder(theTree.root);
		
		cout<<endl<<"Preorder:"<<endl;
		theTree.Preorder(theTree.root);
		
		cout<<endl<<"counter:"<<theTree.counter(theTree.root);

		cout<<endl<<"Iterative Inorder"<<endl;
		theTree.inOrder1(theTree.root); 
		
		cout<<endl<<"Iterative Preorder"<<endl;
		theTree.iterativePreorder(theTree.root);
		
		cout<<endl<<"Height"<<endl<<theTree.maxDepth(theTree.root)-1<<endl;
		
		theTree.deleteNode(theTree.root,65);
		
		
			cout<<"After deleting Node 65 Postorder:"<<endl;
		theTree.Postorder(theTree.root);
		
		cout<<endl<<"BFS"<<endl;
		theTree.printLevelOrder(theTree.root);
		
}

