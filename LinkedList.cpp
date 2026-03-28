#include <iostream>

using namespace std;

typedef struct Node
{
    int data;
    struct Node* next;
} Node;

void Traversal(struct Node * ptr){
    while (ptr != NULL)
    {   
        cout << ptr->data << endl;
        ptr = ptr->next;
    }
    
}

Node* createNode(int val){
    Node* temp = (Node*) malloc(sizeof(Node));
    temp->data = val;
    temp->next = nullptr;
    return temp;
}

int main(){

    struct Node * head;
    struct Node * second;
    struct Node * third;
    struct Node * last;

    head =(struct Node *) malloc(sizeof(struct Node));
    second  = (struct Node *) malloc(sizeof(struct Node));
    third = (struct Node *) malloc(sizeof(struct Node));
    last = (struct Node *) malloc(sizeof(struct Node));

    head->data = 7;
    head->next = third;

    second->data = 4;
    second->next = last;

    third->data = 23;
    third->next = second;

    last->data = 54;
    last->next = NULL;

    
    createNode(8);

    
    // --------TRAVERSAL-------
    Traversal(head);

    return 0;
}