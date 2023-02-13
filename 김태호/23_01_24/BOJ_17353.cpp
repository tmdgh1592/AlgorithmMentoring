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

const int MAX = int(1e5) + 1;

ll degree[MAX];
ll constant[MAX];
ll n, q;

void add(ll* tree, ll pos, ll val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}

ll sum(const ll* tree, ll pos) {
    ll ret = 0;
    while (pos > 0) {
        ret += tree[pos];
        pos &= (pos - 1);
    }
    return ret;
}

void range_add(ll lo, ll hi, ll val) {
    add(degree, lo, val);
    add(degree, hi + 1, -val);
    add(constant, lo, (-lo + 1) * val);
    add(constant, hi + 1, hi * val);
}

ll range_sum(ll lo, ll hi) {
    ll ret = sum(degree, hi) * hi + sum(constant, hi);
    return ret -= sum(degree, lo - 1) * (lo - 1) + sum(constant, lo - 1);
}



int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    REP (i, 1, n) {
        int tmp;
        cin >> tmp;
        range_add(i, i, tmp);
        range_add(i + 1, i + 1, -tmp);
    }

    cin >> q;
    rep (i, 0, q) {
        ll a, b, c;
        cin >> a;
        if (a & 1) {
            cin >> b >> c;
            range_add(b, c, 1);
            range_add(c + 1, c + 1, b - c - 1);
        } else {
            cin >> b;
            cout << range_sum(1, b) << endl;
        }
    }
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
