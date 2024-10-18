#include <iostream>
using namespace std;

int main()
{

    char s;
    int n;
    cout << "Enter direction: ";
    cin >> s;
    cout << "Enter action: ";
    cin >> n;
    switch (s)
    {
        case 'N':
            break;
        case 'W':
            break;
        case 'S':
            break;
        case 'E':
            break;
    }
    switch (n) {
        case 1:
            if (s == 'N')
                cout << "Continue West";
            if (s == 'W')
                cout << "Continue South";
            if (s == 'E')
                cout << "Continue North";
            if (s == 'S')
                cout << "Continue South";
            break;
        case -1:
            if (s == 'N')
                cout << "Continue East";
            if (s == 'W')
                cout << "Continue North";
            if (s == 'E')
                cout << "Continue South";
            if (s == 'S')
                cout << "Continue West";
            break;
        case 0:
            if (s == 'N')
                cout << "Continue North";
            if (s == 'W')
                cout << "Continue West";
            if (s == 'E')
                cout << "Continue East";
            if (s == 'S')
                cout << "Continue South";
            break;
    }
}



