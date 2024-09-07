#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *left;
    Node *right;
    Node(int val)
    {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};
Node *input_tree()
{
    int val;
    cin >> val;
    Node *root;
    if (val == -1)
        root = NULL;
    else
        root = new Node(val);
    queue<Node *> q;
    if (root)
        q.push(root);
    while (!q.empty())
    {
        Node *p = q.front();
        q.pop();

        int l, r;
        cin >> l >> r;
        Node *myLeft;
        Node *myRight;
        if (l == -1)
            myLeft = NULL;
        else
            myLeft = new Node(l);
        if (r == -1)
            myRight = NULL;
        else
            myRight = new Node(r);

        p->left = myLeft;
        p->right = myRight;

        if (p->left)
            q.push(p->left);
        if (p->right)
            q.push(p->right);
    }
    return root;
}
int treeHeight(Node *root)
{
    if (root == NULL)
        return 0;
    int l = treeHeight(root->left);
    int r = treeHeight(root->right);
    return max(l, r) + 1;
}
int countNode(Node *root)
{
    if (root == NULL)
        return 0;
    int l = countNode(root->left);
    int r = countNode(root->right);
    return l + r + 1;
}
int main()
{
    Node *root = input_tree();
    int height = treeHeight(root);
    int Node_num = countNode(root);
    int a = pow(2,height)-1;
    if(a==Node_num) cout << "YES" ;
    else cout << "NO" ;
    return 0;
}
