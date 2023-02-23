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

int n;
vector<int> vec;


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;

    int val;
    rep(i, 0, n) {
        cin >> val;
        if(vec.empty() || val > vec.back()) {
            vec.pb(val);
            continue;
        }

        auto loc = lower_bound(all(vec), val);
        *loc = val;
    }

    cout << n - vec.size();

    return 0;
}