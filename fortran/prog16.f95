!! Jonatan P. Paschoal
!! 28 de fev de 2024.
!! Programa: 
!! Exemplo modulo, funcao
!!-----------------------------------------
	PROGRAM iniciante
		USE prog16modulo, only: dp !! Necessário compilar também o módulo
		
		IMPLICIT NONE
			
		REAL(dp) :: a,b,c !! Definindo dupla precisão
		REAL(dp) :: prog16funcao
		!! a=4; b=5

    		a=5
      		b=3
		c=0
	
		!! c=prog16funcao(a,b)

  		call prog16subrotina(a,b,c)
		
		WRITE(*,*) '-------------------'
		PRINT*,c
		WRITE(*,*) '-------------------'
			
	END PROGRAM iniciante 
