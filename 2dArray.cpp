#include <iostream>


int traversal(int arr[][10], int& row, int& col);


int main()
{
    int row, col;
    int arr[row][col];

    std:: cout << "Enter the number of row : "; std::cin >> row;
    std:: cout << "Enter the number of col : "; std::cin >> col;

    for (int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            std:: cout << "Enter the element at position : " << i << " " << j << " : ";
            std:: cin >> arr[i][j];
        }
        std:: cout << "\n";
    }

    for (int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            std:: cout << "Element at " << i << " " << j << " " << " is " << arr[i][j];
        }
        std:: cout << "\n";
    }


    return 0; 

}