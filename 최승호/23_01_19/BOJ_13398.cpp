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
int arr[100001];
int cache[100001][2];


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    for(auto& e : arr) cin >> e;

    cache[0][0] = cache[0][1] = arr[0];
    int res = arr[0];
    for(int i = 1; i < n; i++) {
        cache[i][0] = cache[i][1] = arr[i];
        cache[i][0] = max(cache[i][0], cache[i-1][0] + arr[i]);
        cache[i][1] = max(cache[i-1][0], cache[i-1][1] + arr[i]);
        res = max(max(res, cache[i][0]), cache[i][1]);
    }

    cout << res;
    return 0;
}