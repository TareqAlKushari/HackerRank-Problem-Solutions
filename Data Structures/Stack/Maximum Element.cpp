#include <bits/stdc++.h>
#include <string> 
const int MAX_SIZE = 10;
using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int top = -1;
vector<int> item(MAX_SIZE);

/*
 * Complete the 'getMax' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY operations as parameter.
 */
    
void push(int Element) {

    if(top >= MAX_SIZE - 1) {
        cout << "Stack full on push" << endl;
    }
    else {
        item[++top] = Element;
    }
}

void pop() {
    if(top <= -1) {
        cout << "Stack empty on pop: " << endl;
    }
    else {
        top--;
    }
}

vector<int> print() {
    return item;
}

vector<int> getMax(vector<string> operations) {
    for(string str : operations) {
        //string start = str.at(0);
        int spec = str.find(" ");
        string queries = str.substr((spec + 1), str.size());
        
        if(str.at(0) == '1'){
            push(stoi(queries));
        }
        else if(str.at(0) == '2'){
            pop();
        }
        else if(str.at(0) == '3'){
            return item;
        }
    }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<string> ops(n);

    for (int i = 0; i < n; i++) {
        string ops_item;
        getline(cin, ops_item);

        ops[i] = ops_item;
    }

    vector<int> res = getMax(ops);

    for (size_t i = 0; i < res.size(); i++) {
        fout << res[i];

        if (i != res.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
