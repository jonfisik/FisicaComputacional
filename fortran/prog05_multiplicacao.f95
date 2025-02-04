!! jonatan paschoal
!! 04 de fev de   2025
!! Calcular produto de 2 numeros reais, precisao dupla
!! informados pelo teclado
!! Conversao inteiro para precisao dupla

program multiplicacao2

       implicit none

!! Declaracao variaveis
!! Inteiras:
!! x, y: numeros a serem multiplicados
!! Reais
!! z: resultado - precisao dupla

       integer :: x, y
       real(kind=1) :: z
       
!! Arquivo
       open(unit=3, file="saidaMult.txt")

!! Entrada
       write(*,*)"Digite os valores x e y (separados por virgula)"      
       write(*,*)" "
       read(*,*)x,y

!! Calculo
!! Utiliza real(<variavel>,kind)
       z=real(x,1)*real(y,1)
                 
!! Saidas
       write(*,*)"Literais utilizados: ",real(x,1),real(y,1)
       write(*,*)" "
       write(*,*)"Produto  >>> ",x," x ",y," = ",z
       write(3,*)"Produto  >>> ",x," x ",y," = ",z

end program multiplicacao2
