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
int n, m, cnt;
int a, b;
ll tree[MAX];
ll money[MAX];
int s[MAX], e[MAX];
vector<int> adj[MAX];

void f(int here) {
    s[here] = ++cnt;
    for (auto there : adj[here]) f(there);
    e[here] = cnt;
    return;
}

void add(int pos, ll val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
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
    cin >> n >> m;
    cin >> tmp;
    money[1] = tmp;
    REP (i, 2, n) {
        cin >> money[i] >> tmp;
        adj[tmp].pb(i);
    }
    f(1);
    char ch;


    REP (i, 1, n) {
        range_add(s[i], s[i], money[i]);
    }

    while (m--) {
        cin >> ch;

        if (ch == 'p') {
            cin >> a >> b;
            range_add(s[a] + 1, e[a], b);
        } else {
            cin >> a;
            cout << sum(s[a]) << endl;
        }
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
