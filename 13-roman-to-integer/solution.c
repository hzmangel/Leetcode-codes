#include <stdio.h>
#include <stdbool.h>

int romanToInt(char* s) {
    char *p = s;
    int result = 0;

    int prev_val = 1000; // M
    int curr_val = 0;

    int nums[26];
    nums['I' - 'A'] = 1;
    nums['V' - 'A'] = 5;
    nums['X' - 'A'] = 10;
    nums['L' - 'A'] = 50;
    nums['C' - 'A'] = 100;
    nums['D' - 'A'] = 500;
    nums['M' - 'A'] = 1000;

    while(*p != 0) {
        curr_val = nums[*p - 'A'];
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

