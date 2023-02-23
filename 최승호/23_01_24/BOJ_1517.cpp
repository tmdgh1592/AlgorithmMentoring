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

const int MAX = 500000;
ll n, res;
ll tree[MAX + 1];
vector<ll> src;
vector<ll> dest; // src의 유니크한 값

ll sum(int pos) {
    ll ret = 0;
    while (pos > 0) {
        ret += tree[pos];
        pos -= (pos & -pos);
    }
    return ret;
}

void add(int pos, ll val) {
    while (pos < MAX) {
        tree[pos] += val;
        pos += (pos & -pos);
    }
}

int get_idx(int val) { // 좌표 압축 := val -> idx로 압축
    // 1 더해주는 이유 : 펜윅 트리는 인덱스 1부터 시작하기 때문에
    return lower_bound(all(dest), val) - dest.begin() + 1; // 값이 처음 등장하는 주소 - 배열의 시작 주소 => 내 앞에 몇개가 있는지
}


// inversion 문제
// i < j, arr[i] > arr[j] 경우의 수 구하는 문제
// ex) i=1, j=2; arr = {1, 3, 2} -> 1개

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    src.resize(n);
    for(auto& e : src) cin >> e;
    dest = src;

    sort(all(dest)); // 좌표 압축한 값을 정렬
    dest.erase(unique(all(dest)), dest.end()); // unique := 중복된 값을 벡터의 뒤로 미루고, 미룬 값의 시작점을 반환함

    rep(i, 0, n) {
        int idx = get_idx(src[i]); // 좌표 압축 src[i] -> idx로 변환 (진짜 값이 필요한게 아니라 '값의 비교'만 하기 때문에 압축해도 ㄱㅊ)
        res += sum(n) - sum(idx); // 지금까지(i이전) 입력된 값들 중, 나보다 큰 숫자가 몇개 있는지? := 스왑해야 하는 횟수
        add(idx, 1); // 압축된 idx 라는 값이 등장했음을 알려주기 위함
    }

    cout << res;
    return 0;
}