#include <iostream>
#include <string.h>

using namespace std;

int main() {
    int T, N, M, min_blocks[1000010], A[30];
    min_blocks[0] = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++) scanf("%d", &A[i]);
        for (int Mi = 1; Mi <= M; Mi++) {
            int min_for_Mi = Mi;
            for (int i = 0; i < N; i++)
                if (Mi - A[i] >= 0)
                    min_for_Mi = min(min_for_Mi, 1 + min_blocks[Mi-A[i]]);
            min_blocks[Mi] = min_for_Mi;
        }
        printf("%d\n", min_blocks[M]);
    }
    return 0;
}
