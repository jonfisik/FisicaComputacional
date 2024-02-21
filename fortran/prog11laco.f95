!! Jonatan P. Paschoal
!! 04 de fev de 2024.
!! do, while
!! Programa laços de repetição iteração
!!-----------------------------------------
	PROGRAM par
	IMPLICIT NONE
		
		INTEGER :: num = 0
		
		DO
		!! DO WHILE (num >= 0) !! forma alternativa para o laço, comentar linha 17 (IF(num < 0) EXIT)
			WRITE(*,*) 'Digite um número positivo ou negativo para parar.'
			READ(*,*) num
			
		! Testar para saber se o laço prossegue ou finaliza
			IF(num < 0) EXIT
		
		! Verificar se número é par
			IF(MOD(num,2) == 0) THEN	 
				WRITE(*,*) '>>> o número digitado é par.'
			ElSE
				WRITE(*,*) '>>> o número digitado é ímpar.'
			END IF
		END DO
		
		WRITE(*,'(A)') 'FIM!!!'
		
	END PROGRAM par
