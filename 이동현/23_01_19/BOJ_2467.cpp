#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
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
vector<int> vec;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    vec.resize(n);
    
    for(auto& e: vec) cin >> e;
    sort(all(vec));

    int lo, hi, cur_sum;
    int res[3];
    res[1] = lo = 0;
    res[2] = hi = n - 1;
    res[0] = cur_sum = vec[0] + vec[n - 1];
    // cout << cur_sum << endl;
    while(lo < hi){
        cur_sum = vec[lo] + vec[hi];

        if(abs(res[0]) > abs(cur_sum)){
            res[0] = cur_sum;
            res[1] = lo;
            res[2] = hi;
        }

        if(cur_sum > 0){
            hi--;
        }
        else if(cur_sum < 0){
            lo++;
        }
        else{
            break;
        }
    }

    cout << vec[res[1]] << ' ' << vec[res[2]];


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
