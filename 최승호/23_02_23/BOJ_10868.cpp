#include <bits/stdc++.h>
#define endl "\n"
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define PIV 1 << 20

using namespace std;

#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;

int n, k;
ll tree[PIV << 1];

void update(int pos, ll val) {
    pos += PIV;
    tree[pos] = val;
    while(pos >>= 1) {
        tree[pos] = min(tree[pos << 1], tree[(pos << 1) + 1]);
    }
}

ll query(int l, int r) {
    l += PIV, r += PIV;
    ll ret = 1000000001;

    while(l <= r) {
        if (l & 1) {
            ret = min(ret, tree[l++]);
        }
        if (~r & 1) {
            ret = min(ret, tree[r--]);
        }
        l >>= 1, r >>= 1;
    }
    return ret;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> k;
    ll t;

    REP(i, 1, n) {
        cin >> t;
        update(i, t);
    }

    int l, r;
    while(k--) {
        cin >> l >> r;
        if (l > r) swap(l, r);
        cout << query(l, r) << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}