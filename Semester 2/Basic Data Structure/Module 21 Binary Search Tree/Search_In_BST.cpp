#include<bits/stdc++.h>
using namespace std;
class Node{
public:
    int val;
    Node* left;
    Node* right;
    Node(int val){
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};
Node* input_tree(){
    int val;
    cin >> val;
    Node* root = new Node(val);
    queue<Node*> q;
    if(root) q.push(root);
    while(!q.empty()){
        Node* p = q.front();
        q.pop();

        int l,r;
        cin >> l >> r;
        if(l==-1) p->left = NULL;
        else p->left = new Node(l);
        if(r==-1) p->right = NULL;
        else p->right = new Node(r);

        if(p->left) q.push(p->left);
        if(p->right) q.push(p->right);
    }
    return root;
}
void levelorder(Node* root){
    queue<Node*> q;
    if(root) q.push(root);
    else{
        cout << "Tree Nai" ;
        return;
    }
    while(!q.empty()){
        Node* f = q.front();
        q.pop();

        cout << f->val << " " ;

        if(f->left) q.push(f->left);
        if(f->right) q.push(f->right);
    }
}
int countNode(Node* root){
    if(root==NULL) return 0;

    int l = countNode(root->left);
    int r = countNode(root->right);

    return max(l,r)+1;
}
bool search_bst(Node* root, int x){
    if(root==NULL) return false;
    if(root->val==x) return true;
    if(x<root->val) return search_bst(root->left,x);
    else return search_bst(root->right,x);
}
void insert(Node* &root,int x){
    if(root==NULL){
        Node* root = new Node(x);
        return;
    }
    if(x < root->val){
        if(root->left==NULL){
            root->left = new Node(x);
        }
        else{
            insert(root->left,x);
        }
    }
    if(x > root->val){
        if(root->right==NULL){
            root->right = new Node(x);
        }
        else{
            insert(root->right,x);
        }
    }
}

int main(){
    Node* root = input_tree();
    insert(root,38);
    insert(root,70);
    levelorder(root);
    cout << endl << countNode(root) << endl;
    if(search_bst(root,60)) cout << "Yes Found" << endl;
    else cout << "Not Found" << endl;

    return 0;
}
