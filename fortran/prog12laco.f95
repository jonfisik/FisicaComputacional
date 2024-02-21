!! Jonatan P. Paschoal
!! 04 de fev de 2024.
!! do, while
!! Programa laços de repetição iteração
!! Sintase
!! DO índice, fim, incremento
!!	declarações
!! END DO
!!-----------------------------------------
	PROGRAM contagem
	IMPLICIT NONE

	INTEGER :: cont, n
	INTEGER :: fat = 1
	CHARACTER(20) :: frase = 'Amanda A. G. Pantoja'
	
	DO cont = 1, 10
		WRITE(*,'(I2)') cont
	END DO
	WRITE(*,*) '-----------------------'
	
	DO cont = 1, 30, 2
		WRITE(*,'(I2)') cont
	END DO
	WRITE(*,*) '-----------------------'
	
	DO cont = 1, 15
		WRITE(*,'(A)') frase
	END DO
	
	WRITE(*,*) '-----------------------'
	! Fatorial
	WRITE(*,'(A)') 'Digite o número inteiro para o fatorial. '
	READ(*,*) n
	
	DO cont = 1, n
		fat = fat * cont
	END DO	
	
	WRITE(*,*) fat
		
	END PROGRAM contagem
