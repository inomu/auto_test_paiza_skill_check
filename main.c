#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){    // 自分の得意な言語で
    // Let's チャレンジ！！
    char str[1000];

    fgets(str, sizeof(str), stdin);
    if( 30 == atoi(str) ){
        printf("200\n");
    }
    /* 便利コード
     * １行の中に複数の取り出したい要素があった場合に使う
    char *sp = strtok( str , " ");
    const int num_of_applicant = atoi(sp);
    sp = strtok( NULL , " ");
    const int expect_x = atoi(sp);
    便利コード */

    /* 便利コード
     * 最後の単語に含まれる改行コードを取り除く 
        char* adr = strchr( str , '\n' );
        if( NULL != adr) *adr = '\0';
    便利コード */

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
    return 0;
}
