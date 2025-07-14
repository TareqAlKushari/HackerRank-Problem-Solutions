#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

// Write your Student class here
class Student
{
    private:
    int grades[5];
    int total;
    public:
    void input()
    {
        int i=0;
        cout << "Enter the grades of student: " << i+1 << endl;
        for(i=0; i < 5; i++)
        {
            cin >> grades[i];
        }
    }
    int calculateTotalScore()
    {
        for(int i=0; i <5; i++)
        {
            total += grades[i];
        }
        return total;
    }
};

int main() {
    int n; // number of students
    cout << "Enter the number of students: " << endl;
    cin >> n;

    Student *s = new Student[n]; // an array of n students

    for(int i = 0; i < n; i++){
        s[i].input();
    }

    // calculate kristen's score
    int kristen_score = s[0].calculateTotalScore();

    // determine how many students scored higher than kristen
    int count = 0;
    for(int i = 1; i < n; i++){
        int total = s[i].calculateTotalScore();
        if(total > kristen_score){
            count++;
        }
    }

    // print result
    cout << "The students is has higher scored than kristen's\n: " << count << " Students " << endl;

    return 0;
}

