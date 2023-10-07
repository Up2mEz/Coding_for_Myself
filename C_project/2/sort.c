#include <stdio.h>

int main() {
    int n;
    scanf("%d" , &n);
    int a[n],i,odd[n],even[n];
    for (i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for (i=0;i<n;i++){
        if (a[i]%2 ==0){
            a[i]=even[i];
        }
        if (a[i]%2 ==1){
            a[i]=odd[i];
        }
    }





	return 0;
}
