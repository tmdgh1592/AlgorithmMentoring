#include <bits/stdc++.h>
#define endl "\n"
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()

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

int parent[10001];
string mw[10001];
vector<pair<int, pair<int, int> > > edges;
ll ret;
int v, e;

int find_parent(int x) {
    if(parent[x] == x) return x;
    return parent[x] = find_parent(parent[x]);
}

void union_parent(int a, int b) {
    a = find_parent(a);
    b = find_parent(b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> v >> e;
    for(int i = 1; i <= v; i++) {
        parent[i] = i;
    }

    for(int i = 1; i <= v; i++) {
        string man_or_woman;
        cin >> man_or_woman;
        mw[i] = man_or_woman;
    }
    
    for (int i = 0; i < e; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        edges.push_back(make_pair(cost, make_pair(a, b)));
    }

    sort(all(edges));

    int edges_count = 0;
    
    for (int i = 0; i < e; i++){
        int cost = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        if(mw[a] != mw[b]) {
            if(find_parent(a) != find_parent(b)) {  
                union_parent(a, b);
                ret += cost;
                edges_count += 1;
            }
        }
    }

    if (v - 1 != edges_count) ret = -1;
    cout << ret;
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}