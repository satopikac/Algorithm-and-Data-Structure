#include "stdio.h"
#include "stdlib.h"
int* extend(int* num,int size,int enlarge)
{
    int* res=new int[size+enlarge];
    for(int i=0;i<size;i++)
    {
        res[i]=num[i];
    }
    delete[] num;
    return res;

}
int main()
{
    ;
}