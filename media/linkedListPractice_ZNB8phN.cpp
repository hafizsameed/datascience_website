#include<iostream>
using namespace std;
class Node{
	public:
	int data;
	Node *next;
	Node(int d){
		data=d;
		next=NULL;
	}
	Node(int d,Node *n){
		data=d;
		next=n;
	}
};
class List{
	public:
		Node *head=NULL;
		Node *tail= NULL;
		List(){
			head=tail=NULL;
		}
		void addtohead(int d){
			if(head==NULL && tail == NULL) head=tail=new Node(d);
			else {
				Node *tmp = new Node(d,head);
				head=tmp;
			}
		}
		void addtotail(int d){
			if(head==NULL && tail==NULL){
			tail= new Node(d);
			head= tail;
			}
			else {
				tail->next = new Node(d);
				tail=tail->next;
			}
		}
		void display(){
			Node *tmp = head;
			while(tmp!=NULL){
				cout<<tmp->data<<" ";
				tmp =  tmp->next;
			}
		}
		
	void deletefromhead(){
		if(head!=NULL){
			Node *tmp = head;
			head = head->next;
			delete tmp ; 
			tmp = NULL;
		}
	}
	void deletefromtail(){
		if(head!=NULL && tail!=NULL){
		Node *tmp = head; 
		while(tmp->next!=tail){
			tmp=tmp->next;
		}
		Node *tmp2 = tail;
		tail=tmp;
		tail->next=NULL;
		delete tmp2; 
		tmp2=NULL;
		}
	}
	void addsomewhere(int d){
		Node *tmp = head;
		while(tmp!=NULL){
			if(tmp->data==d){
			
			}
		}
	}
		
		
};

int main(){
	List l;
//	l.addtohead(12);
	l.addtotail(1);
	l.addtotail(12);
	l.addtotail(11);
//	l.deletefromhead();
	l.addtohead(13);
	l.addtohead(22);
//	l.deletefromhead();
	l.deletefromtail();
	l.display();
}
