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


const int MAX = 555'555;
ll n, val, res;
ll tree[MAX + 1];
vector<ll> coord;
vector<ll> src;

ll sum(int pos) {
    ll ret = 0;

    while (pos > 0) {
        ret += tree[pos];
        pos &= (pos - 1);
    }
    return ret;
}

void add(int pos, int value) {
    while (pos < MAX - 5) {
        tree[pos] += value;
        pos += (pos & -pos);
    }
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;

    coord.resize(n);
    for(auto& e : coord) cin >> e;
    src = coord;
    sort(all(coord));
    coord.erase(unique(all(coord)), coord.end());

    rep (i, 0, n) {
        int idx = lower_bound(all(coord), src[i]) - coord.begin() + 1;
        res += sum(n) - sum(idx);
        add(idx, 1);
    }

    cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
