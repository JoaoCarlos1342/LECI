#include <stdio.h>
#include <unistd.h>
#include "process.h"

int main(void) {
    pid_t ret = pfork();

    if (ret == 0) {
        for (int i = 1; i <= 10; i++) {
            printf("%d\n", i);
        }
    } else {
        pwait(NULL);
        for (int i = 11; i <= 20; i++) {
            printf("%d\n", i);
        }
    }

    return 0;
}