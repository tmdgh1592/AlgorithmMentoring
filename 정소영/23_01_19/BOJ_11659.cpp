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


int arr[MAX];
int sum[MAX];
int n, m;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif

    cin >> n >> m;
    REP(i, 1, n) {
        cin >> arr[i];
        sum[i] = sum[i - 1] + arr[i];
    }

    REP(i, 1, m){
        int a, b;
        cin >> a >> b;
        int res = sum[b] - sum[a - 1];
        cout << res << endl;
    }



#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}