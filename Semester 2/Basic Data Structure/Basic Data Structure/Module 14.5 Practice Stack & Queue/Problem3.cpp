#include<bits/stdc++.h>
using namespace std;

int main(){
    stack<int> st;
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int x;
        cin >> x;
        st.push(x);
    }
    stack<int> stk;
    while(!st.empty()){
        stk.push(st.top());
        st.pop();
    }
    while(!stk.empty()){
        cout << stk.top() << " " ;
        stk.pop();
    }

    return 0;
}