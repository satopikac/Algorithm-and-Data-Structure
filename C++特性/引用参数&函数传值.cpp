//函数1
#include <stdio.h>
int abc(int x,int y, int z)
{
    return x*y*z;
}
int abc1(int &x,int &y,int &z) 
{
return x*y*z;
}
//后者避免传值，节省了时间
int main()
{
    int x=1;
    int y=2;
    int z=3;
    printf("%d\n",abc(x,y,z));
    printf("%d\n",abc1(x,y,z));
}