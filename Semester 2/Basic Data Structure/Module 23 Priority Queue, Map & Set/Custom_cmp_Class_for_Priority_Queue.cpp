//this code will create a list of students based on priority, where students with the highest marks have the highest priority, and in the case of a tie in marks, the student with the lowest roll number will be prioritized:
#include<bits/stdc++.h>
using namespace std;

class Student{
public:
    string name;
    int roll;
    int marks;
    Student(string name, int roll, int marks){
        this->name = name;
        this->roll = roll;
        this->marks = marks;
    }
};

class cmp
{
public:
    bool operator()(Student a, Student b){
        if(a.marks < b.marks) return true; // When true is returned, the priority queue changes. So, we will return true where we want it to change.
        else if(a.marks > b.marks) return false;//  if false return then the priority queue will not change
        else {
            if(a.roll > b.roll) return true;
            else return false;
        }
    }
};

int main(){
    int n;
    cin>> n;
    priority_queue<Student, vector<Student>, cmp> pq;
    for(int i=0;i<n;i++){
        string name;
        int roll, marks;
        cin >> name >> roll >> marks;
        Student obj(name,roll,marks);
        pq.push(obj);
    }
    while(!pq.empty()){
        cout << pq.top().name <<" "<<pq.top().roll<<" "<<pq.top().marks << endl;
        pq.pop();
    }
    return 0;
}