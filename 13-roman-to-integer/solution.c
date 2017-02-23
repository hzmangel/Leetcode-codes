#include <stdio.h>
#include <stdbool.h>

int romanToInt(char* s) {
    char *p = s;
    int result = 0;

    int prev_val = 1000;
    int curr_val = 0;

    while(*p != 0) {
        switch(*p) {
            case 'I':
                curr_val = 1;
                break;
            case 'V':
                curr_val = 5;
                break;
            case 'X':
                curr_val = 10;
                break;
            case 'L':
                curr_val = 50;
                break;
            case 'C':
                curr_val = 100;
                break;
            case 'D':
                curr_val = 500;
                break;
            case 'M':
                curr_val = 1000;
                break;
        }

        result += curr_val > prev_val ? (curr_val - (prev_val << 1)) : curr_val;
        prev_val = curr_val;
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
    printf("%d\n", romanToInt("MDCCCLXXXIV"));
    for (long i = 1; i < 10000000; i++) {
        romanToInt("MCMXCVI");
    }
    return 0;
}

