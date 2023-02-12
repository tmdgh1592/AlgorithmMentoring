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

/*
최하위 원소 구하기
lsb = set & -set
최소 원소 지우기
set &= set - 1 
*/

const int MAX = 1000001;
int n;
ll res;
int tree[MAX + 1];
vector<int> vec;
void add(int idx, int val){
    //펜윅 트리의 경우 값이 변경될때 최 하위 비트에 1을 더한 값에 변경할 값을 더해 주면 된다.
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

    cin >> n;
    vec.resize(n);
    for(auto& e : vec) cin >> e;

    //펜윅트리에 하나씩 넣을 것이다.
    rep(i, 0, n){
        //자신보다 큰 갯수가 몇개인지 더해주면 된다.
        res += (sum(n) - sum(vec[i]));
        add(vec[i], 1); //idx도 1 증가시킨다.
    }

    cout << res;



#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
