#include <bits/stdc++.h>
using namespace std;
void insert_heap(vector<int> &v, int x){
    v.push_back(x);
    int cur_idx = v.size()-1;
    while(cur_idx!=0){
        int par_idx = (cur_idx-1)/2;
        if(v[cur_idx]>v[par_idx]){
            swap(v[cur_idx],v[par_idx]);
        }
        else break;
        cur_idx = par_idx;
    }
}
void print_heap(vector<int> v){
    for(int val:v){
        cout << val << " " ;
    }
    cout << endl;
}
void delete_heap(vector<int> &v){
    v[0] = v[v.size()-1];
    v.pop_back();
    int cur_idx = 0;
    while(true){
        int left_idx = cur_idx*2+1;
        int right_idx = cur_idx*2+2;
        int last_idx = v.size()-1;
        if(left_idx<=last_idx && right_idx<=last_idx){
            if(v[left_idx]>=v[right_idx] && v[left_idx]>v[cur_idx]){
                swap(v[cur_idx],v[left_idx]);
                cur_idx = left_idx;
            }
            else if(v[right_idx]>=v[left_idx] && v[right_idx]>v[cur_idx]){
                swap(v[cur_idx],v[right_idx]);
                cur_idx = right_idx;
            }
            else break;
        }
        else if(left_idx<=last_idx){
            if(v[left_idx]>=v[right_idx]){
                swap(v[cur_idx],v[left_idx]);
                cur_idx = left_idx;
            }
            else break;
        }
        else if(right_idx<=last_idx){
             if(v[right_idx]>=v[left_idx]){
                swap(v[cur_idx],v[right_idx]);
                cur_idx = right_idx;
            }
            else break;
        }
        else break;
    }
}

int main(){
    int n;
    cin >> n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int x;
        cin >> x;
        insert_heap(v,x);
    }
    print_heap(v);
    delete_heap(v);
    print_heap(v);
    delete_heap(v);
    print_heap(v);

    return 0;
}