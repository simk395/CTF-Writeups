# Simple Encryption

Running this program will lead to an error. The first thing that can be done is to check for the strings which leads to nothing. Opening the file in Ghidra will lead to decompiled C showing the main function and the encryption algorithm.

```
undefined8 main(void)

{
  int iVar1;
  time_t tVar2;
  long in_FS_OFFSET;
  uint local_40;
  uint local_3c;
  long local_38;
  FILE *local_30;
  size_t local_28;
  void *local_20;
  FILE *local_18;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_30 = fopen("flag","rb");
  fseek(local_30,0,2);
  local_28 = ftell(local_30);
  fseek(local_30,0,0);
  local_20 = malloc(local_28);
  fread(local_20,local_28,1,local_30);
  fclose(local_30);
  tVar2 = time((time_t *)0x0);
  local_40 = (uint)tVar2;
  srand(local_40);
  for (local_38 = 0; local_38 < (long)local_28; local_38 = local_38 + 1) {
    iVar1 = rand();
    *(byte *)((long)local_20 + local_38) = *(byte *)((long)local_20 + local_38) ^ (byte)iVar1;
    local_3c = rand();
    local_3c = local_3c & 7;
    *(byte *)((long)local_20 + local_38) =
         *(byte *)((long)local_20 + local_38) << (sbyte)local_3c |
         *(byte *)((long)local_20 + local_38) >> 8 - (sbyte)local_3c;
  }
  local_18 = fopen("flag.enc","wb");
  fwrite(&local_40,1,4,local_18);
  fwrite(local_20,1,local_28,local_18);
  fclose(local_18);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

Taking a look at the write, it shows that the seed is being written to the file as the first 4 bytes. Afterwards, the flag is written.

Analyzing the logic, if we put everything in reverse order it should decrypt the flag. That means the left shift should go right and the xor should go last. Here is my implementation:

```
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
```

Running the program on Windows will print garbage out but when printing in Linux will show the flag.
