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

int n, m;
vector<int> heights;


bool check(int x){
    int wood_length = 0;
    rep(i, 0, n){
        if(heights[i] > x){
            // cout << heights[i] - x << endl;
            wood_length += heights[i] - x;
        }
    }
    // cout << "wood length " << wood_length << endl;
    return wood_length >= m;
    }


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    heights.resize(n);

    for(auto& height: heights)
        cin >> height;

    int lo = 0;
    int hi = INF;

    while(lo + 1 < hi){
        
        int mid = (lo + hi) >> 1;
        if(!check(mid)){
            hi = mid;
        }
        else{
            lo = mid;
       }
    }
    
    cout << lo << endl;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}