#include <stdio.h>
#include <stdbool.h>

int romanChToInt(char c) {
    switch(c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default:  return 0;
    }
}

int romanToInt(char* s) {
    char *p = s;
    int result = 0;

    int prev_val = 1000;
    int curr_val = 0;

    while(*p != 0) {
        curr_val = romanChToInt(*p);
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

