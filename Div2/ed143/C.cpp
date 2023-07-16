#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int testcases;
    cin >> testcases;

    for (size_t t = 0; t < testcases; t++)
    {
        int n;
        cin >> n;
        unsigned int teas[n];
        for (size_t i = 0; i < n; i++) {
            cin >> teas[i];
        }

        unsigned int tasters[n];
        for (size_t i = 0; i < n; i++) {
            cin >> tasters[i];
        }

        unsigned int drank[n] = {0};

        for (size_t i = 0; i < n; i++) {
            unsigned int x = teas[i];
            int j = i;
            while(j < n && x > 0) {
                int amt = min(x, tasters[j]);
                x -= amt;
                drank[j] += amt;
                j += 1;
            }
        }

        for (size_t i = 0; i < n; i++) {
            cout << drank[i] << ' ';
        }
        cout << endl;
    }
}