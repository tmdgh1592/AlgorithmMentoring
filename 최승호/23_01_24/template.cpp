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

const int MAX = 1'000'000;
ll n;
ll tree[MAX + 1];

ll sum(int pos) {
    ll ret = 0;
    while(pos > 0) {
        ret += tree[pos];
        pos -= pos & -pos;
    }
    return ret;
}

ll update(int pos, ll val) {
    
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif



    return 0;
}