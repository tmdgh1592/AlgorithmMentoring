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

int n, m;
int arr[10'001];

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    
    cin >> n >> m;
    REP (i, 1, n) {
        cin >> arr[i];
    }
    
    int lo, hi, res, cur_sum;
    lo = hi = res = cur_sum = 0;

    while (true) {
        if (cur_sum >= m) {
            cur_sum -= arr[lo++];
        } 
        else if (hi == n) break;
        else cur_sum += arr[hi++];

        if (cur_sum == m) ++res;
    }

    cout << res;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
