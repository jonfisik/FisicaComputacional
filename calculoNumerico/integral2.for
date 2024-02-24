!! Jonatan P. Paschoal
!! 17 de fev de 2024.
!! Integracao numerica
!! f(x)=x² (0 - 1)
!! Loops inteiros - tempo de execucao maior
!!-----------------------------------------

	PROGRAM integral

	IMPLICIT NONE

   	!! [especificação (variáveis)]
   		REAL :: x, y, dx
   		REAL :: r1,r2,r3
		INTEGER :: i2,i2,i3
   	
   	!! [execução (lógica principal)]
	!! Integrar y=x^2, x variando de 0 a 1
		
		dx=0.000001
		y=0.
		
		r1=1./dx
		i1=int(r1)
		
		x=0.
		
		DO i2=1,i1.,1
			y=y+(x**2.)*dx
			
			WRITE(*,*) y
		ENDDO
   
   	WRITE(*,*) 'Solucao Numerica >>> ', y !! Integral
   	WRITE(*,*) 'Integral exata >>> ', (1.0e0)/(3.0e0)
   	
	END PROGRAM integral
