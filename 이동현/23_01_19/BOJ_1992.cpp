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
int arr[64][64];


void check(int y, int x, int size){
    bool flag = true;
    rep(i, y, y + size){
        rep(j, x, x + size){
            if(arr[i][j] != arr[y][x]){
                flag = false;
                break;
            }
        }
        if(!flag) break;
    }

    if(flag){
        cout << arr[y][x];
    }
    else{
        cout << "(";
        check(y, x, size >> 1);
        check(y, x + (size >> 1), size >> 1);
        check(y + (size >> 1), x, size >> 1);
        check(y + (size >> 1), x + (size >> 1), size >> 1);
        cout << ")";
        return;
    }
}


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    string temp;
    
    rep(i, 0, n){
        cin >> temp;
        rep(j, 0, n){
            arr[i][j] = temp[j] - '0';
        }
    }
    check(0, 0, n);
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
