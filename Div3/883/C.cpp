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
        int N, probs, mins;
        cin >> N >> probs >> mins;

        vi scores;
        for(int i=0; i<N; i++) {
            vi times;
            for (size_t j = 0; j < probs; j++)
            {
                int time;
                cin >> time;
                times.push_back(time);
            }
            times.sort();
            
            cin >> h >> l;
            if (h > l) {
                ropes++;
            }
        }

        cout << ropes << endl;
    }
}