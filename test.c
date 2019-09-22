#import <stdio.h>

int main () {
    int i = 0;
    long int x = 0;
    while (i < 100000000) {
        x += i;
        i++;
    }

    printf("%ld", x);

    return 0;
}