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
vector<pii> adj[10001];
int s, d;


bool f(int node, int weight) {
    queue<int> q;
    bool visited[10001];
    memset(visited, false, sizeof(visited));
    q.push(node);

    while(!q.empty()) {
        auto cur = q.front();
        q.pop();
        
        if (cur == d) return true;
        if (visited[cur]) continue;
        visited[cur] = true;

        for (auto i = 0; i < adj[cur].size(); i++) {
            auto next = adj[cur][i].first;
            auto cost = adj[cur][i].second;
            if (cost < weight) continue;

            q.push(next);
        }
    }
    return false;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

cin >> n >> m;
for (auto i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    adj[a].pb(mp(b, c));
    adj[b].pb(mp(a, c));
}
cin >> s >> d;

int l = 1, r = 1000000000;
int mid;
while(l <= r) {
    mid = (l + r) / 2;

    if (f(s, mid)) {
        l = mid + 1;
    } else {
        r = mid - 1;
    }
}

cout << r;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}