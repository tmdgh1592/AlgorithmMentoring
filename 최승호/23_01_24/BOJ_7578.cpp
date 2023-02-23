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

int MAX = 500000;
ll n, res;
ll tree[MAX + 1];
pii p[MAX + 1];

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
    REP(i, 1, n) cin >> p[i].first, p[i].second = i;
    sort(p + 1, p + n + 1);

    REP(i, 1, n) {
        
    }


    return 0;
}