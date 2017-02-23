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

    int prev_val = 32767;
    int curr_val = -1;

    while(*p != 0) {
        curr_val = romanChToInt(*p);
        if (curr_val > prev_val) {
            result -= prev_val * 2;
        }
        result += curr_val;
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

