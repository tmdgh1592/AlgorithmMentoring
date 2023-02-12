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
vector<ull> heights;

ull dq(int left, int right){ //왼쪽 시작과 오른쪽 시작을 입력 받는다.
    //1. left ~ mid 까지가 최대가 될때
    //2. mid ~ right 까지가 최대가 될때
    //3. mid 를 포함하여 왼쪽 오른쪽이 합쳐 최대가 될때

    if(left == right){ //밑변길이가 1인 경우 더 자를 필요 없음
        return heights[left];
    }
    int mid = (left + right) >> 1;
    //1번과 2번 경우: mid를 중심으로 왼쪽, 오른쪽 탐색
    ull res = max(dq(left, mid), dq(mid + 1, right));
    
    int lo = mid;
    int hi = mid + 1;
    ull min_height = min(heights[lo], heights[hi]);
    res = max(res, 2 * min_height);

    while (left < lo || hi < right) {
        //다음과 같은 경우 오른쪽으로 이동한다.
        //현재 오른쪽으로 이동할 수 있는 상태에서
        //  1) 왼쪽으로 이동할 수 없거나
        //  2) 왼쪽으로 이동한 높이보다 오른쪽으로 이동한 높이가 클 경우에는
        // if (hi < right && (lo == left || heights[lo - 1] < heights[hi + 1])) {
        //     min_height = min(min_height, heights[++hi]);
        // } else {
        //     min_height = min(heights[--lo], min_height);
        // }
        //다음과 같은 경우는 틀렸습니다
        if(lo < left){ //왼쪽으로 못가니까 오른쪽으로 이동
            min_height = min(min_height, heights[++hi]);
        }
        else if(hi > right){ // 오른쪽으로 못가니까 왼쪽으로 이동
            min_height = min(min_height, heights[--lo]);
        }
        else if(heights[lo - 1] > heights[hi + 1]){
            min_height = min(min_height, heights[--lo]);
        }
        else{
            min_height = min(min_height, heights[++hi]);
        }
        
        res = max(res, (hi - lo + 1) * min_height);
    }   
    return res;
}

int main(){
    FAST;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    // freopen("input.txt", "r", stdin);
#endif
    cin >> n;
    heights.resize(n);
    for(auto& height: heights) cin >> height;

    cout << dq(0, n - 1);


    //code


#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
