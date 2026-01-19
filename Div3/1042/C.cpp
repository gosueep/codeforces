#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int cases;
    cin >> cases;
    for(int caseNum=0; caseNum<cases; caseNum++) {
        int N, k;
        cin >> N >> k;

        vi S;
        for(int i=0; i<N; i++) {
            int temp;
            cin >> temp;
            S.push_back(temp);
        }

        vi T;
        for(int i=0; i<N; i++) {
            int temp;
            cin >> temp;
            T.push_back(temp);
        }

        unordered_map<int, int> dict;

        for(int i=0; i<N; i++) {
            int mod,key;
            mod = S[i] % k;
            key = min(mod, k-mod);
            dict[key] += 1;

            mod = T[i] % k;
            key = min(mod, k-mod);
            dict[key] -= 1;
        }

        bool good = true;
        for(const auto& pair: dict) {
            if(pair.second != 0) {
                good = false;
                break;
            }
        }

        if(good){
            cout << "YES";
        }
        else {
            cout << "NO";
        }
        cout << "\n";
    }
}