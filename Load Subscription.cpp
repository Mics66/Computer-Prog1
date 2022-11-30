 #include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int x, y;

    while(y!=10)
    {
        system("CLS");

    cout << "GLOBE PROMO FOR P50:" << endl;
    cout << "1) Go50" << endl;
    cout << "2) GoUNLI50" << endl;
    cout << "3) GoSURF50" << endl;
    cout << "\nEnter choice: " << endl;
    cin>>x;
    system("CLS");

    switch(x){
        case 1:
            system("CLS");
            cout << "5GB all-access data + 1GB GoWiFi" << endl;
            cout << "+ unli all net texts for 3 days." << endl;
            cout << "\n1) SUBSCRIBE" << endl;
            cout << "2) BACK" << endl;
            cout << "3) CANCEL" << endl;
            cout << "\nEnter choice: " << endl;
            cin>>y;

            if(y==1){
                cout << "Congratulations! You are now subscribed to the PROMO!" << endl;
                y=10;
                break;
            }

            else if(y==2){
                break;
            }

            else if(y==3){
                y=10;
                break;
            }


            case 2:
            system("CLS");
            cout << "Unli calls and texts to all networks" << endl;
            cout << "+ 500MB of mobile data for 3 days." << endl;
            cout << "\n1) SUBSCRIBE" << endl;
            cout << "2) BACK" << endl;
            cout << "3) CANCEL" << endl;
            cout << "\nEnter choice: " << endl;
            cin>>y;

            if(y==1){
                cout << "Congratulations! You are now subscribed to the PROMO!" << endl;
                y=10;
                break;
            }

            else if(y==2){
                break;
            }

            else if(y==3){
                y=10;
                break;
            }

            case 3:
            system("CLS");
            cout << "2GB all-access data* + unli texts to all networks " << endl;
            cout << "+ 1GB daily for your choice of GoWATCH&PLAY, GoSHARE&SHOP, GoLISTEN&TRAVEL, or GoLEARN&WORK" << endl;
            cout << "+ 1GB GoWiFi access for 3 days." << endl;
            cout << "\n1) SUBSCRIBE" << endl;
            cout << "2) BACK" << endl;
            cout << "3) CANCEL" << endl;
            cout << "\nEnter choice: " << endl;
            cin>>y;

            if(y==1){
                cout << "Congratulations! You are now subscribed to the PROMO!" << endl;
                y=10;
                break;
            }

            else if(y==2){
                break;
            }

            else if(y==3){
                y=10;
                break;
            }
    }

}
    return 0;
}
