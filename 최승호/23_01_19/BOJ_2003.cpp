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

int n, m;
vector<int> vec;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    vec = vector<int>(n);
    for(auto& e : vec) cin >> e;
    
    int interval_sum = 0;
    int end = 0;
    int res = 0;

    for(int start = 0; start < n; start++) {
        while(interval_sum < m && end < n) interval_sum += vec[end++];
        if(interval_sum == m) res += 1;
        interval_sum -= vec[start];
    }

    cout << res;
    return 0;
}