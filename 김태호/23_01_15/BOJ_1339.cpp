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
vector<string> vec;
vector<int> alpha(26);

int power(int val, int exp) {
	if (exp == 0) return 1;
	if (exp == 1) return val;
	
	if (exp % 2 == 0) {
		int ret = power(val, exp / 2);
		return ret * ret;
	}
	
	return power(val, exp - 1) * val;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

	cin >> n;
	vec = vector<string>(n);
	
	for(auto& e : vec) cin >> e;
    
	for(const auto& e : vec) {
		auto len = e.length();
		rep(i, 0, len) {
			alpha[e[i] - 'A'] += power(10, len - i - 1);
		}
	}
	
	sort(all(alpha), greater<>());
	
	int res = 0;
	
	for(auto i = 0; i < 10; ++i) {
		res += alpha[i] * (9 - i);
	}
	
	cout << res;
	
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}


// #include <bits/stdc++.h>
// #define FAST ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL)
// #define endl "\n"
// #define rep(i, a, b) for(auto i = a; i < b; ++i)
// #define REP(i, a, b) for(auto i = a; i <= b; ++i)
// #define pii pair<int, int>
// #define all(v) (v).begin(), (v).end()
// #define pb push_back
// #define INF 987654321

// using namespace std;
// typedef long long ll;
// typedef unsigned long long ull;

// int n, res;
// vector<string> vec;
// vector<char> alpha;
// int arr[26];

// int power(int val, int exp) {
// 	if (exp == 0) return 1;
// 	if (exp == 1) return val;
	
// 	if (exp % 2 == 0) {
// 		int ret = power(val, exp / 2);
// 		return ret * ret;
// 	}
	
// 	return power(val, exp - 1) * val;
// }

// int calc() {
//     int ret = 0;

//     for (const auto& e : vec) {
//         int size = e.length() - 1;

//         rep(i, 0, e.length()) {
//             ret += arr[e[i] - 'A'] * power(10, size--);
//         }
//     }

//     return ret;
// }

// int main(){
//     FAST;
// #ifndef ONLINE_JUDGE
//     clock_t start = clock();
//     freopen("input.txt", "r", stdin);
// #endif

//     int n;
//     cin >> n;
//     vec.resize(n);

//     for (auto& e : vec) cin >> e;
//     for (const auto& e : vec) {
//         for (const auto& c : e) {
//             alpha.pb(c);
//         }
//     }

//     sort(all(alpha));
//     alpha.erase(unique(all(alpha)), alpha.end());

//     do {
//         int num = 9;

//         for (const auto& e : alpha) {
//             arr[e - 'A'] = num--;
//         }

//         res = max(res, calc());

//     } while (next_permutation(all(alpha)));

//     cout << res;

// #ifndef ONLINE_JUDGE
//     cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
// #endif
//     return 0;
// }
