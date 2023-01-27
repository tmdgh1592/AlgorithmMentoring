#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
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
vector<string> graph;

bool check(int size, int x, int y) {
    char start_val = graph[x][y];
    rep(i, x, x + size) rep(j, y, y + size) if (start_val != graph[i][j]) return false;
    return true;
}

void f(int size, int x, int y) {
    if (size == 1) {
        cout << graph[x][y];
        return;
    }
    if (check(size, x, y)) {
        cout << graph[x][y];
        return;
    }

    cout << '(';
    f(size / 2, x, y);
    f(size / 2, x, y + size / 2);
    f(size / 2, x + size / 2, y);
    f(size / 2, x + size / 2, y + size / 2);
    cout << ')';
}

int main() {
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    graph = vector<string>(n);
    for(auto& e : graph) cin >> e;
    f(n, 0, 0);

    return 0;
}