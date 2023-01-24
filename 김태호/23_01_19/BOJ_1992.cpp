#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n;
string s[64];
string res;

bool check(int y, int x, int div) {
    char ch = s[y][x];

    rep(i, 0, div) rep(j, 0, div) if (ch != s[y + i][x + j]) return false;
    return true;
}

void f(int y, int x, int exp) {
    if (exp == 1 || check(y, x, exp)) {
        res.pb(s[y][x]);
        return ;
    } 

    int div = exp >> 1;
    res.pb('(');

    rep (i, 0, 2) {
        rep (j, 0, 2) {
            f(y + i * div, x + j * div, div);
        }
    }
    res.pb(')');
    return ;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep (i, 0, n) cin >> s[i];
    f(0, 0, n);
    cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
