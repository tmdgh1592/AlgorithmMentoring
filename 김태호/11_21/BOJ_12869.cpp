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

int cache[61][61][61];
int scv[3];
int n;

int f(int u, int v, int w) {
    if (u < 0) return f(0, v, w);
    if (v < 0) return f(u, 0, w);
    if (w < 0) return f(u, v, 0);

    if (!(u || v || w)) return 0;

    int& ret = cache[u][v][w];
    if (ret != -1) return ret;

    ret = INF;

    ret = min(ret, f(u - 9, v - 3, w - 1) + 1);
    ret = min(ret, f(u - 9, v - 1, w - 3) + 1);
    ret = min(ret, f(u - 3, v - 9, w - 1) + 1);
    ret = min(ret, f(u - 3, v - 1, w - 9) + 1);
    ret = min(ret, f(u - 1, v - 9, w - 3) + 1);
    ret = min(ret, f(u - 1, v - 3, w - 9) + 1);
    return ret;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    memset(cache, -1, sizeof(cache));

    rep(i, 0, n) cin >> scv[i];

    cout << f(scv[0], scv[1], scv[2]);

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
