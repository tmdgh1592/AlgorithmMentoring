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

const int MAX = 500001;
int n;
int tree[MAX + 1];
ll res;
vector<pair<int, int>> vec1;
vector<int> vec2;

void add(int idx, int val){
    while(idx < MAX){
        tree[idx] += val;
        idx += (idx & -idx);
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

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    rep(i, 0, n){
        int temp;
        cin >> temp;
        vec1.pb(pair<int, int> (temp, i + 1));
    }
    sort(all(vec1));
    vec2.resize(n);
    
    rep(i, 0, n){
        int temp;
        cin >> temp;
        
    }


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
