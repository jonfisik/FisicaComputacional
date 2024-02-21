!! Jonatan P. Paschoals
!! 02 de fev de 2024.
!! Estrutura de um programa fortran
!!-----------------------------------------
	PROGRAM teste
	! Programa de teste do fortran
	IMPLICIT NONE
		! Seção de declaração
		INTEGER :: i ! Tipo de variável inteira
		INTEGER :: valor
		i = 13 !! Máximo de caracter 123.
		
		! Seção de execução
		valor = 2+3-5/6   ! "&" Instrução continua na linha seguinte -
	1	 -1*10
		
		WRITE(*,'(A, I0)') 'Valor de I >>> ', i
		WRITE(*,'(A, I0)') 'Valor da expressão >>> ', valor
	
	END PROGRAM teste
