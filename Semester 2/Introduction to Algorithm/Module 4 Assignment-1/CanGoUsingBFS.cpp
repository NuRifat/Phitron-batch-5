#include<bits/stdc++.h>
using namespace std;
char mat[1005][1005];
bool vis[1005][1005];
vector<pair<int,int>> d ={{0,1},{0,-1},{-1,0},{1,0}};
int n,m;
bool valid(int i, int j){
    if(i<0 || i>=n || j<0 || j>=m){
        return false ;
    }
    return true;
}
bool bfs(int si, int sj){
    queue<pair<int,int>> q;
    q.push({si,sj});
    vis[si][sj]=true;
    while(!q.empty()){
        pair<int,int> par = q.front();
        int a = par.first, b = par.second;
        q.pop();
        for(int i=0;i<4;i++){
            int ci = a+d[i].first;
            int cj = b+d[i].second;
            if(valid(ci,cj)==true && mat[ci][cj]!= '#' && vis[ci][cj]==false){
                if(mat[ci][cj]=='B') {
                    return true;
                }
                q.push({ci,cj});
                vis[ci][cj]=true;
            }
        }
    }
    return false;
}
int main(){
    cin >> n >> m;
    int si,sj;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            char c;
            cin >> c;
            mat[i][j]=c;
            if(c=='A'){
                si = i;
                sj = j;
            }
        }
    } 
    memset(vis,false,sizeof(vis));
    if(bfs(si,sj)){
        cout << "YES" << endl;
    }
    else cout << "NO" << endl;
    return 0;
}