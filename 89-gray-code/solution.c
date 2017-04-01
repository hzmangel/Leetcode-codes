#include <stdio.h>
#include <stdlib.h>

int* grayCode(int n, int* returnSize) {
    *returnSize = 1 << n;
    int * rslt = (int *)malloc(sizeof(int) * (*returnSize));
    rslt[0] = 0;

    for (int i = 1; i < *returnSize; i++) {
        rslt[i] = (i ^ (i >> 1));
    }

    return rslt;
}

int main() {
    int rslt_len;
    int* rslt = grayCode(3, &rslt_len);

    for (int i = 0; i < rslt_len; i++) {
        printf("%d, ", rslt[i]);
    }

    free(rslt);
    return 0;
}
