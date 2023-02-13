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

const int MAX = 24 * 60 * 60 + 2;
int n, q;

ll degree[MAX];
ll constant[MAX];

void add(ll* tree, int pos, int val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}

ll sum(const ll* tree, int pos) {
    ll ret = 0;
    while (pos > 0) {
        ret += tree[pos];
        pos &= (pos - 1);
    }
    return ret;
}

void range_add(int lo, int hi, int val) {
    add(degree, lo, val);
    add(degree, hi + 1, -val);
    add(constant, lo, (-lo + 1) * val);
    add(constant, hi + 1, hi * val);
}

ll range_sum(int lo, int hi) {
    ll ret = sum(degree, hi) * hi + sum(constant, hi);
    return ret -= sum(degree, lo - 1) * (lo - 1) + sum(constant, lo - 1);
}

ll calc_time(string s) {
    ll ret = stoi(s.substr(0, 2)) * 3600 + stoi(s.substr(3, 2)) * 60 + stoi(s.substr(6, 2));
    return ret;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cout << fixed;
    cout.precision(10);
    cin >> n;
    string a, b;
    ll t1, t2, l;

    while (n--) {
        cin >> a >> b >> b;
        t1 = calc_time(a) + 1;
        t2 = calc_time(b) + 1;
        if (t1 > t2) {
            range_add(t1, 24 * 60 * 60, 1);
            range_add(1, t2, 1);
        } else {
            range_add(t1, t2, 1);
        }
    }
    cin >> n;
    while (n--) {
        cin >> a >> b >> b;
        t1 = calc_time(a) + 1;
        t2 = calc_time(b) + 1;
        ll ss = 0;
        if (t1 > t2) {
            ss += range_sum(t1, 86400);
            ss += range_sum(1, t2);
            l = 86401 - t1 + t2;
        } else {
            ss = range_sum(t1, t2);
            l = t2 - t1 + 1;
        }
        cout << (long double) ss / l << endl;

    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
