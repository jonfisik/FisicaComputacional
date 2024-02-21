!! Jonatan P. Paschoals
!! 04 de fev de 2024.
!! Parâmetos KIND gfortran
!!-----------------------------------------
	PROGRAM parametros_kind
	! Programa - dados, variáveis e constantes nomeadas
	USE iso_fortran_env
	IMPLICIT NONE
	
		! Seção de declaração
		!! Constante nomeada
		INTEGER, PARAMETER :: SGL = 4  ! single
		INTEGER, PARAMETER :: DBL = 8  ! double
		INTEGER, PARAMETER :: QBL = 16 ! double double 
		
		!! Variáveis
		REAL(KIND=4)   :: valor1 ! KIND - valor do parâmetro do tipo que será usado.
		REAL(KIND=DBL) :: valor2
		REAL(KIND=QBL) :: valor3
		REAL(8)        :: valor4
		INTEGER(KIND=8):: valor5
		
		!! Constante nomeada de precisão simples
		REAL, PARAMETER :: CONST = 66._SGL
		
		! Visualização dos resultados		
		WRITE(*,*) '        <<<   Tamanhos das variáveis   >>>         '
		WRITE(*,*) '------------------------------------------------------------'
		
		WRITE(*,*) 'KIND valor1 >>> ', KIND(valor1), 'bytes.' ! KIND - função que diz qual é o valor do parâmetro KIND
		WRITE(*,*) 'KIND valor2 >>> ', KIND(valor2), 'bytes.'
		WRITE(*,*) 'KIND valor3 >>> ', KIND(valor3), 'bytes.'
		WRITE(*,*) 'KIND valor4 >>> ', KIND(valor4), 'bytes.'
		WRITE(*,*) 'KIND valor5 >>> ', KIND(valor5), 'bytes.'
		WRITE(*,*) '------------------------------------------------------------'
		
		WRITE(*,*) 'KIND literal 0.0 >>> ', KIND(0.0), 'bytes.' ! 32 bits
		WRITE(*,*) 'KIND literal 0.0D0 >>> ', KIND(0.0D0), 'bytes.' ! 60 bits
		WRITE(*,*) 'Valor cte. >>> ', CONST ,' KIND ', KIND(CONST) 
		WRITE(*,*) '------------------------------------------------------------'
		
		WRITE(*,*) 'Precisão decimal da var. 1 >>> ', PRECISION(valor1), 'casas decimais.'
		WRITE(*,*) 'Precisão decimal da var. 2 >>> ', PRECISION(valor2), 'casas decimais.'
		WRITE(*,*) 'Precisão decimal da var. 2 >>> ', PRECISION(valor3), 'casas decimais.'
		WRITE(*,*) '------------------------------------------------------------'
		
		WRITE(*,*) 'Faixa expo. decimal da var. 1 >>> x10^', RANGE(valor1)
		WRITE(*,*) 'Faixa expo. decimal da var. 2 >>> x10^', RANGE(valor2)
		WRITE(*,*) 'Faixa expo. decimal da var. 3 >>> x10^', RANGE(valor3)
		WRITE(*,*) '------------------------------------------------------------'
		
		WRITE(*,*) 'KINDS disponíveis - Tipo REAL >>> ', real_kinds
		WRITE(*,*) 'KINDS disponíveis - Tipo INTEGER >>> ', integer_kinds
		WRITE(*,*) 'KINDS disponíveis - Tipo LOGICAL >>> ', logical_kinds
		WRITE(*,*) 'KINDS disponíveis - CHARACTER >>> ', character_kinds
		WRITE(*,*) '------------------------------------------------------------'
	
	END PROGRAM parametros_kind
