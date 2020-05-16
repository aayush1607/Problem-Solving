// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

void toh(int n, int from, int to, int aux, long long &moves);

int main() {

    int T;
    cin >> T;
    while (T--) {
        long long moves = 0;
        int N;
        cin >> N;
        toh(N, 1, 3, 2, moves);
        cout << moves << endl;
    }
    return 0;
}
// } Driver Code Ends


// You need to complete this function

// avoid space at the starting of the string in "move disk....."
void toh(int N, int from, int to, int aux, long long &moves) {
    // Your code here
    if(N==1)
    {
        moves++;
        
        cout<<"move disk "<<N<<" from rod "<<from<<" to rod "<<to<<endl;
        return;
    }
    
    
    toh(N-1,from,aux,to,moves);
    moves++;
    cout<<"move disk "<<N<<" from rod "<<from<<" to rod "<<to<<endl;

    toh(N-1,aux,to,from,moves);
}