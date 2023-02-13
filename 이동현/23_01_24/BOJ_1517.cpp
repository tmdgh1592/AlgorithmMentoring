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
//질문 범위를 왜 500000를 안하고 555555를 하는지?
//add 함수에서 왜 while(idx < MAX) 가 아니고 while(idx < MAX - 5) 인지?


/*
최하위 원소 구하기
lsb = set & -set
최소 원소 지우기
set &= set - 1 
*/

const int MAX = 500005;
ll n, res;
ll tree[MAX + 1];
vector<ll> comp; // 좌표 압축 결과물
vector<ll> src; // 원래 입력받을 것



void add(int idx, int val){
    //펜윅 트리의 경우 값이 변경될때 최 하위 비트에 1을 더한 값에 변경할 값을 더해 주면 된다.
    while(idx < MAX){
        tree[idx] += val;
        idx += (idx & -idx);
    }
}

// ll sum(int idx){
//     //펜윅트리에서 구간합을 구하고 싶으면 매번 최하위 비트를 빼주며 더해주면 된다.
//     ll res;
//     while(idx > 0){
//         res += tree[idx];
//         idx &= (idx - 1);
//     }
//     return res;
// }


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
    comp.resize(n);
    for(auto& e : comp) cin >> e;
    src = comp;

    //좌표 압추 시작
    sort(all(comp));
    //중복이 시작되는 지점부터 끝까지 삭제하면 됨
    comp.erase(unique(all(comp)), comp.end()); //압축 완료

    //펜윅트리에 하나씩 넣을 것이다.
    rep(i, 0, n){
        //인덱스를 구하려면 lower_bound(시작, 끝, 값) - 배열/벡터의 시작. 현재 문제에서는 1번 인덱스부터 시작하므로 1을 더해준다.
        int idx = lower_bound(all(comp), src[i]) - comp.begin() + 1; 
        //자신보다 큰 갯수가 몇개인지 더해주면 된다.
        // cout<< "sum(n): " << sum(n) << endl;
        // cout<< "sum(idx): " << sum(idx) << endl;
        res += (sum(n) - sum(idx));
        add(idx, 1); //idx도 1 증가시킨다.
        // cout << "res : " << res <<endl;
        
    }

    cout << res;



#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
