#include<stdio.h>
#include<conio.h>
#include <math.h>
main()
{
  int digit, inputbilangan, a;
  digit = 0;

  printf("Masukkan ANGKA :");
  scanf("%d", &inputbilangan);

  a = inputbilangan;

  while (1)
  {
    a /= 10;
    if (a > 0)
    {
      digit++;
    }
    else
    {
      // digit++;
      break;
    }
  }

  int arrayangka[digit];
  int pangkat = digit;
  int banyaknol = 0;

  for (int x = 0; x <= digit; x++)
  {
    arrayangka[x] = inputbilangan / (pow(10, pangkat));
    if (arrayangka[x] == 0)
    {
      banyaknol++;
    }
    inputbilangan = inputbilangan - (arrayangka[x] * (pow(10, pangkat)));
    pangkat--;

    //printf ("\nPanjang Digit adalah %d", arrayangka[x]);
  }
  //  printf ("\nbanyak Nol  %d", banyaknol);
  int posisinol[banyaknol + 2];
  posisinol[0] = -1;
  posisinol[banyaknol + 1] = digit + 1;
  int index = 1;

  for (int x = 0; x <= digit; x++)
  {
    if (arrayangka[x] == 0)
    {
      posisinol[index] = x;
      //   printf ("\nPosisi Nol  %d", posisinol[index]);
      index++;
    }
  }
  for (int x = 0; x < banyaknol + 2; x++)
  {
    //printf ("\nPosisi Nol  %d", posisinol[x]);
  }
  //printf ("\n");


  //int arrayangkabaru[banyaknol+1][];

  for (int x = 0; x < banyaknol + 1; x++) //untuk for perkelompok
  {
    int banyakdataperkelompok = (posisinol[x + 1] - posisinol[x]) - 1;
    int arraykelompok[banyakdataperkelompok];
    int urutkelompok[banyakdataperkelompok];
    int posisiterendah = 0;
    index = 0;
    printf ("%d", banyakdataperkelompok);
    for (int xx = posisinol[x] + 1; xx < posisinol[x + 1]; xx++)
    {
      arraykelompok[index] = arrayangka[xx];
      index++;
    }
    int rendah = 9;
    for (int x = 0; x < banyakdataperkelompok; x++)
    {
      for (int xx = 0; xx < banyakdataperkelompok; xx++)
      {
        if (arraykelompok[xx] < rendah)
        {
          rendah = arraykelompok[xx];
          posisiterendah = xx;
        }

      }
//      urutkelompok[x]=posisiterendah
      printf ("%d",  rendah);
      printf ("\n");
    }



    return (0);
  }
