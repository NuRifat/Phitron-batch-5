#include<bits/stdc++.h>
using namespace std;
char a[1005][1005];
bool vis[1005][1005];
vector<pair<int,int>> d ={{0,1},{0,-1},{-1,0},{1,0}};
int n,m;
bool valid(int i, int j){
    if(i<0 || i>=n || j<0 || j>=m){
        return false ;
    }
    return true;
}
bool dfs(int si, int sj){
    vis[si][sj] = true;
    for(int i=0;i<4;i++){
        int ci = si + d[i].first;
        int cj = sj + d[i].second;
        if(valid(ci,cj)==true && a[ci][cj]!='#' && vis[ci][cj]==false){
            if(a[ci][cj]=='B'){
                return true;
            }
            if(dfs(ci,cj)){
                return true;
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
            a[i][j]=c;
            if(c=='A'){
                si = i;
                sj = j;
            }
        }
    } 
    memset(vis,false,sizeof(vis));
    if(dfs(si,sj)){
        cout << "YES" << endl;
    }
    else cout << "NO" << endl;
    return 0;
}