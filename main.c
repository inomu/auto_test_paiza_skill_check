#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){    // 自分の得意な言語で
    // Let's チャレンジ！！
    char str[1000];

    fgets(str, sizeof(str), stdin);
    if( 30 == atoi(str) ){
        printf("200\n");
    }

    if( 50 == atoi(str) ){
        printf("400\n");
        printf("300\n");
    }

    if( 40 == atoi(str) ){
        printf("500\n");
    }

    fgets(str, sizeof(str), stdin);
    if( 01 == atoi(str) ){
        printf("501\n");
        printf("502\n");
    }

    //printf("argc=%d\n" , argc);
    //printf("argv[0]=%s\n" , argv[0]);
    //printf("argv[1]=%s\n" , argv[1]);

    return 0;
}
