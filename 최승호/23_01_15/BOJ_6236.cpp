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

bool check(int withdraw) {
    int count = 0;
    int remained = 0;

    for(auto required : vec) {
        if(required > withdraw) {
            return false;
        }
        if(remained < required) {
            count += 1;
            remained = withdraw;
        }
        remained -= required;
    }
    return count <= m;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    vec = vector<int>(n);
    for(auto& e : vec) cin >> e;

    int lo = *max_element(vec.begin(), vec.end());
    int hi = 1000000000;

    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if(check(mid)) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    
    cout << lo;

    return 0;
}