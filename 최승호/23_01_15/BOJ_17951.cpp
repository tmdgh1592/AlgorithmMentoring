#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
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
typedef long long int lli;

int n, k, lo, hi;
vector<int> vec;

bool check(int max_score) {
    int cnt, total;
    cnt = total = 0;

    for(auto e : vec) {
        total += e;
        if (total >= max_score) {
            cnt += 1;
            total = 0;
        }
    }

    return cnt >= k;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> k;
    vec = vector<int>(n);

    for(auto& e : vec) cin >> e;
    lo = 0;
    hi = accumulate(vec.begin(), vec.end(), 0);

    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if(check(mid)) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    
    cout << hi;

    return 0;
}