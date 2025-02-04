!! jonatan paschoal
!! 04 de fev de   2025
!! Exemplificar o emprego da funcao intrisica selected_real_kind
!! e formas de transformar precisao simples em dupla (ou maior)

program funcao_kind

       implicit none

!! Declaracao variaveis
!! Inteiras:
!! k_number_s: numero kind de precisao simples
!! k_number_d: numero kind de precisao dupla
!! Reais
!! xsp: Variavel precisa simples padrao
!! xdp: Variavel precisao dupla padrao
!! xs: variavel de precisao simples
!! xd: variavel de precisao dupla
!! xsd1, xsd2: variavel de precisao simples transformada em dupla ou maior

       integer, parameter :: k_number_s=selected_real_kind(p=7), k_number_d=selected_real_kind(p=18)
       real(kind=1) :: xsp=1.0
       real(kind=2) :: xdp=1.0d0
       real(kind=k_number_s) :: xs=1.0
       real(kind=k_number_d) :: xd=1.0d0, xsd1, xsd2
       
       xsd1=dle(xs)
       xsd2=real(xs,kind=k_number_d)
       
!! Saidas
       write(*,*)"Variavel precisao simples padrao: ",xsp
       write(*,*)"Variavel precisao dupla padrao: ",xdp
       write(*,*)"Variavel precisao simples: ",xs
       write(*,*)"Variavel precisao dupla: ",xd
       write(*,*)"Variavel precisao dupla: ",xsd1
       write(*,*)"Variavel precisao dupla: ",xsd2
       
end program funcao_kind
