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

int n, m;
vector<int> vec;

bool check(int height) {
    long long int total = 0;
    for(auto tree_height : vec) {
        if(tree_height > height) {
            total += (tree_height - height);
        }
    }
    return total >= m;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    vec = vector<int>(n);
    for(auto& e : vec) cin >> e;

    int lo = 0;
    int hi = *max_element(vec.begin(), vec.end());

    while(lo <= hi) {
        int mid = (lo + hi) / 2;
        if (check(mid)) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }    

    cout << hi;

    return 0;
}