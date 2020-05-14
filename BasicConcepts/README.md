1.INPUT-OUTPUT

        a.Sometimes input and output is bottleneck in program. So, following lines can be included for making it efficient in c++:

            ios::sync_with_stdio(0);
            cin.tie(0);

        Also note: "\n" works faster than endl as endl always causes a flush operation.

        b.If you want to read whole input line containing spaces then you can us getline function:

            string s;
            getline(cin,s);
        
        c.If amount of data is unknown and don't know where to stop:

            while(cin>>x){
                //code
            }
        
        d.If want to use file for input and output the just include these lines in beginning:


            freopen("input.txt","r",stdin);
            freopen("output.txt","r",stdout);

2.NUMBERS:

        -Most used integer type ---int--32bit integer. value ranges from (-2^31 to 2^31-1) about (-2*10^9 to + 2*10^9)

        -for long long --long long--64bit integer. value ranges from (-2^63 to 2^63) about (-9*10^18 to +9*10^18)

        
        WRONG CODE:

                    int a = 123456789;
                    long long b= a*a;
                    cout<<b;

                    here result of a*a will be in int and will not produce expected answer in long long;

        RIGHT CODE:
                    long long a=123456789;
                    long long b= a*a;
                    cout<<b;

        
        -Comparing Floats:

            example:

                    double x= 0.3*3 + .1;
                    cout<<x; 

                    It may not give output 1.It is because some numbers cannot be represented accurately in float and there are rounding errors.

            Correct way to compare float:

                    if( abs(a-b) < 1e-9){
                        //a and b are equal.
                    } 


3.CODE SHORTEN AND SHORTCUTS:


        TYPE-NAMES:

            typedef long long ll;

            typedef vector<int> v;

            typedef pair<int,int> pi;

        MACROS:

            A macro specifies that certaing strings are replaced before compilation.

            #define f first;
            #define s first;
            #define pb push_back;
            #define mp make_pair;

            #define fo(i,n) for(int i=0;i<n;i++)
            #define fo(i,a,b) for(int i=a;i<=b;i++)
            









        
