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

int n, res = -INF;
int arr[100'000];
int lo[100'000]; // i번째 수에서 끝나는 최대 연속합
int hi[100'000]; // i번째 수에서 시작하는 최대 연속합

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    rep (i, 0, n) cin >> arr[i];

    lo[0] = arr[0];
    hi[n - 1] = arr[n - 1];

    rep (i, 1, n) lo[i] = max(lo[i - 1] + arr[i], arr[i]);
    for (int i = n - 2; i >= 0; --i) hi[i] = max(hi[i + 1] + arr[i], arr[i]);

    res = *max_element(lo, lo + n);
    rep (i, 1, n - 1) res = max(res, lo[i - 1] + hi[i + 1]);

    cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
