#include<bits/stdc++.h>
using namespace std;

int main(){
    queue<int> q;
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int x;
        cin >> x;
        q.push(x);
    }
    stack<int> stk;
    while(!q.empty()){
        stk.push(q.front());
        q.pop();
    }
    queue<int> qu;
    while(!stk.empty()){
        qu.push(stk.top());
        stk.pop();
    }
    while(!qu.empty()){
        cout << qu.front() << " " ;
        qu.pop();
    }

    return 0;
}