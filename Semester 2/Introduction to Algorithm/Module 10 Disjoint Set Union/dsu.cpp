#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+5;
int par[N];
int grp_size[N];
int level[N];
void dsu_init(int n){
    for(int i=0;i<n;i++){
        par[i] = -1;
        grp_size[i]=1;
        level[i]=0;
    }
}
int dsu_find(int node){
    if(par[node]==-1) return node;
    int leader = dsu_find(par[node]);
    par[node] = leader;
    return leader;
}

void dsu_union(int node1, int node2){
    int leaderA = dsu_find(node1);
    int leaderB = dsu_find(node2);
    par[leaderA] = leaderB;
}
void dsu_union_by_size(int node1, int node2){
    int leaderA = dsu_find(node1);
    int leaderB = dsu_find(node2);
    if(grp_size[leaderA]>grp_size[leaderB]){
        par[leaderB] = leaderA;
        grp_size[leaderA] += grp_size[leaderB];
    }
    else{
        par[leaderA] = leaderB;
        grp_size[leaderB] += grp_size[leaderA];
    }
}
void dsu_union_by_level(int node1, int node2){
    int leaderA = dsu_find(node1);
    int leaderB = dsu_find(node2);
    if(level[leaderA]>level[leaderB]){
        par[leaderB] = leaderA;
    }
    else if(level[leaderB]>level[leaderA]){
        par[leaderA] = leaderB;
    }
    else{
        par[leaderA] = leaderB;
        level[leaderB]++;
    }
}

int main(){
    dsu_init(6);
    dsu_union_by_size(1,4);
    dsu_union_by_size(3,0);
    dsu_union_by_size(3,2);
    dsu_union_by_size(1,5);
    dsu_union_by_size(1,2);
    cout << dsu_find(3) << endl;

    return 0;
}
