#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
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

//연속합이 최대가 되는 경우
//1. max(이전까지 결과 + 현재 값, 현재 값, 이전까지 결과에서 숫자 하나 뺀거 + 현재 값, 이전까지 결과 + 현재값 빼기) 
//dp[i][0] := i를 마지막으로 할때 최대 연속합, 숫자는 빼지 않음
//dp[i][1] := i를 마지막으로 할때 최대 연속합, 숫자를 1개 뺄 경우
//dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
//dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0])

int n, res;
int arr[100001];

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    
    rep(i, 0, n){
        cin >> arr[i];
    }

    int dp[n + 1][2];
    res = dp[0][0] = dp[0][1] = arr[0];

    rep(i, 1, n){
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0]);
        int temp = max(dp[i][0], dp[i][1]);
        res = max(res, temp);
    }
    cout << res;
    


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
