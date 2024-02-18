// Autor - Jonatan
// Data 27-mar-2023
// Derivada numérica - f'(x)=[f(x+h)-f(x-h)]/2h (série de taylor) ou f'(x)=[f(x+h)-f(x)]/h (definição)

#include<stdio.h>
#include<math.h>

int main(){
        double f0,f1,f2,h,x;
        double d1,d2,d3;
        
        // f(x)=ln(x) --> df/dx=1/x (derivada exata)
        
        x=2.;
        h=0.1;
        
        //log() - logaritmo natural "ln"
        
        f2=log(x+h); // f(x+h)        
        f1=log(x); // f(x)
        f0=log(x-h); // f(x-h)

        d1=(f2-f0)/(2.*h); //(f(x+h)-f(x-h))/2*h
        d2=(f2-f1)/h; // f(x+h)-f(x)/h
        d3=1./x;        
        
        printf("%13.8f %13.8f %13.8f \n", d1,d2,d3); // Derivadas
        printf("%13.8f %13.8f \n", fabs(d1-d3),fabs(d2-d3)); // Diferença das derivadas

        return 0;
}

