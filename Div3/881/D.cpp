#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;



vector<vi> adjlist;
vi leaves;
vi parent;

unsigned long long count(int a) {
    if (leaves[a] != 0)
        return leaves[a];
    int num = 0;
    for(int i : adjlist[a]) {
        if(i != parent[a]) {
            num += count(i);
        }
        leaves[a] = num;
    }
    return num;
}



int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int cases;
    cin >> cases;
    for(int caseNum=0; caseNum<cases; caseNum++) {
        int N;
        cin >> N;
        adjlist = vector<vi>(N+1);

        for(int i=0; i<N-1; i++) {
            int u,v;
            cin >> u >> v;
            adjlist[u].push_back(v);
            adjlist[v].push_back(u);
        }

        leaves = vi(N+1);
        parent = vi(N+1);

        vi dfs({1});
        set<int> seen;
        while(!dfs.empty()) {
            int curr = dfs.back();
            dfs.pop_back();
            seen.insert(curr);
            bool leaf = true;
            for(int i : adjlist[curr]) {
                if(!seen.count(i)) {
                    dfs.push_back(i);
                    parent[i] = curr;
                    leaf = false;
                }
            }

            if(leaf) {
                leaves[curr] = 1;
                // int p = parent[curr];
                // while(p != 0) {
                //     leaves[p]++;
                //     p = parent[p];
                // }
            }
        }

        int Q;
        cin >> Q;
        for (int i=0; i<Q; i++) {
            int a,b;
            cin >> a >> b;
            cout << count(a) * count(b) << endl;
        }
    }
}