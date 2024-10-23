import argparse                                                                                                                       
import math                                                                                                                           
import io                                                                                                                             
from contextlib import redirect_stderr                                                                                                
                                                                                                                                      
                                                                                                                                      
def calculo_A(P, n, i):                                                                                                               
    amount = 0                                                                                                                        
    m = 1                                                                                                                             
    while m <= n:                                                                                                                     
        A = math.ceil(P / n + i *(P - (P * (m - 1)) / n))                                                                             
        amount += A                                                                                                                   
        print(f'Month {m}: payment is {A}')                                                                                           
        m += 1                                                                                                                        
    overpayment = amount - P                                                                                                          
    print('')                                                                                                                         
    return overpayment                                                                                                                
                                                                                                                                      
                                                                                                                                      
def calculo_A_annuity(P,calculo_interes,n):                                                                                           
    A = math.ceil(P * calculo_interes)                                                                                                
    overpayment = n * A - P                                                                                                           
    return A, overpayment                                                                                                             
                                                                                                                                      
def calculo_P(A, calculo_interes, n):                                                                                                 
    P = int(A / calculo_interes)                                                                                                      
    overpayment = math.ceil(A * n - P)                                                                                                
    return P, overpayment                                                                                                             
                                                                                                                                      
                                                                                                                                      
def calculo_n(A, i, P):                                                                                                               
    x = A / (A - i * P)                                                                                                               
    n = math.ceil(math.log(x, 1 + i))                                                                                                 
    anyos = n // 12                                                                                                                   
    meses = n - (anyos * 12)                                                                                                          
    overpayment = math.ceil(n * A - P)                                                                                                
    return anyos, meses, overpayment                                                                                                  
                                                                                                                                      
                                                                                                                                      
def exit_programa():                                                                                                                  
    print('Incorrect parameters')                                                                                                     
    exit()                                                                                                                            
                                                                                                                                      
                                                                                                                                      
def check_parametros(interest, type_int, payment, principal, periods):                                                                
    inputs = [interest, type_int, payment, principal, periods]                                                                        
    cuenta_none = 0                                                                                                                   
    for z in inputs:                                                                                                                  
        if z is None:                                                                                                                 
            cuenta_none += 1                                                                                                          
        elif not isinstance(z, str):                                                                                                  
            if z < 0:                                                                                                                 
                exit_programa()                                                                                                       
                                                                                                                                      
    if interest is None or type_int is None or (type_int == 'diff' and payment != None) or cuenta_none > 1:                           
        exit_programa()                                                                                                               
                                                                                                                                      
                                                                                                                                      
def error_eleccion(string):                                                                                                           
    if string not in ('diff', 'annuity'):                                                                                             
        exit_programa()                                                                                                               
                                                                                                                                      
                                                                                                                                      
def pintar_overpayment(overpayment):                                                                                                  
    print(f'Overpayment = {overpayment}')                                                                                             
                                                                                                                                      
                                                                                                                                      
def main():                                                                                                                           
    parser = argparse.ArgumentParser(description='''This program calculates \n                                                           
    the annuity payment.''')                                                                                                            
                                                                                                                                      
    parser.add_argument("--payment", type=float)                                                                                      
    parser.add_argument("--principal", type=int)                                                                                      
    parser.add_argument("--periods", type=int)                                                                                        
    parser.add_argument("--interest", type=float)                                                                                     
    parser.add_argument("--type_int", choices=["annuity", "diff"])                                                                    
                                                                                                                                      
    try:                                                                                                                              
        f = io.StringIO()                                                                                                             
        with redirect_stderr(f):                                                                                                      
            args = parser.parse_args()                                                                                                
    except:                                                                                                                           
        exit_programa()                                                                                                               
                                                                                                                                      
    check_parametros(args.interest, args.type_int, args.payment, args.principal, args.periods)                                        
                                                                                                                                      
    # defino las variables                                                                                                            
    A = args.payment                                                                                                                  
    P = args.principal                                                                                                                
    n = args.periods                                                                                                                  
    i = args.interest / 12 / 100                                                                                                      
    m = args.type_int                                                                                                                 
                                                                                                                                      
    if args.periods:                                                                                                                  
        # 1 + i elevado a n                                                                                                           
        interes_total = math.pow(1 + i, n)                                                                                            
        calculo_interes = (i * interes_total / (interes_total - 1))                                                                   
                                                                                                                                      
    if args.payment == None:                                                                                                          
        if m == 'diff':                                                                                                               
            overpayment = calculo_A(P, n, i)                                                                                          
        elif m == 'annuity':                                                                                                          
            payment, overpayment = calculo_A_annuity(P, calculo_interes, n)                                                           
            print(f'Your annuity payment = {payment}!')                                                                               
                                                                                                                                      
                                                                                                                                      
    if args.principal == None and m == 'annuity':                                                                                     
        P, overpayment = calculo_P(A, calculo_interes, n)                                                                             
        print(f'Your loan principal = {P}!')                                                                                          
                                                                                                                                      
    if args.periods == None:                                                                                                          
        anyos, meses, overpayment = calculo_n(A, i, P)                                                                                
        if anyos > 0 and meses > 0:                                                                                                   
            print(f'It will take {anyos} years and {meses} months to repay this loan!')                                               
        elif meses > 0:                                                                                                               
            print(f'It will take {meses} months to repay this loan!')                                                                 
        elif anyos > 0:                                                                                                               
            print(f'It will take {anyos} years to repay this loan!')                                                                  
                                                                                                                                      
    pintar_overpayment(overpayment)                                                                                                   
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
if __name__ == '__main__':                                                                                                            
    main()                                                                                                                            
