#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main(){
    unsigned int seed;
    unsigned char byte;
    void *flag;
    int random;
    int random2;
    int i;
    
    flag = fopen("flag.enc","rb");
    fread(&seed, sizeof(unsigned char), 4, flag);
    srand(seed);

    for (i = 0; i < 28; i++) {
        random = rand();
        random2 = rand();
        fread(&byte, sizeof(unsigned char), 1, flag);
        random2 = random2 & 7;
        byte = 
            byte >> random2 |
            byte << 8 - random2;
        byte = byte ^ random;
        printf("%c", byte);
    }

    fclose(flag);
    return 0;
}
