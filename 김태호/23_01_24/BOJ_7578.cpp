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

const int MAX = 500'001;
ll n, res;
ll tree[MAX];
pii p[MAX];

ll sum(int pos) {
    ll ret = 0;

    while (pos > 0) {
        ret += tree[pos];
        pos &= (pos - 1);
    }
    return ret;
}

void add(int pos, int val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    int tmp, idx;
    cin >> n;

    REP (i, 1, n) cin >> p[i].first, p[i].second = i;
    sort(p + 1, p + n + 1);

    REP (i, 1, n) {
        cin >> tmp;
        idx = lower_bound(p + 1, p + n + 1, make_pair(tmp, -INF))->second;
        res += idx - 1 - sum(idx - 1);
        add(idx, 1);
    }

    cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
