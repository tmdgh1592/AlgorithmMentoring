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

const int MAX = 1000000;
vector<ll> tree;
vector<ll> comp;
//pos까지의 누적합을 구함

int n, val;
vector<int> vec;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    
    rep(i, 0, n){
        cin >> val;
        
        //만약 벡터가 비어 있거나, 벡터의 마지막 값이 주어진 값보다 작다면, 꼬임이 발생하지 않는다.
        if(vec.empty() || vec.back() < val){
            vec.pb(val);// 전선을 뒤에 꽂아줌
        }else{// 꼬임이 발생하는 경우
            auto it = lower_bound(all(vec), val);
            *it = val;
        }
        // 반복문이 끝나면 vec에는 꼬이지 않은 전선들만 남아 있음
    }
    
    cout << n - vec.size();

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
