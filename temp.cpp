#include <iostream>

using namespace std;

int fib(int value);

int main(){
    fib(8);
    return 0;
}

int fib(int value){
    for (int i = 0; i < value; i++)
    {
        cout<<i;
        i += i;
    }
    
}