#include <stdio.h>
#include <cs50.h>

int check(long cn);

int main(void)
{
    // Prompt user for card number
    long cn;
    cn = get_long("Please enter your card number: ");
    
    // Identifies invalid
    if (check(cn) % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    
    // Assign card type
    int k;
    k = ((cn - cn % 1000000000000) / 1000000000000);
    if ((k == 4) || (k > 3999 && k < 5000))
    {
        printf("VISA\n");
    }
   
    else if ((k > 339 && k < 350) || (k > 369 && k < 380))
    {
        printf("AMEX\n");
    }
   
    else if (k > 5099 && k < 5600)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
    
    
}
  
// Checksum
int check(long cn)
{
    int checksum = 0;
    int j = 1;
    int i;
    do
    {
      i = cn % 10;
      cn = (cn - i) / 10;
     
      if (j % 2 == 0) // Doubles every other digit
      {
        i *= 2;
        
        if (i > 9) // Adds double-digit numbers
        {
           i = i % 10 + ((i - i % 10) / 10);
        }
      }
      checksum += i; // Sums digits
      j++;
    }
    while (cn > 1);
    return checksum;
}
