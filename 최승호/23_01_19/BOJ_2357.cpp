#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 1000000001

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n, m;
vector<int> input;
vector<int> min_seg;
vector<int> max_seg;


void init(int node, int s, int e) {
    if (s == e) {
        min_seg[node] = max_seg[node] = input[s];
        return;
    }
    init(node * 2, s, (s + e) / 2);
    init(node * 2 + 1, (s + e) / 2 + 1, e);
    min_seg[node] = min(min_seg[node * 2], min_seg[node * 2 + 1]);
    max_seg[node] = max(max_seg[node * 2], max_seg[node * 2 + 1]);
}

pair<int, int> query_min_max(int node, int s, int e, int l, int r) {
    if (l > e || r < s) {
        return make_pair(INF, -INF);
    }
    if (l <= s && e <= r) {
        return make_pair(min_seg[node], max_seg[node]);
    }
    pair<int, int> left, right;
    left = query_min_max(node * 2, s, (s + e) / 2, l, r);
    right = query_min_max(node * 2 + 1, (s + e) / 2 + 1, e, l, r);
    return make_pair(min(left.first, right.first), max(left.second, right.second));
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    input = vector<int>(n);
    min_seg = vector<int>(n * 4);
    max_seg = vector<int>(n * 4);

    for(auto& e : input) cin >> e;
    
    init(1, 0, n - 1);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        pair<int, int> min_max = query_min_max(1, 0, n - 1, a - 1, b - 1);
        cout << min_max.first << " " << min_max.second << endl;
    }

    return 0;
}