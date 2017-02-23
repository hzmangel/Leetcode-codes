#include <stdio.h>
#include <stdbool.h>

int romanChToInt(char c) {
    int result = 0;

    switch(c) {
        case 'I':
        case 'i':
            result = 1;
            break;
        case 'V':
        case 'v':
            result = 5;
            break;
        case 'X':
        case 'x':
            result = 10;
            break;
        case 'L':
        case 'l':
            result = 50;
            break;
        case 'C':
        case 'c':
            result = 100;
            break;
        case 'D':
        case 'd':
            result = 500;
            break;
        case 'M':
        case 'm':
            result = 1000;
            break;
    }

    return result;
}

int romanToInt(char* s) {
    char *p = s;
    int result = 0;

    while (*p != 0) {
        int p_val = romanChToInt(*p);
        if ((p_val == 1 || p_val == 5 || p_val == 10 || p_val == 100) && *(p+1)) {
            // Check next character to determine whether require minus
            int next_p_val = romanChToInt(*(p+1));
            if (p_val < next_p_val) {
                result += (next_p_val - p_val);
                p++;
            } else {
                result += p_val;
            }
        } else {
            result += p_val;
        }

        p++;
    }

    return result;
}

int main() {
    printf("%d\n", romanToInt("X") == 10);
    printf("%d\n", romanToInt("XIV") == 14);
    printf("%d\n", romanToInt("VIII") == 8);
    printf("%d\n", romanToInt("XCIX") == 99);
    printf("%d\n", romanToInt("XLV") == 45);
    printf("%d\n", romanToInt("MCMXCVI") == 1996);
    return 0;
}

