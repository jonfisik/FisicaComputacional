!! Jonatan P. Paschoals
!! 04 de fev de 2024.
!! if, else if e else
!! Programa Condicionais
!!-----------------------------------------
	PROGRAM condicionais
	IMPLICIT NONE
		
		INTEGER :: num = 0
		CHARACTER(34) :: msg = 'Digite um número para avaliação: '
		
		WRITE(*,'(A)') msg
		READ(*,*) num
		
		IF(num >= 10) THEN
			WRITE(*,'(A, I3, 1X, A)') 'O número ', num, ' é maior ou igual a 10.'
		ELSE
			WRITE(*,'(A, I3, 1X, A)') 'O número ', num, ' é menor do que 10.'
		END IF 
				
	END PROGRAM condicionais
