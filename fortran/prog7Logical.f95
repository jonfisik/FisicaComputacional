!! Jonatan P. Paschoals
!! 04 de fev de 2024.
!! .not. negação lógica, .and. intersecção lógica, .or. união lógica,
!! .eqv. equivalência lógica, .neqv. não equivalêcia lógica   + <------- - 
!! Operações lógicas
!!-----------------------------------------
	PROGRAM operacoes_logicas
	IMPLICIT NONE
	
	CHARACTER :: j1, j2, j3 
	LOGICAL :: estado, estado_j1, estado_j2, estado_j3
	
	j1 = 'f'
	j2 = 'f'
	j3 = 'f'
	
	WRITE(*,*) '-------------------------------------'
	WRITE(*,*) 'Janela 01 está aberta? ', j1 == 'a', NEW_LINE('a')
	
	estado = j1 == 'a' .or. j2 == 'a' .or. j3 == 'a'
	WRITE(*,*) 'Alguma janela aberta? ', estado
	
	WRITE(*,*) NEW_LINE('a'), 'Alarme desligado? ', .not. estado
	
	estado = j1 == 'a' .and. j2 == 'a' .and. j3 == 'a'
	WRITE(*,*) NEW_LINE('a'), 'Todas as janelas abertas? ', estado
	
	! Converter os caracteres 'a' e 'f'em variáveis lógicas
	estado_j1 = (j1 == 'a')
	estado_j2 = (j2 == 'a')
	estado_j3 = (j3 == 'a')
	
	! Verificar estado
	estado = (estado_j1 .eqv. estado_j2) .and. (estado_j2 .eqv. estado_j3)
	WRITE(*,'(/, A, 1X, L)') 'Todas as janelas estão abertas ou fechadas ao mesmo tempo? ', estado
	
	
	WRITE(*,*) '-------------------------------------'
	
	END PROGRAM operacoes_logicas
