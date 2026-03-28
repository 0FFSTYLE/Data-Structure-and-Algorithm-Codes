#include <iostream>
using namespace std;

const int MAX_SIZE = 10;

int showResult(signed short a[], short size);
int indexResult(signed short a[], int len, short index, int size);
void updateValue(short arr[], int index, signed short value, int size);
bool insertion(short arr[], int &size, int pos, signed short value);
bool deletion(signed short arr[], int &size, int index);

int main()
{
    int lenOfArray = 4;
    signed short arr[MAX_SIZE] = {};

    for (int i = 0; i < lenOfArray; i++)
    {
        cout << "Enter the array element " << i << endl;
        cin >> arr[i];
    }

    showResult(arr, lenOfArray);
    indexResult(arr, lenOfArray, 2, lenOfArray);
    
    updateValue(arr, 3, -43, lenOfArray);
    showResult(arr, lenOfArray);

    insertion(arr, lenOfArray, 4, -92);
    showResult(arr, lenOfArray);

    deletion(arr, lenOfArray, 4);
    showResult(arr, lenOfArray);

    return 0;
}

int showResult(signed short a[], short size)
{
    for (int j = 0; j < size; j++)
    {
        cout << "Element at index " << j << " is " << a[j] << endl;
    }
    cout << endl;
    return 0;
}

int indexResult(signed short a[], int len, short index, int size)
{
    if (index < 0 || index >= size)
    {
        cout << "Given index " << index << "is out array length!!! " << endl;
        return -1;
    }
    else
    {
        cout << "Element of array at index " << index << " is " << a[index] << endl;
    }
    cout << endl;
    return a[index];
}

void updateValue(short arr[], int index, signed short value, int size)
{
    if (index >= 0 && index < size)
    {
        arr[index] = value;
    }
    else
    {
        cout << "Invalid index for update!" << endl;
    }
    cout << endl;
}

bool insertion(short arr[], int &size, int pos, signed short value)
{
    if(size >= MAX_SIZE){
        cout << "Array is full cannot add new elements!!" << endl;
    }
    if(pos < 0 || pos > size){
        cout << "Invalid Index!" << endl;
    }

    for(int i = size; i < pos; i--){
        arr[i] = arr[i-1];
    }
    arr[pos] = value;
    size++;
    return true;
}

bool deletion(signed short arr[], int &size, int index)
{
    if (index < 0 || index >= size)
    {
        cout << "Invalid index for deletion!" << endl;
        return false;
    }

    for(int i = index; i < size - 1; i++){
        arr[i] = arr[i + 1];
    }
    size--;
    return true;
}