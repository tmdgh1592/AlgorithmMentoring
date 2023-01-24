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
int arr[1025][1025];
int sum[1025][1025];


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    REP(i, 1, n) REP(j, 1, n) cin >> arr[i][j];
    REP(i, 1, n) REP(j, 1, n) sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + arr[i][j];

    int x1, y1, x2, y2;
    rep(i, 0, m) {
        cin >> x1 >> y1 >> x2 >> y2;
        cout << sum[x2][y2] + sum[x1-1][y1-1] - sum[x1-1][y2] - sum[x2][y1-1] << endl;
    }

    return 0;
}