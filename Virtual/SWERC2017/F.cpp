#include <cstdio>
#include <iostream>

int main() {
    int W;
    int N;
    std::cin >> W;
    std::cin >> N;
    int64_t total_area = 0;
    for (int i = 0; i < N; i++) {
        int w;
        int l;
        std::cin >> w >> l;
        total_area += w * l;
    }
    std::cout << total_area / W << std::endl;
}