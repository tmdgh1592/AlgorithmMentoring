#include <bits/stdc++.h>
#define endl "\n"
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define mp make_pair

using namespace std;

#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;

int n, k;
ll satisfaction[100001];
ll dp[100001];

int solve(int idx) {
    if (idx > n) return 0;
    if (dp[idx] != -1) return dp[idx];
    
    int eat = 0;
    int total = 0;
    int lo = idx, hi = idx;
    int next = hi;
    while(lo <= hi && hi <= n) {
        total = satisfaction[hi] - satisfaction[lo - 1];
        if (total >= k) {
            eat = total - k;
            break;
        } else { 
            hi++;
            next++;
        }
    }

    int result = max(solve(idx + 1), eat + solve(next + 1));
    return dp[idx] = result;
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

cin >> n >> k;

REP(i, 1, n) {
    cin >> satisfaction[i];
    satisfaction[i] += satisfaction[i-1];
}
memset(dp, -1, sizeof(dp));

int answer = solve(1);
cout << answer << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}