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

int n;
vector<int> vec;
int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    vec = vector<int>(n);
    for(auto& e : vec) cin >> e;

    int l = 0;
    int r = n - 1;
    int res_l = vec[l];
    int res_r = vec[r];
    
    while(l < r) {
        int interval_sum = vec[l] + vec[r];
        if (abs(interval_sum) < abs(res_l + res_r)) {
            res_l = vec[l];
            res_r = vec[r];
        }

        if (interval_sum > 0) {
            r--;
        } else {
            l++;
        }
    }
    cout << res_l << " " << res_r;

    return 0;
}