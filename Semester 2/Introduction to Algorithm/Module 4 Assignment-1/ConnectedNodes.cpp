#include<bits/stdc++.h>
using namespace std;
const int N = 1e6+5;
vector<int> v[N];

int main(){
    int n,e;
    cin >> n >> e;
    while(e--){
        int a,b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int q;
    cin >> q;
    while(q--){
        int src;
        cin >> src;
        if(v[src].empty()){
            cout << "-1" << endl;
        }
        else{
            sort(v[src].begin(),v[src].end(),greater<int>());
            for(int val:v[src]){
                cout << val << " " ;
            }
            cout << endl;
        }
    }
    return 0;
}
