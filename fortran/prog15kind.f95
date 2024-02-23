!! Jonatan P. Paschoal
!! 23 de fev de 2024.
!! Programa: Aplicação Kind
!! Escreve os valores de kind para valores de precisão
!! simples e dupla
!!-----------------------------------------
	PROGRAM checa_kind
	IMPLICIT NONE
	
	INTEGER:: nkindis 

	nkindis=kind(9)

	WRITE(*,*) '--------------------------------------------------------'
	WRITE(*,*) 'Valor de kind p/ inteiro, extensão simples >>>', nkindis
	WRITE(*,*) 'Valor de kind p/ inteiro, extensão simples >>>', kind(9) 
	WRITE(*,*) 'Valor de kind p/ inteiro, extensão dupla >>>', kind(11111111)
	WRITE(*,*) 'Valor de kind p/ precisão simples >>>', kind(0.0)
	WRITE(*,*) 'Valor de kind p/ precisão simples >>>', kind(0.0e0)
	WRITE(*,*) 'Valor de kind p/ precisão dupla >>>', kind(0.0d0)
	WRITE(*,*) 'Valor de kind p/ precisão dupla >>>', kind(1.0d-300)
	WRITE(*,*) '--------------------------------------------------------'
	
	! Stop !! Opcional
			
	END PROGRAM checa_kind