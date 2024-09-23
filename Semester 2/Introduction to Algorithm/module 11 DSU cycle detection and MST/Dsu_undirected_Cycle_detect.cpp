#include<bits/stdc++.h>
using namespace std;

const int N = 1e5+5;
int par[N];
int grp_size[N];

void dsu_init(int n){
    for(int i=0;i<n;i++){
        par[i]=-1;
        grp_size[i]=0;
    }
}

int dsu_find(int node){
    if(par[node]==-1) return node;
    int leader = dsu_find(par[node]);
    par[node]=leader;
    return leader;
}

void dsu_union_by_size(int node1, int node2){
    int leaderA = dsu_find(node1);
    int leaderB = dsu_find(node2);
    if(grp_size[leaderA] > grp_size[leaderB]){
        par[leaderB] = leaderA;
        grp_size[leaderA] += grp_size[leaderB];
    }
    else{
        par[leaderA] = leaderB;
        grp_size[leaderB] += grp_size[leaderA];
    }
}

int main(){
    int n,e;
    cin >> n >> e;
    dsu_init(n);
    bool cycle = false;
    while(e--){
        int a,b;
        cin >> a >> b;
        int leaderA = dsu_find(a);
        int leaderB = dsu_find(b);
        if(leaderA == leaderB){
            cycle = true;
        }
        else{
            dsu_union_by_size(a,b);
        }
    }
    if(cycle){
        cout << "Cycle found" << endl;
    }
    else{
        cout << "Cycle not found" << endl;
    }
    return 0;
}

//input
//6 6
//0 1
//0 2
//0 3
//3 4
//3 5
//4 5
