#include<bits/stdc++.h>
using namespace std;
class myQueue
{
public:
    list <int> v;
    void push(int val){
        v.push_back(val);
    }
    void pop(){
        v.pop_front();
    }
    int front(){
        return v.front();
    }
    int size(){
        return v.size();
    }
    bool empty(){
        if(v.size()==0) return true;
        else return false;
    }
};

int main(){
    myQueue q;
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        q.push(x);
    }
    while(!q.empty())
    {
        cout<< q.front() <<" ";
        q.pop();
    }
    return 0;
}

