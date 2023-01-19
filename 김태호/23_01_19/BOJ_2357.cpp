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

struct RMQ {
    int n;
    vector<int> range_min;

    RMQ(const vector<int>& array) {
        n = array.size();
        range_min.resize(n * 4);
        init(array, 0, n - 1, 1);
    }

    int init(const vector<int>& array, int left, int right, int node) {
        if (left == right) return range_min[node] = array[left];

        int mid = left + right >> 1;
        int left_ret = init(array, left, mid, node * 2);
        int right_ret = init(array, mid + 1, right, node * 2 + 1);
        return range_min[node] = min(left_ret, right_ret);
    }

    int query(int left, int right, int node, int node_left, int node_right) {
        if (right < node_left || node_right < left) return INF;
        if (left <= node_left && node_right <= right) return range_min[node];

        int mid = node_left + node_right >> 1;
        return min(query(left, right, node * 2, node_left, mid), query(left, right, node * 2 + 1, mid + 1, node_right));
    }

    int query(int left, int right) {
        return query(left, right, 1, 0, n - 1);
    }

    int update(int index, int value, int node, int node_left, int node_right) {
        if (index < node_left || node_right < index) return range_min[node];
        if (node_left == node_right) return range_min[node] = value;

        int mid = node_left + node_right >> 1;
        return min(update(index, value, node * 2, node_left, mid), update(index, value, node * 2 + 1, mid + 1, node_right));
    }

    int update(int index, int value) {
        return update(index, value, 1, 0, n - 1);
    }
};

struct RMQ2 {
    int n;
    vector<int> range_max;

    RMQ2(const vector<int>& array) {
        n = array.size();
        range_max.resize(n * 4);
        init(array, 0, n - 1, 1);
    }

    int init(const vector<int>& array, int left, int right, int node) {
        if (left == right) return range_max[node] = array[left];

        int mid = left + right >> 1;
        int left_ret = init(array, left, mid, node * 2);
        int right_ret = init(array, mid + 1, right, node * 2 + 1);
        return range_max[node] = max(left_ret, right_ret);
    }

    int query(int left, int right, int node, int node_left, int node_right) {
        if (right < node_left || node_right < left) return -INF;
        if (left <= node_left && node_right <= right) return range_max[node];

        int mid = node_left + node_right >> 1;
        return max(query(left, right, node * 2, node_left, mid), query(left, right, node * 2 + 1, mid + 1, node_right));
    }

    int query(int left, int right) {
        return query(left, right, 1, 0, n - 1);
    }

    int update(int index, int value, int node, int node_left, int node_right) {
        if (index < node_left || node_right < index) return range_max[node];
        if (node_left == node_right) return range_max[node] = value;

        int mid = node_left + node_right >> 1;
        return max(update(index, value, node * 2, node_left, mid), update(index, value, node * 2 + 1, mid + 1, node_right));
    }

    int update(int index, int value) {
        return update(index, value, 1, 0, n - 1);
    }
};


int n, m;
vector<int> arr;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    int u, v;

    cin >> n >> m;
    arr.resize(n);
    for (auto& e : arr) cin >> e;

    RMQ rmq(arr);
    RMQ2 rmq2(arr);

    rep (i, 0, m) {
        if (u > v) swap(u, v);
        cin >> u >> v;
        cout << rmq.query(u - 1, v - 1) << ' ' << rmq2.query(u - 1, v - 1) << endl;
    }

#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
