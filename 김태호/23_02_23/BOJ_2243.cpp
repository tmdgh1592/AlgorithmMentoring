#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define PIV (1 << 20)
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

int n;
ll tree[PIV << 1];

void update(int pos, ll val) {
    pos |= PIV; // leaf node로 이동
    tree[pos] += val;

    while (pos >>= 1) { // leaf node에서 root까지 이동하며 internal node들을 모두 update
        tree[pos] = tree[pos << 1] + tree[pos << 1 | 1];
    }
}

ll query(ll k) {
    ll here = 1;

    while (here < PIV) { // here가 leaf가 아닐때까지
        ll left_child = here << 1;
        if (tree[left_child] >= k) { // kth element가 left subtree어딘가에 있다
            here = left_child;
        } else { // kth element가 right subtree어딘가에 있다
            k -= tree[left_child]; // left subtree의 연결을 끊음
            here = left_child | 1; // root node를 right child로 옮김
        }
    }
    return here - PIV;
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    int a, b, c;

    rep (i, 0, n) {
        cin >> a;
        if (a & 1) {
            cin >> b;
            int ppos = query(b);
            cout << ppos << endl;
            update(ppos, -1);

        } else {
            cin >> b >> c;
            update(b, c);
        }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
