#include <bits/stdc++.h>
#define endl "\n"
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define pii pair<int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define mp make_pair

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

int n;
vector<pii> vec;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

cin >> n;
vec.resize(n);
for (auto& [a, b] : vec) cin >> a >> b;
sort(all(vec));

priority_queue<pii, vector<pii>, greater<pii> > pq; // 싸지방 일찍 끝나는 시간에 따라 정렬 (끝나는 시간, 자리 번호)
int ans = 0;
int count[100001] = {0, };
set<int> s; // 싸지방 남은 자리 번호 저장


for(auto& [start, end] : vec) {
    while(!pq.empty() && pq.top().first <= start) {
        s.insert(pq.top().second);
        pq.pop();
    }
    
    if (s.empty()) { // 빈 자리가 없다면
        pq.push(mp(end, ans)); // 끝나는 시간과 싸지방 번호를 넣는다.
        count[ans++]++;
    } else { // 남는 자리가 있다면, 앞자리 부터
        auto idx = *s.begin();
        count[idx]++;
        pq.push(mp(end, idx));
        s.erase(s.begin());
    }
}

cout << ans << endl;
rep(i, 0, ans) cout << count[i] << " ";  


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}