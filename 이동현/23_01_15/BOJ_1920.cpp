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
vector<int> vec1, vec2;


void check(int x){
    int lo = 0;
    int hi = n - 1;

    while(lo + 1 < hi){
        int mid = (lo + hi) >> 1;
        cout << "mid: " << vec1[mid] << endl;
        if(vec1[mid] == x){
            cout << "1" << endl;
            return;
        }

        if(vec1[mid] > x){
            hi = mid;
        }
        else{
            lo = mid;
        }
    }
    cout << "0" << endl;
    return;
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    vec1.resize(n);
    for(auto& element: vec1) cin >> element;
    sort(all(vec1));

    
    for(auto& element: vec1) cout <<" " << element;
    cout << endl;
    
    cin >> m;
    vec2.resize(m);

    int lo = vec1.front();
    int hi = vec1.back();

    for(auto& element: vec2) cin >> element;

    rep(i, 0, m){
        cout << "this: " << vec2[i] << endl;
        check(vec2[i]);
    }    


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}