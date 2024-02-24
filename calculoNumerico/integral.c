// Autor - Jonatan P. Paschoal
// Data 24-fev-2024
// Integral numerica
// I_retangulo ~ (b-a)*f[(a+b)/2] -- Retangulos
// I_trapezio ~ (b-a)*[(f(a)+f(b))/2] -- Trapezios
// I_simpson ~ (b-a)*[(f(a)+4f[(a+b)/2]f(b))/6] -- Media ponderada

#include<stdio.h>
#include<math.h>

int main(){
        double x,dx;
        double I1,I2,I3,I4;
        double r1,r2,r3;
        
        dx=0.05;
        I1=0.;
        I2=0.;
        I3=0.;
        
        // f(x)=exp{x} --> I = exp{x}
        for(x=0.;x<=1.;x=x+dx){
        // Regra do retangulo 
                r1=dx*(exp((x+x+dx)*0.5));
                I1=I1+r1;
        // Regra do trapezio
                r2=(exp(x)+exp(x+dx))*dx/2.;
                I2=I2+r2;
        // Regra de simpson
                r3=(exp(x)+4.*(exp((x+x+dx)*0.5))+exp(x+dx))*dx/6.;
                I3=I3+r3;
                
                printf("%13.8f %13.8f %13.8f \n", I1,I2,I3); // Integrais
        }        
        
        // Integral exata
        I4=exp(1.)-1.;
        printf("\n");
        printf("%13.8f %13.8f %13.8f %13.8f \n", I1,I2,I3,I4); // Integrais
        printf("\n");
        printf("%13.8f %13.8f %13.8f %13.8f \n", fabs(I4-I1),fabs(I4-I1),fabs(I4-I1),fabs(I4-I1)); // Diferenca

        return 0;
}

