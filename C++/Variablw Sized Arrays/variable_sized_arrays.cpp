#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//int main()
{
    int n;
    int q;

    cout <<" Enter a Number of Array ";
    cin >> n >> q;

    vector<int> a[n];

    for(int  i = 0; i<n; i++)
    {
        int m;
        cout << " Enter a size of array ";
        cin >>m;
        int o;

        for( int j=0; j<m; j++)
        {
            cin >> o;
            a[i].push_back(o);
        }
    }
    int r, s;
    for(int k=0; k<q; k++)
    {
        cout << "Enter a position ";
        cin >>r>>s;
        cout <<a[r][s]<< endl;
    }
    return 0;
}
