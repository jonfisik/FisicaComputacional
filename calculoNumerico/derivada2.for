!! Jonatan P. Paschoal
!! 17 de fev de 2024.
!! Derivada numérica com 3 pontos
!! f(x) -- {f(x1),f(x2),f(x3),...}
!! f'(x_k) = (1/2h)*(-3*f(x_k)+4*f(x_k+h)-f(x_k+2h))
!! f'(x_k) = (1/2h)*(f(x_k-2h)-4*f(x_k-h)+3*f(x_k)) 
!!-----------------------------------------

	PROGRAM derivada

	IMPLICIT NONE

   	!! [especificação (variáveis)]
   		REAL :: f0,f1,f2, h = 0.005, x = 2.
   		REAL :: d1,d2,d3
   	
   	!! log() - logaritmo natural "ln"
   	!! Derivada exata -- f(x)=ln(x) --> df/dx=1/x
   
   	!! [execução (lógica principal)]
  		f2=log(x+2.*h)   !! f(x+2h)        
        	f1=log(x+h)      !! f(x+h)
        	f0=log(x)        !! f(x)
        	
        	d1=(-3*f0+4.*f1-f2)/(2.*h)   !! df/dx = (1/2h)*(-3*f(x_k)+4*f(x_k+h)-f(x_k+2h))
        	
        	f2=log(x-2.*h)   !! f(x-2h)        
        	f1=log(x-h)      !! f(x-h)
        	f0=log(x)        !! f(x)
        
        	d2=(f2-4.*f1+3.*f0)/(2.*h)   !! df/dx=(f(x-2h)-4f(x-h)+3f(x))/2*h
 
        	d3=1.0/x          !! Der. exata
   
   	WRITE(*,*) 'Der. ln(2) "+" >>> ', d1
   	WRITE(*,*) 'Der. ln(2) "-" >>> ', d2
   	WRITE(*,*) 'Der. ln(2) Exata >>> ', d3
   	WRITE(*,*) 'Abs. "+" - Exata >>> ', abs(d1-d3)
   	WRITE(*,*) 'Abs. "-" - Exata >>> ', abs(d2-d3)
   

	END PROGRAM derivada
