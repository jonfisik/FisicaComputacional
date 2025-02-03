!! jonatan paschoal
!! 03 de fev de   2025
!! Uso da funcao kind


program verifica_tipo

implicit none

!! Declaracao variaveis

integer :: nkindis

!! Verificar os valores de kind para valores de precisao simples e dupla

nkindis=kind(9)

write(*,*)"Valor de kind para inteiro extensao simples A: ",nkindis
write(*,*)"Valor de kind para inteiro extensao simples B: ",kind(3)
write(*,*)"Valor de kind para inteiro extensao dupla: ",kind(111111111)
write(*,*)"Valor de kind para precisao simples A: ",kind(0.0)
write(*,*)"Valor de kind para precisao simples B: ",kind(0.0e0)
write(*,*)"Valor de kind para precisao dupla A: ",kind(0.0d0)
write(*,*)"Valor de kind para precisao dupla B: ",kind(1.0d-300)
write(*,*)"Valor de kind para precisao simples: ",kind(1.0e-30)
end program verifica_tipo
