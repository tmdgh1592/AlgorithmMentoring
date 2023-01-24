#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
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

vector<string> words;
vector<int> alphas(26);


int main(){
    FAST;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    words = vector<string>(n);

    for(auto& e : words) cin >> e;
    for (auto& word : words) { // 단어 개수
        int weight = 1;

        for (int index = word.length() - 1; index >= 0; index--) { // 단어의 알파벳 만큼
            alphas[word[index] - 'A'] += weight;
            weight *= 10;
        }
    }

    int res = 0;
    int weight = 9;
    sort(all(alphas), greater<int>());
    for (auto& alpha : alphas) {
        if(alpha != 0) {
            res += alpha * weight;
            weight -= 1;
        }
    }

    cout << res;
    return 0;
}