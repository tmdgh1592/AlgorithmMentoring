#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
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

const int MAX = 500000;
ll tree[MAX + 1];
int n, m;

ll sum(int pos) {
    int ret;
    while(pos > 0) {
        ret += tree[pos];
        pos -= (pos & -pos);
    }
    return ret;
}

void add(int pos, int val) {
    while(pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    REP(l, 1, n) {
        ll tmp;
        cin >> tmp;
        add(l, tmp);
    }

    cin >> m;
    rep(b, 0, m) {
        int query, i, j, k;
        cin >> query;
        if(query == 1) {
            cin >> i >> j >> k;
            REP(a, i, j) {
                add(a, k);
            }
        } else {
            int x; //?
            cin >> x;
            cout << sum(x) - sum(x-1) << endl;
        }
    }

    return 0;
}