#include <iostream>

int main(){

    int sizeOfArr = 10;
    int reqired;
    int arr[sizeOfArr] = {1,2,3,4,5,6,7,8,9,10};

    std:: cout << "Element to search : " << std:: endl;
    std:: cin >> reqired;

    for (int i = 0; i < sizeOfArr; i++){
        if (arr[i] == reqired)
        {
            std:: cout << "element found at index " << i << std::endl;
        }
        
    }
    return 0;
}