#include<iostream>
using namespace std;
int* insertionSort(int arr[],int size){
	
	int i,key,j;
	for(i=1;i<size;i++){
		key = arr[i];
		j=i-1;
		while(j<=0 && key<arr[j]){
			key=arr[j];
			j--;
		}
	arr[i] = key;
	}
	
	return arr;
}
int * SelectionSort(int A[], int n) 
{ 
int min;
 for (int i=0; i<n-1; i++){
     for (int j=i+1, min=i; j<n; j++){
		if(A[min] > A[j]){
           	min=j;
            }          
        }
      swap (A[i], A[min]);
  }
  return A;
}


int main(){
	int a[] = {1,4,3,7,6};
	int *arr = insertionSort(a,5);
	for(int i=0;i<5;i++)
	cout<<arr[i];
	int* a2=SelectionSort(a,5);
	cout<<endl;
	for(int i=0;i<5;i++)
	cout<<a2[i];
}
