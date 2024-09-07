#include<bits/stdc++.h>
using namespace std;
vector<int> v[105];
bool vis[105];
int level[105];

void bfs(int src){
    queue<int> q;
    q.push(src);
    vis[src] = true;
    level[src] = 0;
    while(!q.empty()){
        int par = q.front();
        q.pop();
        for(int child: v[par]){
            if(vis[child]==false){
                q.push(child);
                vis[child]=true;
                level[child] = level[par]+1;
            }
        }
    }

}
int main(){
    int n,e;
    cin >> n >> e;
    while(e--){
        int a,b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    memset(vis,false,sizeof(vis));
    memset(level,-1,sizeof(level));
    bfs(0);
    int lev;
    cin >> lev;
    for(int i=n-1;i>=0;i--){
        if(level[i]==lev){
            cout << i << " ";
        }
    }
    return 0;
}


