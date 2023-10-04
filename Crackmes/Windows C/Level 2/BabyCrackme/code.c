#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv){

    char *key = (char *) calloc(6, sizeof(char));
    strcpy(key, "\"3 \"*,$");

    for(int i = 0; i <= 256; i++){
        printf("%i: ", i);
       for(int j = 0 ; j < (int) strlen(key); j++){
            char c = *(key + j);
            char val = i ^ c;
            printf("%c", val);
       }

       printf("\n");
    }

    free(key);
}
