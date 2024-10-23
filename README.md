# Loan-calculator
### Hyperskill project


Description

Finally, let's add to our calculator the capacity to compute differentiated payments. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. Let’s look at the formula:

Dm=Pn+i⋅(P−P⋅(m−1)n)Dm​=nP​+i⋅(P−nP⋅(m−1)​)

Where:

DmDm​ = mmth differentiated payment;

PP = the loan principal;

ii = nominal interest rate. This is usually 1/12 of the annual interest rate and is a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.

nn = number of payments. This is usually the number of months in which repayments will be made.

mm = current repayment month.

In this stage, the user has to provide more inputs, so your program should be able to parse new command-line arguments. Let's add the --type one, so now the calculator should be run with 4 arguments:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

The --type argument is indicating the type of payment: "annuity" or "diff" (differentiated). It must always be provided in any run.

Also, it is possible that the user will make a mistake in the provided input. The program should not fail, but inform the user, that he has provided "Incorrect parameters".

    --type is specified neither as "annuity" nor as "diff" or not specified at all:

    > python creditcalc.py --principal=1000000 --periods=60 --interest=10
    Incorrect parameters

For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid:

> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters

Our loan calculator can't calculate the interest, so it must always be provided:

> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters

For differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters

Negative values should not be provided:

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters

