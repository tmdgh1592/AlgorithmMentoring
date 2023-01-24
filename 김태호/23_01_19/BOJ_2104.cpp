#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n;
vector<ull> vec;

ull f(int left, int right) {
    if (left == right) return vec[left] * vec[left];

    int mid = left + right >> 1;
    ull ret = max(f(left, mid), f(mid + 1, right));

    int lo = mid, hi = mid + 1;

    ull rhs = min(vec[lo], vec[hi]);
    ull cur_sum = vec[lo] + vec[hi];
    ret = max(ret, rhs * cur_sum);

    while (left < lo || hi < right) {
        if (hi < right && (lo == left || vec[lo - 1] < vec[hi + 1])) {
            rhs = min(rhs, vec[++hi]);
            cur_sum += vec[hi];
            ret = max(ret, rhs * cur_sum);
        } else {
            rhs = min(rhs, vec[--lo]);
            cur_sum += vec[lo];
            ret = max(ret, rhs * cur_sum);
        }
    }
    return ret;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    vec.resize(n);
    for (auto& e : vec) cin >> e;

    cout << f(0, n - 1);

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
