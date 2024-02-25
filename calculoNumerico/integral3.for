!! Jonatan P. Paschoal
!! 25 de fev de 2024.
!! Integracao numerica
!! f(x)=x³ (-1 a 1)
!! Loops reais
!!-----------------------------------------

	PROGRAM integral3

	IMPLICIT NONE

   	!! [especificação (variáveis)]
   		REAL*8 :: x, y, dx !! Precisão dupla (*)
   		REAL*8 :: r1,r2,r3 !! Idem (*)
   	
   	!! [execução (lógica principal)]
	!! Integrar y=x^3, x variando de -1 a 1
		
		dx=1d-5 !! dx=0.000001 (*)
		y=0.0d0 !! y=0. (*)
		
		DO x=-1.00d0,(1.00d0-dx),dx
			y=y+(x**3.+(x+dx)**3.)*dx*0.5
			
			WRITE(*,*) y
		END DO
   
   	WRITE(*,*) 'Solucao Numerica >>> ', y !! Integral
   	WRITE(*,*) 'Integral exata >>> ', 0.
   	
	END PROGRAM integral3
