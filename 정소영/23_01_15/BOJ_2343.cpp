#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 987654321

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n, m;
vector<int> v;

bool check(int x){
    ll cnt, t;
    cnt = t = 0;
    rep(i, 0, n){
        if(t + v[i] > x) t = 0, ++cnt;
        if (v[i] > x) return false;
        t += v[i];
    }
    return cnt < m;
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif
    cin >> n >> m;
    v.resize(n);
    for(auto& e : v) cin >> e;


    ll lo = 0;
    ll hi = INF;

    while(lo + 1 < hi){
        ll mid = (lo + hi) >> 1;
        if(!check(mid)) lo = mid;
        else hi = mid;
    }
    cout << hi << endl;


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}