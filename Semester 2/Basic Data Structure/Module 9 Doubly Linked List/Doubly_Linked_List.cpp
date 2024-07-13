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

    cout << endl << endl << "Inserted at tail" <<endl <<endl;
}

void insert_at_head(Node *&head, int v){
    Node *newNode = new Node(v);
    newNode->next = head;
    head->prev = newNode;
    head = newNode;
    cout << endl << endl << "Inserted at head" <<endl <<endl;
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
    newNode->prev=tmp;
    tmp->next->prev=newNode;
    tmp->next=newNode;
    cout << endl << endl << "Inserted at: "<<pos <<endl <<endl;
}
int list_size(Node *head){
    Node *tmp=head;
    int cnt=0;
    while(tmp!=NULL){
        cnt++;
        tmp=tmp->next;
    }
    return cnt;
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
    tmp->next->prev = tmp;
    delete deletNode;
    cout << endl << "Deleted from position: " << pos << endl << endl;
}
void delete_head(Node *&head){
    if(head==NULL){
        cout << "Head is not available." << endl<< endl;
    }
    Node *deleteNode = head;
    head = head->next;
    head->prev = NULL;
    delete deleteNode;
    cout << endl << "Deleted head" << endl << endl;
}
void delete_tail(Node *&tail){
    Node *deleteNode = tail;
    tail = tail->prev;
    tail->next = NULL;
    delete deleteNode;
    cout << endl << "Deleted tail" << endl << endl;
}
void print_normal(Node *head){
    cout << endl << endl << "Normal Linked List: ";
    Node *temp = head;
    while(temp!=NULL){
        cout << temp->val << " ";
        temp = temp->next;
    }
}
void print_reverse(Node *tail){
    cout << endl << endl << "Reverse Linked List : ";
    Node *temp = tail;
    while(temp!=NULL){
        cout << temp->val << " ";
        temp = temp->prev;
    }
    cout << endl << endl;
}

int main(){
    Node *head = NULL;
    Node *tail = NULL;
    while(true){
        cout << "Option 1: Insert at Tail" << endl;
        cout << "Option 2: Print Linked List" << endl;
        cout << "Option 3: Insert at any Position: " << endl;
        cout << "Option 4: Insert at Head" << endl;
        cout << "Option 5: Delete node at any Position: " << endl;
        cout << "Option 6: Delete node at Head" << endl;
        cout << "Option 7: Delete node at tail" << endl;
        cout << "Option 8: Terminate" << endl;
        int op;
        cin >> op;
        if(op==1){
            cout << "Please enter value: ";
            int v;
            cin >> v;
            insert_at_tail(head,tail,v);
        }
        else if(op==2){
            print_normal(head);
            print_reverse(tail);
        }
        else if(op==3){
            cout << "Enter position value: ";
            int pos;
            cin >> pos;
            cout << "Please enter value: ";
            int v;
            cin >> v;
            if(pos==0) insert_at_head(head, v);
            else if(pos==list_size(head)) insert_at_tail(head,tail,v);
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
            if(pos==0) delete_head(head);
            else if(pos==list_size(head)) delete_tail(tail);
            else delete_from_pos(head,pos);
        }
        else if(op==6){
            delete_head(head);
        }
        else if(op==7){
            delete_tail(tail);
        }
        else if(op==8){
            break;
        }
    }
    return 0;
}

