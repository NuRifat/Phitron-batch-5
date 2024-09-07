#include<bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node(int val){
        this->val=val;
        this->next = NULL;
    }
};

void insert_at_tail(Node *&head, int v){
    Node *newNode = new Node(v);
    if(head==NULL){
        head = newNode;
        return;
    }
    Node *temp = head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = newNode;
    cout << endl << endl << "Inserted at tail" <<endl <<endl;
}
void insert_at_pos(Node *&head,int pos, int v){
    Node *newNode = new Node(v);
    Node *tmp = head;
    for(int i=1;i<=pos-1;i++){
        tmp=tmp->next;
        if(tmp==NULL){
            cout << "Invalid Index" << endl << endl;
            return ;
        }
    }
    newNode->next=tmp->next;
    tmp->next=newNode;
    cout << endl << endl << "Inserted at: "<<pos <<endl <<endl;
}
void insert_at_head(Node *&head, int v){
    Node *newNode = new Node(v);
    newNode->next = head;
    head = newNode;
    cout << endl << endl << "Inserted at head" <<endl <<endl;
}
void print_linked_list(Node *head){
    cout << endl << endl << "Your Linked List: ";
    Node *temp = head;
    while(temp!=NULL){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl << endl;
}
void delete_from_pos(Node *head, int pos){
    Node *tmp = head;
    for(int i=1;i<=pos-1;i++){
        tmp = tmp->next;
        if(tmp==NULL){
            cout << "Invalid Index" << endl << endl;
            return ;
        }
    }
    if(tmp->next==NULL){
            cout << "Invalid Index" << endl << endl;
            return ;
        }
    Node *deletNode = tmp->next;
    tmp->next = tmp->next->next;
    delete deletNode;
    cout << endl << "Deleted from position: " << pos << endl << endl;
}
void delete_head(Node *&head){
    if(head==NULL){
        cout << "Head is not available." << endl<< endl;
    }
    Node *deleteNode = head;
    head = head->next;
    delete deleteNode;
    cout << endl << "Deleted head" << endl << endl;
}
int main(){
    Node *head = NULL;
    while(true){
        cout << "Option 1: Insert at Tail" << endl;
        cout << "Option 2: Print Linked List" << endl;
        cout << "Option 3: Insert at any Position: " << endl;
        cout << "Option 4: Insert at Head" << endl;
        cout << "Option 5: Delete node at any Position: " << endl;
        cout << "Option 6: Delete node at Head" << endl;
        cout << "Option 7: Terminate" << endl;
        int op;
        cin >> op;
        if(op==1){
            cout << "Please enter value: ";
            int v;
            cin >> v;
            insert_at_tail(head, v);
        }
        else if(op==2){
            print_linked_list(head);
        }
        else if(op==3){
            cout << "Enter position value: ";
            int pos;
            cin >> pos;
            cout << "Please enter value: ";
            int v;
            cin >> v;
            if(pos==0) insert_at_head(head, v);
            else insert_at_pos(head,pos,v);
        }
        else if(op==4){
            cout << "Please enter value: ";
            int v;
            cin >> v;
            insert_at_head(head, v);
        }
        else if(op==5){
            cout << "Enter position value: ";
            int pos;
            cin >> pos;
            delete_from_pos(head, pos);
        }
        else if(op==6){
            delete_head(head);
        }
        else if(op==7){
            break;
        }
    }
    return 0;
}
