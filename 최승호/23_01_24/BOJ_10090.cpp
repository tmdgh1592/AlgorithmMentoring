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

const int MAX = 4000000;
ll tree[MAX + 1];
ll n, res;
vector<ll> src;
vector<ll> dest;

ll sum(int pos) {
    ll ret = 0;
    while(pos > 0) {
        ret += tree[pos];
        pos -= (pos & -pos);
    }
    return ret;
}

void add(int pos, ll val) {
    while(pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}

int get_idx(int val) {
    return lower_bound(all(dest), val) - dest.begin() + 1;
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    src.resize(n);
    for(auto& e : src) cin >> e;

    dest = src;
    sort(all(dest)); // 좌표 압축한 값을 정렬
    dest.erase(unique(all(dest)), dest.end()); // unique := 중복된 값을 벡터의 뒤로 미루고, 미룬 값의 시작점을 반환함

    rep(i, 0, n) {
        int idx = get_idx(src[i]);
        res += sum(n) - sum(idx);
        add(idx, 1);
    }

    cout << res;
    return 0;
}