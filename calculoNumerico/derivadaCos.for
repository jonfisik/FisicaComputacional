!! Jonatan P. Paschoal
!! 17 de fev de 2024.
!! Derivada numérica
!! f'(x)=[f(x+h)-f(x-h)]/2h (série de taylor) ou f'(x)=[f(x+h)-f(x)]/h (definição)
!!-----------------------------------------

	PROGRAM derivada

	IMPLICIT NONE

   	!! [especificação (variáveis)]
   		REAL :: f0,f1,f2, h = 0.1, x = .5
   		REAL :: d1,d2,d3
   	
   	!! cos(x) cosseno 
   	!! Derivada exata -- f(x)=cos(x) --> df/dx=-sen(x)
   
   	!! [execução (lógica principal)]
  		f2=cos(x+h) !! f(x+h) - depois        
        	f1=cos(x)   !! f(x) - atual
        	f0=cos(x-h) !! f(x-h) - antes
        	
        	d1=(f2-f0)/(2.*h)  !!(f(x+h)-f(x-h))/2*h Der. Taylor
        	d2=(f2-f1)/h       !! f(x+h)-f(x)/h Der. definição 
        	d3=-sin(x)          !! Der. exata
   
   	WRITE(*,*) 'Der. cos(x) Taylor >>> ', d1
   	WRITE(*,*) 'Der. cos(x) Definição >>> ', d2
   	WRITE(*,*) 'Der. cos(x) Exata >>> ', d3
   	WRITE(*,*) 'Abs. Taylor - Exata >>> ', abs(d1-d3)
   	WRITE(*,*) 'Abs. Definição - Exata >>> ', abs(d2-d3)
   

	END PROGRAM derivada
