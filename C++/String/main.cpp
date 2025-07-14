#include <sstream>
#include <vector>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstring>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    int s = 0, t = 0, e = 0;
    stringstream ss;

    //s = strlen(str);
    //char g[s];
    //strcpy_s(g, str);
    vector<int>x;
    ss << str << str << str;
    ss >> x[0] >> x[1] >> x[2];

    return x;
}

int main() {
    string str;
    cout << "Enter the string: " <<endl;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}
