#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define PIV (1 << 20) // 배열의 길이
using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
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

int n, m, k;
ll tree[PIV << 1];

void update(int pos, ll val) {
    pos |= PIV; // leaf node의 index
    tree[pos] = val;

    while (pos >>= 1) {
        tree[pos] = min(tree[pos << 1], tree[pos << 1 | 1]);
    }
}

ll query(int l, int r) {
    l |= PIV, r |= PIV; // leaf node의 index
    ll ret = LLONG_MAX;

    while (l <= r) { // l과 r이 교차할 때까지
        if (l & 1) { // l이 홀수이면
            ret = min(tree[l++], ret);
        }
        if (~r & 1) { // r이 짝수이면
            ret = min(tree[r--], ret);
        }
        l >>= 1, r >>= 1;
    }
    return ret;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;

    ll tt;
    REP (i, 1, n) {
        cin >> tt;
        update(i, tt);
    }
    
    while (m--) {
        ll a, b;
        cin >> a >> b;
        if (a > b) swap(a, b);
        cout << query(a, b) << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
