!! Jonatan P. Paschoals
!! 02 de fev de 2024.
!! Cálculo do fatorial de um número
!!-----------------------------------------
	PROGRAM teste
	! Programa de teste do fortran
	IMPLICIT NONE
		
		INTEGER :: n
		
		WRITE(*,*) 'Digite um número: '
		READ(*,*) n
		WRITE(*,'(A, I0)') 'O número digitado foi >>> ', n
	
	END PROGRAM teste
