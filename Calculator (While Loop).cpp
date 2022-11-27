#include <iostream>

using namespace std;

int main()
{
    int a,b,c,s,d,p,q,x;
    char o;

    while(o != 'N')
    {

    cout<<"1 - Addition"<<endl;
    cout<<"2 - Subtraction"<<endl;
    cout<<"3 - Multiplication"<<endl;
    cout<<"4 - Division"<<endl;

    cout<<"\nEnter your choice: "<<endl;
    cin>>c;
    cout<<"Enter number 1: ";
    cin>>a;
    cout<<"Enter number 2: ";
    cin>>b;


    if(c==1)
        {
            x=a+b;
            cout<<"Answer is: "<<x<<endl;
            cout<<"Another? (Y/N): ";
            cin>>o;
        }

    else if(c==2)
        {
            x=a-b;
            cout<<"Answer is: "<<x<<endl;
            cout<<"Another? (Y/N): ";
            cin>>o;
        }

    else if(c==3)
        {
            x=a*b;
            cout<<"Answer is: "<<x<<endl;
            cout<<"Another? (Y/N): ";
            cin>>o;
        }

    else if(c==4)
        {
            x=a/b;
            cout<<"Answer is: "<<x<<endl;
            cout<<"Another? (Y/N): ";
            cin>>o;
        }

    else
        {
            cout<<"Wrong choice!"<<endl;
            cout<<"Another? (Y/N): ";
            cin>>o;
        }


    }

    return 0;
}
