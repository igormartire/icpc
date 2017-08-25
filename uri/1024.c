#include <stdio.h>
#include <string.h>

int main() {
    int T, i;
    char s[1001];

    scanf("%d\n", &T);
    while(T--) {
        int len = strlen(gets(s));
        for (i = 0; i < len; i++) {
            if ((s[i] >= 'a' && s[i] <= 'z') ||
                (s[i] >= 'A' && s[i] <= 'Z')) {
                s[i] += 3;
            }
        }
        for (i = 0; i < len / 2; i++) {
            char aux = s[i];
            s[i] = s[len - 1 - i];
            s[len - 1 - i] = aux;
        }
        int half_index = (int)(len / 2);
        for (i = half_index; i < len; i++) {
            s[i] -= 1;
        }
        printf("%s\n", s);
    }
    return 0;
}