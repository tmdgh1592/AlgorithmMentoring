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

int n, m;
int a[MAX];

bool check(int temp){
    int lo = 0, hi = n - 1;
    int mid;
    //cout <<"temp "<< temp << endl;
    while(lo <= hi){
        mid = (lo + hi) >> 1;
        //cout << "a[mid] " << a[mid] << endl;
        if(a[mid] == temp) return true;
        else if (a[mid] > temp) hi = mid - 1;
        else if (a[mid] < temp) lo = mid + 1;
    }
    return false;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    rep(i, 0, n) cin >> a[i];
    sort(a, a + n);
    //rep(i, 0, n) cout << a[i] << endl;
    cin >> m;
    rep(i, 0, m){
        int temp;
        cin >> temp;

        if(check(temp)) cout << 1 << endl;
        else cout << 0 << endl;
    }


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}