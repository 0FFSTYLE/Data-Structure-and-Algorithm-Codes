#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> num;
    vector<int> num3(5);
    vector<int> num2(5,2);

    cout << num3[1] << endl;

    for(int x : num2) cout << x << "\t";

    cout << endl;

    num3[2] = 4;
    num3.insert(num3.begin(),22);
    cout << num3[2] << endl;
    cout << num3[0];
    
}