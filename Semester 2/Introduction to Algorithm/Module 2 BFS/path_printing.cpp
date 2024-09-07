#include<bits/stdc++.h>
using namespace std;
vector<int> v[105];
bool vis[105];
int level[105];
int parent[105];
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
                parent[child]= par;
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
    int src,des;
    cin >> src >> des;
    memset(vis,false,sizeof(vis));
    memset(level,-1,sizeof(level));
    memset(parent,-1,sizeof(parent));
    bfs(src);
    vector<int> path;
    int x = des;
    while(x!=-1){
        path.push_back(x);
        x = parent[x];
    }
    reverse(path.begin(),path.end());
    for(int val:path){
        cout << val << " " ;
    }
    return 0;
}

