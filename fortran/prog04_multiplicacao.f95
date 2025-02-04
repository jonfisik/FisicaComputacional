!! jonatan paschoal
!! 04 de fev de   2025
!! Calcular produto de 2 numeros inteiros,
!! informados pelo teclado

program multiplicacao

       implicit none

!! Declaracao variaveis
!! Inteiras:
!! i, j: numeros a serem multiplicados
!! k: resultado

       integer :: i, j, k

!! Entradas
       write(*,*)"Digite os valores i e j (separados por virgula)"      
       write(*,*)" "
       read(*,*)i,j

!! Calculo
       k=i*j
                 
!! Saidas
       write(*,*)" "
       write(*,*)"Produto  >>> ",i," x ",j," = ",k

end program multiplicacao
