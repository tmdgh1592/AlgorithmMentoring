#include <bits/stdc++.h>
#define endl "\n"
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()

using namespace std;

#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;

// 우선순위
// 1. 불린 횟수가 가장 적은 경우
// 2. 그 중에서 가장 낮은 가격
// 3. 같은 가격을 여러번 말했으면 먼저 말한 사람

static bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second < b.second;
}

int n, m;

map<int, int> price_call_count;
map<int, string> price_name;

string name;
int price = INF;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    price_call_count[INF] = INF;
    
    rep(i, 0, m) {
        string new_name;
        int new_price;
        cin >> new_name >> new_price;

        price_call_count[new_price] += 1;
        if (price_name[new_price] == "") {
            price_name[new_price] = new_name;
        }
    }
    
    vector<pair<int, int> > vec(all(price_call_count));
    sort(all(vec), cmp);

    int result_price = vec.front().first;
    cout << price_name[result_price] << " " << result_price;

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}