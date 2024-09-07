#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node *left, *right;
    Node(int val)
    {
        this->val = val;
        left = right = NULL;
    }
};

Node* input_tree()
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

        if (l != -1)
        {
            p->left = new Node(l);
            q.push(p->left);
        }

        if (r != -1)
        {
            p->right = new Node(r);
            q.push(p->right);
        }
    }
    return root;
}
vector<int> v;

void left_boundary(Node* root)
{
    if (root == NULL)
        return;

    if (root->left)
    {
        left_boundary(root->left);
        v.push_back(root->val);
    }
    else if (root->right)
    {
        left_boundary(root->right);
        v.push_back(root->val);
    }
    else
    {
        v.push_back(root->val);
    }
}

void right_boundary(Node* root)
{
    if (root == NULL)
        return;

    if (root->right)
    {
        v.push_back(root->val);
        right_boundary(root->right);
    }
    else if (root->left)
    {
        v.push_back(root->val);
        right_boundary(root->left);
    }
    else
    {
        v.push_back(root->val);
    }
}

void tree_boundary(Node* root)
{
    if (root == NULL)
        return;

    left_boundary(root->left);
    v.push_back(root->val);
    right_boundary(root->right);
}

int main()
{
    Node *root = input_tree();
    v.clear();
    tree_boundary(root);

    for(int val : v)
    {
        cout << val << " ";
    }

    return 0;
}

