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
int n, m;
int a, b, c, d;
ll tree[MAX];

void add(int pos, ll val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos |= (pos & -pos);
    }
}

ll sum(int pos) {
    ll ret = 0;
    while (pos > 0) {
        ret += tree[pos];
        pos &= (pos - 1);
    }

    return ret;
}

void range_add(int lo, int hi, ll val) {
    add(lo, val);
    add(hi + 1, -val);
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    ll tmp;
    cin >> n;
    REP (i, 1, n) {
        cin >> tmp;
        range_add(i, i, tmp);
    }
    cin >> m;

    while (m--) {
        cin >> a;
        if (a & 1) {
            cin >> b >> c >> d;
            range_add(b, c, d);
        } else {
            cin >> b;
            cout << sum(b) << endl;
        }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
