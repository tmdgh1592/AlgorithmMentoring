#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
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
int arr[100'000];
int lo, hi, candidate, sum = INF;
pii res;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep (i, 0, n) cin >> arr[i];
    lo = 0, hi = n - 1;

    while (lo < hi) {
        candidate = arr[lo] + arr[hi];
        
        if (abs(candidate) < sum) {
            sum = abs(candidate);
            res.first = arr[lo];
            res.second = arr[hi];

        }
        
        if (candidate < 0) ++lo;
        else --hi;
    }

    cout << res.first << ' ' << res.second;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
