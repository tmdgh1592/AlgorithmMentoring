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

ll n, m;
ll arr[10001];

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    REP(i, 1, n){
        cin >> arr[i];
    }

    int lo, hi ,res;
    ll cur_sum;
    lo = hi = 1;
    cur_sum = res = 0;
    
    while(true){
        if(cur_sum >= m){ // 현재 합이 주어진 값보다 크거나 같을 경우
            cur_sum -= arr[lo++]; // arr[lo]값을 빼주어 현재 합을 감소 시키고 Lo를 증가 시킨다.
        }
        else if(hi == n + 1){ // 만약 hi가 끝에 다다랐다면 더 이상 증가 시키면 안된다.
            break;
        }
        else{
            cur_sum += arr[hi++]; //cur_sum이 주어진 값보다 작고, hi 값이 끝에 다다르지 않았다면, cur_sum을 증가 시키기 위해 arr[hi]값을 더해주고 hi를 증가시킨다.
        }
        if(cur_sum == m){
            res++; //조건에 맞다면 결과값을 증가시킨다.
        }
       
    }

    cout << res;


    //code


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}