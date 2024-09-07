#include<bits/stdc++.h>
using namespace std;

int main(){
    map<string,int> mp;
    mp.insert({"Rifat",100});
    mp.insert({"Shamim",200});
    mp.insert({"Arif",300});
    mp["Rifat"] = 150;
    mp["Sakib"] = 200;

    for(auto it=mp.begin(); it!=mp.end(); it++){
        cout << it->first << " " << it->second << endl;
    }
    if(mp.count("Sakib")){
        cout << "Asee" << endl;
    }
    else cout << "Naaaai" << endl;
    return 0;
}