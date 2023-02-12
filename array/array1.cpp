#include"stdio.h"
#include"stdlib.h"
//随机返回一个数组元素
int ranret(int* num,int size)
{
    int arrnum=rand()%size;
    int arrnumber=num[arrnum];
    return arrnumber;
}
int main()
{
    int size;
    printf("please put the lenth of the array\n");
    scanf("%d",&size);

    int num[size];
    puts("put the numbers of the array\n");
    for (int i = 0; i < size; i++)
    {
        /* code */
        scanf("%d",&num[i]);
    }
    int count[5]={0};
    for(int j=0;j<1000000;j++)
    {
    switch (ranret(num,size))
    {
    case /* constant-expression */1:
        /* code */count[0]++;
        break;
    case 2:
    count[1]++;
    break;
    case 3:
    count[2]++;
    break;
    case 4:
    count[3]++;
       break;
    default:count[4]++;
        break;
    }
    }

    for (int i = 0; i < size; i++)
    {
        /* code */
        printf("%d\n",count[i]);
    }
    

}