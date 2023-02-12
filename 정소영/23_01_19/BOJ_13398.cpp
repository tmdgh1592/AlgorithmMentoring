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

#define MAX 100001

int n, m;
int arr[MAX];
int l[MAX], r[MAX];

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif

    cin >> n;
    rep(i, 0, n) cin >> arr[i];

    l[0] = arr[0], r[0] = arr[n - 1];
    int res = l[0];

    if(n == 1) cout << arr[n - 1] << endl;

    rep(i, 1, n) 
        l[i] = max(arr[i], l[i - 1] + arr[i]), res = max(l[i], res);
    
    for(int i = n; i >= 0; i--){
        r[i] = max(arr[i], r[i + 1] + arr[i]);
    }
    
    rep(i, 1, n) res = max(res, l[i - 1] + r[i + 1]);

    cout << res << endl;
    




#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}