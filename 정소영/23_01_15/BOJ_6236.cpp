#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 987654321
#define MAX 100001
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
int n, m, total;
int a[MAX];

bool check(int mid){
    int cnt = 1;
    int temp = mid;

    rep(i, 0, n){
        if(mid < a[i]) return false;
        if(temp < a[i]){
            temp = mid;
            cnt++;
        }
        temp -= a[i];
    }

    return  cnt <= m;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    rep(i, 0, n) cin >> a[i], total += a[i];

    int lo = 1, hi = total;
    int res = 0;
    while(lo <= hi){
        int mid = (lo + hi) >> 1;
        if(!check(mid)) lo = mid + 1;
        else res = mid, hi = mid - 1;
    }
    cout << res << endl;


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}