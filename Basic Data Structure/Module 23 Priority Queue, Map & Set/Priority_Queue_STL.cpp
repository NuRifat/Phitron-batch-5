#include<bits/stdc++.h>
using namespace std;

int main(){
    priority_queue<int> pq;// for maximum priority queue
    //priority_queue<int, vector<int>, greater<int>> pq;// for minmum priority queue

    while(true){
        int a;
        cin >> a;
        if(a==0){
            int x;
            cin >> x;
            pq.push(x);
        }
        else if(a==1){
            pq.pop();
        }
        else if(a==2){
            cout << pq.top() << endl;
        }
        else break;
    }
    return 0;
}