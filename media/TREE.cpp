#include<iostream>
using namespace std;
class Node{
	public:
		int data;
		Node *left,right;
		Node(int d){
			data=d;
			left=right=NULL;
		}
};
class Tree{
	public:
		Node *root;
		Tree(){
			root=NULL;
		}
		void addNode(int data){
			if(root==NULL){
				root= new Node(data);
			}
			else{
				Node *tmp =  root;
				while(1){
					if(tmp->data>data){
						  					
					}
					
				}
			
			}
		}
		
};
