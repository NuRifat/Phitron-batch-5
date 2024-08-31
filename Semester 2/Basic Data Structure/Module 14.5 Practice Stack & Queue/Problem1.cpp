#include<bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node* next;
    Node* prev;
    Node (int val)
    {
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};
class myStack
{
public:
    Node *head=NULL;
    Node *tail=NULL;
    int sz=0;
    void push(int val){
        sz++;
        Node *newNode = new Node(val);
        if(head==NULL){
            head=newNode;
            tail=newNode;
            return;
        }
        newNode->prev = tail;
        tail->next = newNode;
        tail = tail->next;
    }
    void pop(){
        sz--;
        Node *deleteNode = tail;
        tail = tail->prev;
        if(tail==NULL){
            head=NULL;
        }
        else{
            tail->next=NULL;
        }
        delete deleteNode;
    }
    int top(){
        return tail->val;
    }
    int size(){
        return sz;
    }
    bool empty(){
        if(sz==0) return true;
        else return false;
    }
};
bool is_equal(myStack st, myStack stk){
    if(st.size()==stk.size()){
        while(!st.empty()){
            if(st.top()!=stk.top()){
                return false;
            }
            st.pop();
            stk.pop();
        }
    }
    else{
        return false;
    }
    return true;
}


int main(){
    myStack st;
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        st.push(x);
    }
    myStack stk;
    int m;
    cin>>m;
    for(int i=0;i<m;i++){
        int x;
        cin>>x;
        stk.push(x);
    }
    if(is_equal(st,stk)) cout << "YES" << endl;
    else cout << "NO" << endl;
    
    return 0;
}
