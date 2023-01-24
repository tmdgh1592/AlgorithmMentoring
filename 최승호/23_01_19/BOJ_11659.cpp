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

int n, m;
int vec[100000];
int sums[100000];

int interval_sum(int left, int right) {
    return sums[right] - sums[left - 1];
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;

    rep(i, 0, n) {
        cin >> vec[i];
        sums[i + 1] = sums[i] + vec[i];
    }

    rep(i, 0, m) {
        int left, right;
        cin >> left >> right;
        cout << interval_sum(left, right) << endl;
    }

    return 0;
}