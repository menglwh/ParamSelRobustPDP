// test.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include "/home/200499800036/src/gmp/gmp-6.0.0/gmp.h"
#include <time.h>
#include <string.h>
//////////////////////////////////////////////////////////////
unsigned char *a;
char *b_8;
#define  __int64 long long

int main(int argc, char **argv)
{
	srand((int)time(0));
	time_t seed;  
	gmp_randstate_t state;  
	time(&seed); 
    mpz_t p;
	mpz_init(p);
	gmp_randinit_default(state);  
	gmp_randseed_ui(state, long(seed)); 
	//gmp_randseed_ui(state, long(5)); 
 	

	mpz_t f,d;
	mpz_init_set_str(f,argv[1],10);//100000
	mpz_init_set_str(d,argv[2],10);//100000
	//gmp_printf("blocks f=%Zd d=%Zd\n",f,d);
    
	size_t i_f,i_d;
	i_f=atoi(argv[1]);
	i_d=atoi(argv[2]);
	////////////////////////////////
	mpz_t f_and_d;
	int i_f_and_d;
	mpz_init_set (f_and_d,f);
	mpz_add (f_and_d,f_and_d,d);
    mpz_div_ui(f_and_d,f_and_d,1);
	mpz_add_ui (f_and_d,f_and_d,1);
	//gmp_printf("F+D=%Zd\n",f_and_d);
	i_f_and_d=mpz_get_ui(f_and_d);
    b_8= (char *) malloc(i_f_and_d);
	if (b_8==NULL)
	{
		return 1;
	}
   /////////////////////////////////////////
	int k=atoi(argv[3]);//100
	int n=atoi(argv[4]);//108
    
	mpz_t groups_t;
	mpz_init(groups_t);
	mpz_div_ui(groups_t,f,k);
	//gmp_printf("groups %Zd \n",groups_t);

	size_t groups=mpz_get_ui(groups_t);
    //printf("groups  %u\n",groups);
	a=(unsigned char *)malloc(groups);
	if (a==NULL)
	{
		return 2;
	}
	int ll=atoi(argv[7]);//times 500
	
	unsigned long int index;
	int oks=0;
    
	mpz_t mpz_x_f,mpz_x_r;
	mpz_init_set_str(mpz_x_f,argv[5],10);
	mpz_init_set_str(mpz_x_r,argv[6],10);

    //gmp_printf("choose  X_f=%Zd X_r=%Zd\n",mpz_x_f,mpz_x_r);
	size_t len;
	char *tt;
	__int64 x_f;
	memset((char *)&x_f,0,8);
	tt=(char *)mpz_export(0, &len, 1, 1, 0, 0, mpz_x_f);
	free(tt);
	memcpy((char *)&x_f,mpz_x_f->_mp_d,len);
	__int64 x_r;
	memset((char *)&x_r,0,8);
	tt=(char *)mpz_export(0, &len, 1, 1, 0, 0, mpz_x_r);
	free(tt);
	memcpy((char *)&x_r,mpz_x_r->_mp_d,len);
	//printf("choose x_f=%I64d x_r=%I64d\n",x_f,x_r);
	//printf("choose x_f=%lld x_r=%lld\n",x_f,x_r);
	int corrected=atoi(argv[8]);

	for (int i=0;i<ll;i++)
	{
		//printf("running %d\n",i);
		memset(a,0,groups);
        bool F=false;
		memset(b_8,0,i_f+i_d);
		//////////////////////////////////////////////////////////////
// 		gmp_randstate_t state1; 
// 		gmp_randstate_t state2; 
// 		mpz_t p;
// 		{
// 			srand((int)time(0));
// 			time_t seed;  
// 			time(&seed); 
// 			mpz_init(p);
// 			gmp_randinit_default(state1);  
// 			//gmp_randinit_mt(state);
// 			gmp_randseed_ui(state1, long(GetTickCount())); 
// 	
//             //Sleep(1000);
// 			gmp_randinit_default(state2);  
// 			//gmp_randinit_mt(state);
// 			gmp_randseed_ui(state2, long(GetTickCount()+1000)); 
// 	
// 		}
		////////////////////////////////////////////////////////////////
		for (__int64 jj=0;jj<x_f;jj++)
		{
			int ccc=0;
			while(1)
			{
				mpz_urandomm(p,state,f);
				index=mpz_get_ui(p);
				if (b_8[index]==1)
				{
					//printf("one error repeat at %I64d\n",jj);
					//ccc++;
// 					if (ccc>1)
// 						printf("one error %d repeat at %I64d\n",i,jj);
					continue;
				}
				
				b_8[index]=1;
				mpz_div_ui(p,p,k);
				index=mpz_get_ui(p);
				break;
			}
			

			a[index]++;
			if (a[index]==corrected)
			{
				oks++;
				//printf("find at X_f %I64d of %I64d\n",jj,x_f);
				F=true;
				break;
			}

		}
		if (!F)
			for ( __int64  jj=0;jj<x_r;jj++)
			{

				while(1)
				{
					mpz_urandomm(p,state,d);
					index=mpz_get_ui(p);
					if (b_8[index+i_f]==1)
					{
						//printf("two error repeat at %I64d\n",jj);
						continue;
					}

					b_8[index+i_f]=1;
					mpz_div_ui(p,p,n-k);
					index=mpz_get_ui(p);
					break;
		
				}
				a[index]++;
				if (a[index]==corrected)
				{
					oks++;
					//printf("find at X_r %I64d of %I64d\n",jj,x_r);
					break;
				}
				
			}
// 			gmp_randclear(state1);
// 			gmp_randclear(state2);
	}
	
	printf("%d %f",oks,oks*1.0/ll);
	free (a);
  return 0;
}
