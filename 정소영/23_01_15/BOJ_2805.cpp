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
int arr[1 << 20];

bool check(int h){
    ll res = 0;
    rep(i, 0, n) res += arr[i] >= h ? arr[i] - h : 0;
    return res >= m;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif
    
    cin >> n >> m;

    int mx;
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
        mx = max(mx, arr[i]);
    }

    int lo = 0, hi = mx;
    int res, mid;

    while(lo + 1 < hi){
        mid = (lo + hi) >> 1;
        if(check(mid) == check(lo)) lo = mid;
        else hi = mid;
    }

    cout << lo << endl;




#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}