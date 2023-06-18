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

int n, m;
int parent[1001];
int result = 0;
vector<pair<int, pii> > edges;
vector<pii> tree[1001];


int findParent(int x) {
    if (x == parent[x]) return x;
    return parent[x] = findParent(parent[x]);
}

void unionParent(int a, int b) {
    a = findParent(a);
    b = findParent(b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int max_node = 0;
ll max_cost = -1;
bool visited[1001];


void dfs(int x, ll cost) {
    if(max_cost < cost) {
        max_cost = cost;
        max_node = x;
    }

    for (pii node : tree[x]) {
        int next = node.first;
        if (!visited[next]) {
            visited[next] = true;
            dfs(next, cost + node.second);
        }
    }
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

cin >> n >> m;

rep(i, 0, n) parent[i] = i;
rep(i, 0, m) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.pb(mp(c, mp(a, b)));
    
}
sort(all(edges));

rep(i, 0, m) {
    int cost = edges[i].first;
    int a = edges[i].second.first;
    int b = edges[i].second.second;

    if (findParent(a) != findParent(b)) {
        unionParent(a, b);
        result += cost;
        tree[a].pb(mp(b, cost));
        tree[b].pb(mp(a, cost));
    }
}

visited[0] = true;
dfs(0, 0);

max_cost = 0;
memset(visited, false, sizeof(visited));

visited[max_node] = true;
dfs(max_node, 0);

cout << result << endl << max_cost << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}