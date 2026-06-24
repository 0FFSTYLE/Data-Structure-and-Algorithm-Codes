#include<iostream>
using namespace std;

int add(int num1, int num2);
int sub(int num1, int num2);
int mul(int num1, int num2);
int div(int num1, int num2);
int rem(int num1, int num2);

int main(){
    int num1, num2;

    cout<<"Enter first number : "; cin>> num1;
    cout<<"Enter second number : "; cin>> num2;

    cout<<add(num1,num2)<<endl;
    cout<<sub(num1,num2)<<endl;
    cout<<mul(num1,num2)<<endl;
    cout<<div(num1,num2)<<endl;
    cout<<rem(num1,num2)<<endl;
}

int add(int num1, int num2){
    return num1 + num2;
}

int sub(int num1, int num2){
    return num1 - num2;
}

int mul(int num1, int num2){
    return num1*num2;
}

int div(int num1, int num2){
    if (num2 == 0)
    {
        cout<<"Cannot divide by 0 ";
    }
    else{
        return num1/num2;
    }
    
}

int rem(int num1, int num2){
    if(num2 == 0){
         cout<<"Cannot divide by 0, unable to process remainder ";
    }
    else{
        return num1%num2;
    }
}