#include <iostream>

int binarySearchIterative(int arr[], int left, int right, int target) {
    while (left <= right) {

        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    int arr[] = {2, 5, 9, 12, 17, 37, 86};
    int target = 17;
    int n = sizeof(arr) / sizeof(arr[0]);

    int result = binarySearchIterative(arr, 0, n - 1, target);
    if (result != -1) {
        std::cout << "Element found at index " << result << std::endl;
    } else {
        std::cout << "Element not found." << std::endl;
    }

    return 0;
}
