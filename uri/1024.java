import java.io.*;
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useDelimiter("\n");
        int T = in.nextInt();
        // Stress test:
        // int T = 10000;

        while(T-- > 0) {
            char[] s = in.next().toCharArray();
            // Stress test:
            // char[] s = new char[1000];
            // for (int i = 0; i < 1000; i++) {
            //     s[i] = 'a';
            // }
            int len = s.length;
            for (int i = 0; i < len; i++) {
                if ((s[i] >= 'a' && s[i] <= 'z') ||
                    (s[i] >= 'A' && s[i] <= 'Z')) {
                    s[i] += 3;
                }
            }
            for (int i = 0; i < len / 2; i++) {
                char aux = s[i];
                s[i] = s[len - 1 - i];
                s[len - 1 - i] = aux;
            }
            int half_index = (int)(len / 2);
            for (int i = half_index; i < len; i++) {
                s[i] -= 1;
            }
            System.out.println(s);
        }
    }
}