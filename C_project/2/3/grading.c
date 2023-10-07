#include <stdio.h>


int main()
{
    int i,s[2],total=0;

    for(i=0; i<=2; i++) {

        scanf("%d", &s[i]);
        total = total + s[i];


    }

    if (total >= 80)
    {
        printf("A");
    }
        if (total >= 74 && total <= 79 )
    {
        printf("B+");
    }



}

