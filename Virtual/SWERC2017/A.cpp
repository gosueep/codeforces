#include <cstdio>
#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    int N;
    int M;
    std::vector<int> entries;
    for (int i = 0; i < N; i++) {
        int temp;
        std::cin >> temp;
        entries.push_back(temp);
    }
    std::unordered_map<int, int> differences;
    for (int i = 0; i < M; i++) {
        int exit;
        std::cin >> exit;

        for (int j = 0; j < N; j++) {
            if (entries[j] >= exit) {
                break;
            }
            auto diff = exit - entries[j];
            if (differences.count(diff)) {
                differences[diff]++;
            } else {
                differences[diff] = 1;
            }
        }
    }

    int num_occurances = 0;
    int smallest = 0;
    for (auto diff : differences) {
        if (diff.second > num_occurances) {
            num_occurances = diff.second;
            smallest = diff.first;
        } else if (diff.second == num_occurances && diff.first < smallest) {
            smallest = diff.first;
        }
    }

    std::cout << smallest << std::endl;
}