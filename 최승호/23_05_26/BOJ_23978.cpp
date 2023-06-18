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

ll n, k;
int dates[1000001];

ll calc(ll n) {
    return n * (n + 1) / 2;
}

bool possible(ll mid) {
    ll sum = 0;
    ll cur;

    for (auto i = 0; i < n - 1; i++) {
        cur = mid;
        int gap = dates[i + 1] - dates[i];
        if (mid <= gap) sum += calc(mid);
        else sum += (calc(mid) - calc(mid - gap));
        
        if (sum >= k) return true;
    }
    
    sum += calc(mid);
    return sum >= k;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

cin >> n >> k;
for (auto i = 0; i < n; i++) cin >> dates[i];

ll l = 1, r = 1500000000;

while (l <= r) {
    ll mid = l + r >> 1;
    if (possible(mid)) { // mid원을 올려서 k원 이상 현금화 가능할 때
        r = mid - 1;
    } else {
        l = mid + 1;
    }
}

cout << l;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}