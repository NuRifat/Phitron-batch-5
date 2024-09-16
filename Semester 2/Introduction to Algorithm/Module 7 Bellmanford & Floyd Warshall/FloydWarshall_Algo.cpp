#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
    ll n, e;
    cin >> n >> e;
    ll adj[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j) adj[i][j] = 0;
            else adj[i][j] = INT_MAX;
        }
    }

    while(e--){
        int a,b,c;
        cin >> a >> b >> c;
        adj[a][b] = c;
    }
    cout << "Before: " << endl;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(adj[i][j] == INT_MAX) cout << "INF ";
            else cout << adj[i][j] << " ";
        }
        cout << endl;
    }

    for(int k=0;k<n;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(adj[i][k]+adj[k][j]<adj[i][j]){
                    adj[i][j] = adj[i][k]+adj[k][j];
                }
            }
        }
    }
    cout << "After: " << endl;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(adj[i][j] == INT_MAX) cout << "INF ";
            else cout << adj[i][j] << " ";
        }
        cout << endl;
    }
    //to check whether there is loop or not
    for (int i = 0; i < n; i++)
    {
        if (adj[i][i] < 0)
        {
            cout << "Cycle detected" << endl;
            break;
        }
    }

    return 0;
}