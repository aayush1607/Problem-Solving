# Problem-Solving
PROBLEM SOLVING FOR CODING INTERVIEW AND COMPETITIVE PROGRAMMING.

-ALGORITHM ANALYSIS.
-MATHS.
-DATA STRUCTURES AND ALGORITHMS.


1.ALGORITHM ANALYSIS:
    ALGORITHM-It is step by step unambigous instructions to solve  problem.

    It should be Correct+Efficient.

    Comparison of algorithms is not done by Execution time or no. of statements because this parameters can differ from machine to machine and programmer to programmer respectively.

    Comparison should be independent of machine time, Programming style.

    The reason for this is that one algorithm may take 1s in a fast modern pc and may take 5s in an old computer. So we can tell absolutely that one algorithm is best.
    We need to be relative and neglect some parameters that vary machine to machine.

    So, Ideally we assume and express the running time of a given algorithm as a function of input size n f(n) and compare those functions.

    ASYMPTOTIC NOTATIONS- For representaion of expressions for best avg and worst cases we use a form of function f(x)

    1. Big O NOTATIONS--UPPER BOUND
    2. OMEGA NOTATIONS--LOWER BOUND
    3. THETA NOTATIONS--TIGHT BOUND
    4. SMALL-o NOTATIONS.
    5. SMALL-omega NOTATIONS.

    REFER-  
     https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/
     https://www.geeksforgeeks.org/properties-of-asymptotic-notations/
     https://www.geeksforgeeks.org/analysis-of-algorithems-little-o-and-little-omega-notations/?ref=rp

    Also go through book included for detailed study.


    ANALYSIS OF TIME COMPLEXITY:
    1. MASTER THEOREM
        .FOR DIVIDE AND CONQUER -- https://www.geeksforgeeks.org/advanced-master-theorem-for-divide-and-conquer-recurrences/
        .FOR SUBTRACT AND CONQUER -- https://www.geeksforgeeks.org/master-theorem-subtract-conquer-recurrences/

    2. RECURSION TREE METHOD.(RECOMMENDED) --https://www.geeksforgeeks.org/analysis-algorithm-set-4-master-method-solving-recurrences/

    3. SUBSTITUTION METHOD.


2.MATHS

    A.BASIC MATHS
    
        IMPORTANT SERIES:
            1.  1+2+3+...N= N(N+1)/2

            2.  1+x+x^2+x^3+......x^n = (x^(n+1)-1)(x-1)

            3.  1+(1/2)+(1/3)+(1/4)+.....(1/n)= log(n)

            4.  log(1)+log(2)+....log(n)= n*log(n)

            5.  (1^p)+(2^p)+(3^p)+....(n^p)=(n^(p+1))/(p+1)

            6. 1/2+1/3+1/5+...1/n= log(log(n))     (for sigma(1/k) k is prime number)

            AP AND GP FORMULAS.

            AP-

            1. tn= a+(n-1)d
            2. Sn= n/2(2a+(n-1)d)= n/2(a+l)
            3. if n is even
                    sum of even terms-sum of odd terms = (nd/2)


            GP-

            1. tn= a* r^(n-1)

            2. Sn =
                    a(r^n - 1)/(r-1) if (r>1)

                    a(1 - r^n)/(1-r) if (r<1)


                    if(r<<1)
                    S(inf)= a/(r-1)

        .PRIME NUMBERS
        .FACTORS
        .LCM
        .GCD/HCF
        .P AND C
        .MODULAR INVERSE
        .EULER TOTIENT FUNCTION


    B. NUMBER THEORY

        1.  MODULAR ARITHMETIC
        2.  MODULAR EXPONENTIATION
        3.  GCD/HCF
        4.  EUCLID'S ALGORITHM --O(MAX(log(A,B)))
        5.  EXTENDED EUCLIDEAN ALGORITHM --O(MAX(log(A,B)))
        6.  PRIME NUMBERS
                    A. CHECK IF PRIME NUMBER- O(sqrt(n)) APPROACH
                    B. SIEVE OF ERATHOTHENES APPROACH FOR FINDNG ALL PRIME NO.S LESS THAN N
                                a. find for 1-N classic -O(n log(log(n)))
                                b. Manipualed for 1-N  -O(N)
                                c. For range [L-R] -O(sqrt(R))
                    C. FERMANT LITTLE METHOD.
        7.  PRIME FACTORIZATION
                    A. FIND PRIME FACTORS--O(sqrt(n)
                    B. USING SIEVE --O(log(N))

        8.  LCM
                A.  FOR TWO NUMBERS-USING GCD*LCM=a*b FORMULA. --O(MAX(log(A,B)))

                B.  FOR ARRAY OF INTEGERS - STILL USE FORMULA BUT SLIGHT CHANGE.


        9.  MODULAR MULTIPLICATIVE INVERSE

                FOR GIVEN A and M FIND: B SUCH THAT (A*B)%M=1 ASLO ALWAYS GCD(A,M)=1.


                A. NAIVE- B IS FROM [1-M-1]                                       --O(M)
                B. EXTENDED EUCLID GCD(A,M)=Ax+My=1 use theorem                   --O(log(max(A,M)))
                C. FERMATS LITTLE THEOREM ONLY WHEN N IS PRIME                    --O(log(M))

        10. TOTIENT FUNCTION

                IT IS A FUNCTION REALTED TO FIND COUNT OF NUMBERS THAT ARE COPRIME WITH A NUMBER X AND ARE LESS THAT OR EQUAL TO X.

                SO FOR GIVEN X WE NEED TO COUNT ALL NO.S Yi where GCD(X,Yi)=1 and 1<=Yi<=X.

                A.NAIVE --O(nlog(n))
                B.Eulers formula
                        f(x)= x*( product of all (1-1/p) for all prime factors of n) --O(log(n))



                imp facts :
                        -sum of all values of totient fxn of all divisors of n =n.
                        - value of totient fxn for prime numbers f(p)=p-1.
                        - if gcd(a,b)=1 then f(a)*f(b)=f(a,b) f is totient fxn here.


    C.BIT MANIPULATION

            1. BITWISE OPERATORS
            2. SET UNSET Kth bit and also check.
                    -shifting.
                    -merging and masking.
                    -swapping

            3. Powers of two.
            4. Power set.


3.DATA STRUCTURES AND ALGORITHMS


    A. DATA STRUCTURES

            1. ARRAYS
            2. LINKED LISTS
            3. STACK
            4. QUEUE
            5. TREE
            6. HEAP
            7. GRAPH
            8. TRIE
            9. SEGMENT TREE
            10. DISJOINT SET

    B. ALGORITHMS
            1. RECURSION
            2. SEARCHING
            3. SORTING
            4. MATRIX
            5. HASHING
            6. STRINGS
            7. GREEDY
            8. BACKTRACKING
            9. DYNAMIC PROGRAMMING
            10. GRAPH ALGORITHMS



#DATA STRUCTURES AND ALGORITHMS to be updated soon.
