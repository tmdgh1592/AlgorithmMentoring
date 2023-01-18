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

int k;
int arr[501];
int dp[501][501];
int cumulated[501];

int f(int u, int v) {
    int& ret = dp[u][v];

    if (ret != 0x3f3f3f3f) return ret;
    if (u == v) return ret = 0;
    if (u + 1 == v) return ret = arr[u] + arr[v];

    rep (mid, u, v) {
        int left = f(u, mid);
        int right = f(mid + 1, v);
        ret = min(ret, left + right);
    }

    return ret += cumulated[v] - cumulated[u - 1];
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    int t;
    cin >> t;
    while (t--) {
        memset(dp, 0x3f, sizeof(dp));
        cin >> k;
        
        REP (i, 1, k) {
            cin >> arr[i];
            cumulated[i] = cumulated[i - 1] + arr[i];
        }
        cout << f(1, k) << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
