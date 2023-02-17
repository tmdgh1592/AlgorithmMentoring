#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF 0x7f7f7f7f

using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
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

int v, e, k;
int dist[20001];
vector<pii> vec[20001];

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> v >> e >> k;
    memset(dist, 0x7f, sizeof(dist));
    rep (i, 0, e) {
        int a, b, c;
        cin >> a >> b >> c;
        vec[a].pb({b, c});
    }


    priority_queue<pii> pq;
    dist[k] = 0;
    pq.push({dist[k], k});

    while (!pq.empty()) {
        auto here_tmp = pq.top(); pq.pop();
        int here = here_tmp.second;
        int here_cost = -here_tmp.first;

        if (dist[here] < here_cost) continue;

        for (auto there_tmp : vec[here]) {
            int there = there_tmp.first;
            int there_cost = there_tmp.second;

            if (dist[here] + there_cost < dist[there]) {
                dist[there] = dist[here] + there_cost;
                pq.push({-dist[there], there});
            }
        }
    }

    REP (i, 1, v) {
        if (dist[i] == INF) cout << "INF";
        else cout << dist[i];
        cout << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
