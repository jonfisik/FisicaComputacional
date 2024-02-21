!! Jonatan P. Paschoals
!! 04 de fev de 2024.
!! Estrutura de um programa fortran
!!-----------------------------------------
	PROGRAM declaracoes
	! Programa - dados, variáveis e constantes nomeadas
	IMPLICIT NONE
	
		! Seção de declaração
		!! Tamanho para nome variável - máximo de caracter 123.
		INTEGER :: quantidade ! Tipo de variável inteira
		REAL :: peso ! Tipo real, ponto flutuante
		CHARACTER(len=20) :: nome ! Tipo Caracter
		LOGICAL :: estado = .true. ! Tipo lógico
		COMPLEX :: tensao ! Tipo complexo
		
		! Constante nomeada
		REAL, PARAMETER :: fator_mult = 4.56
		
		! Atribuição de valores 
		quantidade = 50
		peso = 45.60
		nome = 'Jonatan P. Paschoal'
		! fator_mult = 5.5
		tensao = (12.0, 2.0)
		
		! Visualização dos resultados		
		WRITE(*,*) 'Var. Quantidade >>> ', quantidade
		WRITE(*,*) 'Var. Peso >>> ', peso
		WRITE(*,*) 'Var. Nome >>> ', nome
		WRITE(*,*) 'Var. Estado >>> ', estado
		WRITE(*,*) 'Var. Fator >>> ', fator_mult
		WRITE(*,*) 'Var. Tensão >>> ', tensao
		
		WRITE(*,*) 'Maior valor inteiro >>>', HUGE(quantidade) ! HUGE - maior valor, "enorme". Var. inteira.
		WRITE(*,*) 'Menor valor real positivo >>>', TINY(peso) ! TIMY - menor valor. Var. real.
	
	END PROGRAM declaracoes
