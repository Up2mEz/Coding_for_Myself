#include <stdio.h>

int main()
{
    int num[9],i,j,k,z,found=0,count,none[z];

    for(i=0;i <= 9;i++)
    {
    scanf("%d" ,&num[i]);
    num[i] %= 42;

    }

    for(i=0; i <= 9; i++)
    {
      count=0;
      for(j=1; j <= 9; j++)
      {
        if (num[i] != num[j])
        {
            for(k=0; k<found; k++)
            {

                if(num[i] == none[k])
                {
                    count++;
                }
            }
            if(count==0)
            {
               none[found] = num[i];
               found++;
            }

        }
      }
    }
    printf("resualt = %d\n" ,found);
    return 0;
}
