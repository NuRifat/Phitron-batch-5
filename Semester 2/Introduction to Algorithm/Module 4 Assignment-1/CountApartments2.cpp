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
int bfs(int si, int sj){
    queue<pair<int,int>> q;
    q.push({si,sj});
    vis[si][sj]=true;
    int cnt=1;
    while(!q.empty()){
        pair<int,int> par = q.front();
        int a = par.first, b = par.second;
        q.pop();
        for(int i=0;i<4;i++){
            int ci = a+d[i].first;
            int cj = b+d[i].second;
            if(valid(ci,cj)==true && mat[ci][cj]!= '#' && vis[ci][cj]==false){
                q.push({ci,cj});
                vis[ci][cj]=true;
                cnt++;
            }
        }
    }
    return cnt;
}
int main(){
    cin >> n >> m;
    vector<pair<int,int>> d;
    vector<int> aprt;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            char c;
            cin >> c;
            mat[i][j]=c;
            if(c=='.'){
                d.push_back({i,j});
            }
        }
    } 
    memset(vis,false,sizeof(vis));
    for(pair<int,int> val: d){
        int si = val.first;
        int sj = val.second;
        if(vis[si][sj]==false){
            int num = bfs(si,sj);
            aprt.push_back(num);
        }
    }
    if(aprt.empty()){
        cout << 0 << endl;
    }
    else{
        sort(aprt.begin(),aprt.end());
        for(int room : aprt){
            cout << room << " ";
        }
    }
    
    return 0;
}