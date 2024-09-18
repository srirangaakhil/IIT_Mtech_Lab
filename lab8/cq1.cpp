#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

struct eArray{

private:
  // put data members here
  int *data_ptr;
  int nums = 0, heap_size = 0;
  static const int DEFAULT_SIZE = 32;

public:
  // construct an array with 0 elements
  eArray(){
    data_ptr = (int*) malloc(DEFAULT_SIZE * sizeof(int));
    if (data_ptr == NULL){
      printf("malloc: Memory not allocated.\n");
    } else{
      heap_size = DEFAULT_SIZE;
    }
  }
  
  // return a reference to the ith element of the array
  int &operator[](int i){
    return data_ptr[i];
  }

  // Append v to the current array
  // Use a simple implementation: allocate a new array to
  // accommodate the extra element v.  Then copy the current
  // array into it.  Copy v, and delete the current array.
  void push_back(int v){
    int *temp_ptr;
    if (nums == heap_size) {
      temp_ptr = (int*) malloc(2 * heap_size * sizeof(int));
      memcpy(temp_ptr, data_ptr, nums * sizeof(int));
      if (temp_ptr == NULL){
        printf("malloc: Memory not allocated.\n");
      } else {
        free(data_ptr);
        data_ptr = temp_ptr;
        heap_size *= 2;
      }
    }
    data_ptr[nums++] = v;
  }
    
  // return the current size of the array
  // "const" says this function will not change the receiver
  int size() const {
    return nums;
  }
    
  // copy constructor
  eArray(const eArray &rhs){
    data_ptr = (int*) malloc(rhs.heap_size * sizeof(int));
    if (data_ptr == NULL){
      printf("malloc: Memory not allocated.\n");
    } else{
      heap_size = rhs.heap_size;
      nums = rhs.nums;
    }
    memcpy(data_ptr, rhs.data_ptr, nums * sizeof(int));
  }
    
  // destructor
  ~eArray(){ 
  	free(data_ptr);
  }
   
  // assignment operator 
  eArray& operator=(const eArray &rhs){
  	nums = rhs.nums;
  	heap_size = rhs.heap_size;
  	free(data_ptr);
  	data_ptr = (int*) malloc(rhs.heap_size * sizeof(int));
    if (data_ptr == NULL){
      printf("malloc: Memory not allocated.\n");
    } else{
      heap_size = rhs.heap_size * sizeof(int);
    }
  	memcpy(data_ptr, rhs.data_ptr, nums * sizeof(int));
  	return *this;
  }
};