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

constexpr int MAX = 1e6 + 1;

int n;
int cache[MAX];
int trace[MAX];

int f(int x) {
    if (x == 0) return INF;
    if (x == 1) return 0;

    int& ret = cache[x];
    if (ret != -1) return ret;
    ret = INF;

    if (x % 3 == 0 && (ret > f(x / 3) + 1)) {
        ret = f(x / 3) + 1;
        trace[x] = x / 3;
    }
    
    if (x % 2 == 0 && (ret > f(x / 2) + 1)) {
        ret = f(x / 2) + 1;
        trace[x] = x / 2;
    }
    
    if (ret > f(x - 1) + 1) {
        ret = f(x - 1) + 1;
        trace[x] = x - 1;
    }
    return ret;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    
    memset(cache, -1, sizeof(cache));
    cin >> n;
    cout << f(n) << endl;
    int temp = n;

    while (true) {
        if (temp == 1) {
            cout << 1 << endl;
            break;
        }
        cout << temp << ' ';
        temp = trace[temp];
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
