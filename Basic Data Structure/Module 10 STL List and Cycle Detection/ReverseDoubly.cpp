#include<bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node *prev;
    Node(int val){
        this->val=val;
        this->next = NULL;
        this->prev = NULL;
    }
};
void insert_at_tail(Node *&head,Node *&tail, int v){
    Node *newNode = new Node(v);
    if(head==NULL){
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next = newNode;
    newNode->prev = tail;
    tail = newNode;
}
void reverse_doubly(Node* head, Node* tail){
    Node *i=head;
    Node *j=tail;
    while(i!=j && i->next!=j){
        swap(i->val,j->val);
        i=i->next;
        j=j->prev;
    }
    swap(i->val,j->val); //in the loop, for number of even numbers case last one don't swap so this line is for the last one
}
void print_linked_list(Node *head){
    Node *tmp = head;
    while(tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp=tmp->next;
    }
}

int main(){
    Node *head = NULL;
    Node *tail = NULL;
    while(true){
        int val;
        cin>>val;
        if(val==-1) break;
        insert_at_tail(head,tail,val);
    }
    reverse_doubly(head,tail);
    print_linked_list(head);
    return 0;
}

