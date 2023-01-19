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

bool check(int limit) {
    long long int total = 0;
    int count = 1;
    for(auto size : vec) {
        if(size > limit) return false;
        total += size;
        if(total > limit) {
            count += 1;
            total = size;
        }
    }
    return count <= m;
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
    int hi = accumulate(vec.begin(), vec.end(), 0);

    while(lo <= hi) {
        int mid = (lo + hi) / 2; // 블루레이 하나의 크기
        if(check(mid)) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }

    cout << lo;

    return 0;
}