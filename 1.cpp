#include <bits/stdc++.h>
using namespace std;
int main(){
 	int n, m, k;
    cin >> n >> m >> k;
    int x = max(n, max(m, k));
    if(x > 727 || x < 94){
    	cout << "Error";
    }
    else
        cout << x;
    return 0;
}