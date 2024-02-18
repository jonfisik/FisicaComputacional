// Autor - Jonatan
// Data 27-mar-2023
// Derivada numérica com 3 pontos
// f(x) -- {f(x1),f(x2),f(x3),...}
// f'(x_k) = (1/2h)*(-3*f(x_k)+4*f(x_k+h)-f(x_k+2h))
// f'(x_k) = (1/2h)*(f(x_k-2h)-4*f(x_k-h)+3*f(x_k)) 

#include<stdio.h>
#include<math.h>

int main(){
        double f0,f1,f2,h,x;
        double d1,d2,d3;
        
        // f(x)=ln(x) --> df/dx=1/x
        
        x=2.;
        h=0.005;
        
        //log() - logaritmo natural "ln"
        
        f2=log(x+2.*h); // f(x+2h)        
        f1=log(x+h); // f(x+h)
        f0=log(x); // f(x)

        d1=(-3*f0+4.*f1-f2)/(2.*h); //(f(x+h)-f(x-h))/2*h
        
        f2=log(x-2.*h); // f(x-2h)        
        f1=log(x-h); // f(x-h)
        f0=log(x); // f(x)
        
        d2=(f2-4.*f1+3.*f0)/(2.*h); // df/dx=(f(x-2h)-4f(x-h)+3f(x))/*h
     
        d3=1./x;        
        
        printf("%13.8f %13.8f %13.8f \n", d1,d2,d3); // Derivadas
        printf("%13.8f %13.8f \n", fabs(d1-d3),fabs(d2-d3)); // Diferença das derivadas

        return 0;
}

