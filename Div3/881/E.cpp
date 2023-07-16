#pragma once
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


const int inf = 1e9;
struct Node {
	Node *l = 0, *r = 0;
	int lo, hi, mset = inf, madd = 0, val = -inf;
	Node(int lo,int hi):lo(lo),hi(hi){} // Large interval of -inf
	Node(vi& v, int lo, int hi) : lo(lo), hi(hi) {
		if (lo + 1 < hi) {
			int mid = lo + (hi - lo)/2;
			l = new Node(v, lo, mid); r = new Node(v, mid, hi);
			val = max(l->val, r->val);
		}
		else val = v[lo];
	}
	int query(int L, int R) {
		if (R <= lo || hi <= L) return -inf;
		if (L <= lo && hi <= R) return val;
		push();
		return max(l->query(L, R), r->query(L, R));
	}
	void set(int L, int R, int x) {
		if (R <= lo || hi <= L) return;
		if (L <= lo && hi <= R) mset = val = x, madd = 0;
		else {
			push(), l->set(L, R, x), r->set(L, R, x);
			val = max(l->val, r->val);
		}
	}
	void add(int L, int R, int x) {
		if (R <= lo || hi <= L) return;
		if (L <= lo && hi <= R) {
			if (mset != inf) mset += x;
			else madd += x;
			val += x;
		}
		else {
			push(), l->add(L, R, x), r->add(L, R, x);
			val = max(l->val, r->val);
		}
	}
	void push() {
		if (!l) {
			int mid = lo + (hi - lo)/2;
			l = new Node(lo, mid); r = new Node(mid, hi);
		}
		if (mset != inf)
			l->set(lo,hi,mset), r->set(lo,hi,mset), mset = inf;
		else if (madd)
			l->add(lo,hi,madd), r->add(lo,hi,madd), madd = 0;
	}
};

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int cases;
    cin >> cases;
    for(int caseNum=0; caseNum<cases; caseNum++) {
        int N;
        cin >> N;
        vector<vi> adjlist(N+1);

        for(int i=0; i<N-1; i++) {
            int u,v;
            cin >> u >> v;
            adjlist[u].push_back(v);
            adjlist[v].push_back(u);
        }

        vi leaves(N+1);
        vi parent(N+1);

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
            cout << leaves[a]*leaves[b] << endl;
        }
    }
}