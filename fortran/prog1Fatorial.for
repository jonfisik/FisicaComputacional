!! Jonatan P. Paschoal
!! 02 de fev de 2024.
!! Cálculo do fatorial de um número
!!-----------------------------------------

	PROGRAM fatorial

	IMPLICIT NONE

   	!! [especificação (variáveis)]
   		INTEGER :: n, i, fat = 1
   
   	!! [execução (lógica principal)]
  		WRITE(*,*) '----Fatorial de N - V1.0----'
   		WRITE(*,*) 'Digite um número N: '
   		READ(*,*) n
   
   	!! Cálculo do fatorial
   
   		DO i = 1, n
   			fat = fat*i
   		END DO
   
   	WRITE(*,'(A, I0)') 'O fatorial é: ', fat	
   
   	!! [subprogramas (funçõese procedimentos)]

	END PROGRAM fatorial
