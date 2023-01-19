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

int n;
vector<ull> heights;

ull f(int left, int right) {
    if (left == right) return heights[left];

    int mid = left + right >> 1;
    ull ret = max(f(left, mid), f(mid + 1, right));

    int lo = mid, hi = mid + 1;
    ull min_height = min(heights[lo], heights[hi]);

    ret = max(ret, 2 * min_height);

    while (left < lo || hi < right) {
        
        if (hi < right && (lo == left || heights[lo - 1] < heights[hi + 1])) {
            min_height = min(min_height, heights[++hi]);
        } else {
            min_height = min(heights[--lo], min_height);
        }
        ret = max(ret, (hi - lo + 1) * min_height);
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
    heights.resize(n);
    for (auto& e : heights) cin >> e;

    cout << f(0, n - 1);

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
