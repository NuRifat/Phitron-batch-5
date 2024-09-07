#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+5;
vector<int> v[N];

bool dfs(int src, int des){
    for(int child : v[src]){
        if(child==des){
            return true;
        }
    }
    return false;
}

int main(){
    int n,e;
    cin >> n >> e;
    while(e--){
        int a,b;
        cin >> a >> b;
        v[a].push_back(b);
    }
    int q;
    cin >> q;
    while(q--){
        int src, des;
        cin >> src >> des;
        if(src==des || dfs(src,des)){
            cout << "YES" << endl;
        }
        else cout << "NO" << endl;
    }
    return 0;
}
