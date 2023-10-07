#include <stdio.h>
 #include <conio.h>


int main()
{
    int i,n,m,M;
    int a[n];

    scanf("%d",&n);


    for(i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    m,M = a[0];

    for(i=1; i<n; i++){


        if(a[i] > M)
            {
            M = a[i];
            }

        if(a[i] < m)
            {
            m = a[i];
            }


     printf("%d",m);
     printf("%d",M);

    }

}
