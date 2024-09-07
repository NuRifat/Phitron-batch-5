#include<bits/stdc++.h>
using namespace std;
bool is_equal(stack<int> st, queue<int> q){
    if(st.size()==q.size()){
        while(!st.empty()){
            if(st.top()!=q.front()){
                return false;
            }
            st.pop();
            q.pop();
        }
    }
    else return false;
    return true;
}
int main(){
    stack<int> st;
    queue<int> q;
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int x;
        cin >> x;
        st.push(x);
    }
    int m;
    cin >> m;
    for(int i=0;i<m;i++){
        int x;
        cin >> x;
        q.push(x);
    }

    if(is_equal(st,q)) cout << "YES" << endl;
    else cout << "NO" << endl;

    return 0;
}