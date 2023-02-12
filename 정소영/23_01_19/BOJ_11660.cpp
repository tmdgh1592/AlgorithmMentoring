#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)

using namespace std;

#define MAX 1025

int n, m;
int dp[MAX][MAX]; //dp[x2][y2] = dp[x2][y1 - 1] - dp[x1 - 1][y2] - dp[x1 - 1][y1 - 1]
int arr[MAX][MAX];

int main(){
    FAST;

    cin >> n >> m;
    REP(i, 1, n){
        REP(j, 1, n){
            cin >> arr[i][j];
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j];
        }
    }

    int x1, x2, y1, y2;
    rep(i, 0, m){
        cin >> x1 >> y1 >> x2 >> y2;
        int res = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1];
        cout << res << endl;

    }

    return 0;
}