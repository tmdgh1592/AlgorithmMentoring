#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 1000000000
#define PIV (1 << 21)

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int n, m;
vector<int> arr, range_min, range_max;

ll min_init(const vector<int>& array, int l, int r, int node){

    if(l == r) return range_min[node] = array[l];
    int mid = (l + r) >> 1;

    return range_min[node] = min(min_init(array, l, mid, node * 2), min_init(array, mid + 1, r, node * 2 + 1));
    
}

ll max_init(const vector<int>& array, int l, int r, int node){
    if(l == r) return range_max[node] = array[l];
    int mid = (l + r) >> 1;
    return range_max[node] = max(max_init(array, l, mid, node * 2), max_init(array, mid + 1, r, node * 2 + 1));

}

ll min_query(int l, int r, int l_node, int r_node, int node){
    if(r < l_node || r_node < l) return INF;
    if(l <= l_node && r_node <= r) return range_min[node];

    int mid = (l_node + r_node) >> 1;
    return min(min_query(l, r, l_node, mid, node * 2), min_query(l, r, mid + 1, r_node, node * 2 + 1));
}

ll max_query(int l, int r, int l_node, int r_node, int node){
    if(l > r_node || r < l_node) return -INF;
    if(l <= l_node && r_node <= r) return range_max[node];

    int mid = (l_node + r_node) >> 1;
    return max(max_query(l, r, l_node, mid, node * 2), max_query(l, r, mid + 1, r_node, node * 2 + 1));
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("./input.txt", "r", stdin);
#endif

    cin >> n >> m;
    arr.resize(n);
    range_min.resize(PIV * 4);
    range_max.resize(PIV * 4);

    for(auto& e : arr) cin >> e;

    min_init(arr, 0, n - 1, 1);
    max_init(arr, 0, n - 1, 1);


    int u, v;
    rep(i, 0, m){
        if(u > v) swap(u, v);
        cin >> u >> v;
        cout << min_query(u - 1, v - 1, 0, n - 1, 1) << ' ' << max_query(u - 1, v - 1, 0, n - 1, 1) << endl;
    }


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}