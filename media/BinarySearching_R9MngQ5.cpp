#include<iostream>
using namespace std;
search(int arr[],int start,int end,int searchingValue){
	int mid = (start+end)/2;
	if(arr[start]==searchingValue){
		return start;
	}
	else if(arr[end]==searchingValue)
	return end;
	if(mid<start || start==end){
		cout<<"returned";
		return -1;		
			}
	if(arr[mid]==searchingValue){
	cout<<mid<<"found";	
	return mid;
	}
	else if(mid<searchingValue){
		search(arr,mid+1,end,searchingValue);
	}
	else if(mid>searchingValue){
		search(arr,start,mid-1,searchingValue);
	}
}


int main(){
	int arr[]={3,4,5,2,6,8,9};
	int size=sizeof(arr)/sizeof(arr[0]);
	int searchingValue;
	cin>>searchingValue;
	int searchedValue = search(arr,0,size-1,searchingValue);
	cout<<endl<<searchedValue<<endl;
}
