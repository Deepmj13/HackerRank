#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    char s[100];
    char sen[100];
    
    scanf("%c",&ch);
    scanf("%s",s);
    gets(sen);
    
    printf("%c\n%s\n%s\n",ch,s);
    puts(sen);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
