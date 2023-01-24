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

struct MinRMQ{
    int rmq_size;
    vector<int> range_min;

    MinRMQ(const vector<int>& arr){
        rmq_size = arr.size();
        range_min.resize(rmq_size * 4); // 4를 곱하면 노드 모두 커버 가능
        init(arr, 0, rmq_size - 1, 1); //셍성자 호출시 모든 노드(0 ~ n - 1)를 초기화 해준다. 루트 노드는 1번부터 시작한다. (2곱하면 왼쪽 자식 나오므로)
    }

    //세그먼트 트리를 만드는 초기화 함수
    int init(const vector<int>& arr, int left, int right, int node){ 
        //1. 리프 노드인 경우
        if(left == right){ // 시작과 끝 범위가 같은 경우는 리프 노드인 경우 (ex. 2~2까지 등)
            return range_min[node] = arr[left];
        }
        //2. 리프 노드가 아닌 경우
        int mid = (left + right) >> 1; // 분할 정복하기 위해 mid 설정
        int left_min = init(arr, left, mid, node * 2); // 왼쪽 자식 노드를 루트로 설정
        int right_min = init(arr, mid + 1, right, node * 2 + 1); // 오른쪽 자식 노드를 루트로 설정
        return range_min[node] = min(left_min, right_min);
    }

    //최솟값을 찾는 쿼리
    int query(int left, int right, int node, int node_left, int node_right){ 
        //1. 노드의 범위가 원하는 범위 밖일 경우 (겹치지 않는 경우)
        if((right < node_left) || (left > node_right)) return INF; //최댓값을 return 함

        //2. 원하는 범위가 노드의 범위를 포함하는 경우
        if((left <= node_left) && (right >= node_right)) return range_min[node]; //루트를 return 하면 됨

        //3. 노드의 범위가 원하는 범위를 포함하는 경우
        //4. 노드의 범위와 원하는 범위가 약간 겹치는 경우
        int mid = (node_left + node_right) >> 1;
        return min(query(left, right, node * 2, node_left, mid), query(left, right, node * 2 + 1, mid + 1, node_right));
    }
    int query(int left, int right){ // 원하는 범위만 입력했을 때 정상작동하도록 오버로딩
        return query(left, right, 1, 0, rmq_size - 1);
    }

    //값이 바뀌었을때 사용
    //index: 바꿀 위치 value: 바꿀 값
    int update(int index, int value, int node, int node_left, int node_right){
        //1. 바꿀 인덱스가 노드의 범위 밖일 경우
        if((index < node_left) || (index > node_right)) return range_min[node];

        if(node_left == node_right) return range_min[node] = value;

        int mid = (node_left + node_right) >> 1;
        return min(update(index, value, node * 2, node_left, mid), update(index, value, node * 2 + 1, mid + 1, node_right));
    }
    int update(int index, int value){
        return update(index, value, 1, 0, rmq_size - 1);
    }

};


struct MaxRMQ{
    int rmq_size;
    vector<int> range_max;

    MaxRMQ(const vector<int>& arr){
        rmq_size = arr.size();
        range_max.resize(rmq_size * 4); // 4를 곱하면 노드 모두 커버 가능
        init(arr, 0, rmq_size - 1, 1); //셍성자 호출시 모든 노드(0 ~ n - 1)를 초기화 해준다. 루트 노드는 1번부터 시작한다. (2곱하면 왼쪽 자식 나오므로)
    }

    //세그먼트 트리를 만드는 초기화 함수
    int init(const vector<int>& arr, int left, int right, int node){ 
        //1. 리프 노드인 경우
        if(left == right){ // 시작과 끝 범위가 같은 경우는 리프 노드인 경우 (ex. 2~2까지 등)
            return range_max[node] = arr[left];
        }
        //2. 리프 노드가 아닌 경우
        int mid = (left + right) >> 1; // 분할 정복하기 위해 mid 설정
        int left_max = init(arr, left, mid, node * 2); // 왼쪽 자식 노드를 루트로 설정
        int right_max = init(arr, mid + 1, right, node * 2 + 1); // 오른쪽 자식 노드를 루트로 설정
        return range_max[node] = max(left_max, right_max);
    }

    //최댓값을 찾는 쿼리
    int query(int left, int right, int node, int node_left, int node_right){ 
        //1. 노드의 범위가 원하는 범위 밖일 경우 (겹치지 않는 경우)
        if((right < node_left) || (left > node_right)) return -INF; //최솟값을 return 함

        //2. 원하는 범위가 노드의 범위를 포함하는 경우
        if((left <= node_left) && (right >= node_right)) return range_max[node]; //루트를 return 하면 됨

        //3. 노드의 범위가 원하는 범위를 포함하는 경우
        //4. 노드의 범위와 원하는 범위가 약간 겹치는 경우
        int mid = (node_left + node_right) >> 1;
        return max(query(left, right, node * 2, node_left, mid), query(left, right, node * 2 + 1, mid + 1, node_right));
    }
    int query(int left, int right){ // 원하는 범위만 입력했을 때 정상작동하도록 오버로딩
        return query(left, right, 1, 0, rmq_size - 1);
    }

    //값이 바뀌었을때 사용
    //index: 바꿀 위치 value: 바꿀 값
    int update(int index, int value, int node, int node_left, int node_right){
        //1. 바꿀 인덱스가 노드의 범위 밖일 경우
        if((index < node_left) || (index > node_right)) return range_max[node];

        if(node_left == node_right) return range_max[node] = value;

        int mid = (node_left + node_right) >> 1;
        return max(update(index, value, node * 2, node_left, mid), update(index, value, node * 2 + 1, mid + 1, node_right));
    }
    int update(int index, int value){
        return update(index, value, 1, 0, rmq_size - 1);
    }

};

int n, m;
vector<int> arr;

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif
    cin >> n >> m;
    arr.resize(n);
    for(auto& e: arr) cin >> e;
    
    MinRMQ minRMQ(arr);
    MaxRMQ maxRMQ(arr);
    int a, b;

    while(m--){
        cin >> a >> b;
        // cout << "a: " << a << ", b: " << b << endl;

        //arr 벡터는 0부터 시작하므로 1빼주어야 한다.
        int res_min = minRMQ.query(a - 1, b - 1);
        int res_max = maxRMQ.query(a - 1, b - 1);

        cout << res_min << ' ' << res_max << endl;

    }


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}