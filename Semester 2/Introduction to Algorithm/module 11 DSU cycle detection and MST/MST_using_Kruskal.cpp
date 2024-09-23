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

class edge{
public:
    int u,v,w;
    edge(int u, int v, int w){
        this->u = u;
        this->v = v;
        this->w = w;
    }
};

bool cmp(edge a, edge b){
    return a.w < b.w;
}

int main(){
    int n, e;
    cin >> n >> e;
    dsu_init(n);
    vector<edge> edgeList;
    while(e--){
        int u,v,w;
        cin >> u >> v >> w;
        edgeList.push_back(edge(u,v,w));
    }
    sort(edgeList.begin(),edgeList.end(),cmp);
    int totalCost = 0;
    for(edge ed : edgeList){
        int leaderU = dsu_find(ed.u);
        int leaderV = dsu_find(ed.v);
        if(leaderU == leaderV) continue;
        else{
            dsu_union_by_size(leaderU,leaderV);
            totalCost += ed.w;
        }
    }
    cout << totalCost << endl;
    return 0;
}


//input
//5 7
//0 1 2
//0 2 3
//0 3 3
//3 4 6
//2 4 4
//2 1 7
//1 4 5
