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
vector<int> graph[2000001];
int color[2001];
int RED = 1, BLUE = 2;
bool flag = false;

void dfs(int node) {
    if(!color[node]) color[node] = RED;
    
    for(auto next : graph[node]) {
        if(color[node] == color[next]) {
            flag = true;
            return;
        }
        if(color[next]) continue;

        color[node] == RED ? color[next] = BLUE : color[next] = RED;
        dfs(next);
    }
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

cin >> n >> m;
int start_node = 0;
rep(i, 0, m){
    int u, v;
    start_node = u;
    cin >> u >> v;
    graph[u].pb(v);
    graph[v].pb(u);
}
dfs(start_node);
cout << !flag ? 0 : 1;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}