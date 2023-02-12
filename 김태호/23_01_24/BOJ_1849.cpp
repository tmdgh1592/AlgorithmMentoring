#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

const int MAX = 100'001;

int n;
int tree[MAX + 1];
vector<int> res;

void add(int pos, int val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}

ll sum(int pos) {
    ll ret = 0;
    
    while (pos > 0) {
        ret += tree[pos];
        pos &= (pos - 1);
    }
    return ret;
}

// F F F ... T T
bool check(int x, int val) {
    return sum(x) >= val;
}

int search(int val) {
    int s = 0;
    int pos = 0;

    for (auto i = (int)log2(MAX); i >= 0; --i) {
        if (pos + (1 << i) < MAX && s + tree[pos + (1 << i)] < val) {
            s += tree[pos + (1 << i)];
            pos += (1 << i);
        }
    }
    return pos + 1;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    int tmp;
    res.resize(n + 1);

    REP (i, 1, n) add(i, 1);

    REP (i, 1, n) {
        cin >> tmp;
        int idx = search(tmp + 1);
        add(idx, -1);
        res[idx] = i;
    }

    REP (i, 1, n) cout << res[i] << endl;


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
