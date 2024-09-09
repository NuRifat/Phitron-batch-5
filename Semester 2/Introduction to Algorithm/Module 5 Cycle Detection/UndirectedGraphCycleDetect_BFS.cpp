#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+5;
vector<int> v[N];
bool vis[N];
int parentArray[N];
bool ans;

void bfs(int s){
    queue<int> q;
    q.push(s);
    vis[s]=true;
    while(!q.empty()){
        int parent = q.front();
        q.pop();
        for(int child:v[parent]){
            if(vis[child]==true && parentArray[parent]!=child){
                ans = true;
            }
            if(vis[child]==false){
                vis[child]=true;
                parentArray[child]=parent;
                q.push(child);
            }
        }
    }
}

int main(){
    int n,e;
    cin >> n >> e;
    while(e--){
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    memset(vis,false,sizeof(vis));
    memset(parentArray,-1,sizeof(parentArray));
    ans =false;
    for(int i=0;i<n;i++){
        if(vis[i]==false){
            bfs(i);
        }
    }
    if(ans){
        cout << "Cycle Detected" << endl;
    }
    else cout << "Cycle Not Detected" << endl;
    return 0;
}
