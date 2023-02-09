#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 987654321

using namespace std;
typedef long long ll;
typedef unsigned long long ull;


string str[64];

void f(int n, int y, int x){
    
    int mid = n >> 1;
    rep(i, y, y + n)
        rep(j, x, x + n)
            if(str[i][j] != str[y][x])
            {
                cout << '(';
                f(mid, y, x);
                f(mid, y, x + mid);
                f(mid, y + mid, x);
                f(mid, y + mid, x + mid);
                cout << ')';
                return;
            }
        
    
    cout << str[y][x];
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif
    int n;
    cin >> n;
    rep(i, 0, n)
        cin >> str[i];


    f(n, 0, 0);



#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}