#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+5;
vector<int> v[N];
bool vis[N];
bool pathVisit[N];
bool ans;

void dfs(int parent){
    vis[parent]=true;
    pathVisit[parent]=true;
    for(int child:v[parent]){
        if(pathVisit[child]){
            ans = true;
        }
        if(!vis[child]){
            dfs(child);
        }
    }
    pathVisit[parent]= false;
}

int main(){
    int n,e;
    cin >> n >> e;
    while(e--){
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
    }
    memset(vis,false,sizeof(vis));
    memset(pathVisit,false,sizeof(pathVisit));
    ans =false;
    for(int i=0;i<n;i++){
        if(vis[i]==false){
            dfs(i);
        }
    }
    if(ans){
        cout << "Cycle Detected" << endl;
    }
    else cout << "Cycle Not Detected" << endl;
    return 0;
}

