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

#define MAX 10000

int n, m;
int arr[MAX];

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif

    cin >> n >> m;
    rep(i, 0, n) cin >> arr[i];

    int lo, hi, sum, res;
    lo = hi = sum = res = 0;

    while(1){
        if(sum >= m) sum -= arr[lo++];
        else if(hi == n) break;
        else sum += arr[hi++];

        if(sum == m) ++res;
    }

    cout << res << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}