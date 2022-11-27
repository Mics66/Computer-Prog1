#include <iostream>
using namespace std;


int main()
{
   char x, y, r, p, s;
   string choice;

    while ((choice!="N")&&(choice!="n")&&(choice!="No")&&(choice!="no"))
    {
      system("CLS");


    cout << "RPS Game \n";
    cout << "type 'r' for rock \n";
    cout << "type 'p' for paper \n";
    cout << "type 's' for scissor \n";

    cout << "Player 1: ";
    cin >> x;
    cout << "Player 2: ";
    cin >> y;

  if(x=='r' && y=='s'){
      cout<<"\nPlayer 1 Won!"<<endl;
      cout<<"Player 2 Lost!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }

  else if(x=='p' && y=='r'){
      cout<<"\nPlayer 1 Won!"<<endl;
      cout<<"Player 2 Lost!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }

  else if(x=='s' && y=='p'){
      cout<<"\nPlayer 1 Won!"<<endl;
      cout<<"Player 2 Lost!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }

  else if(x=='r' && y=='p'){
      cout<<"\nPlayer 2 Won!"<<endl;
      cout<<"Player 1 Lost!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }

  else if(x=='p' && y=='s'){
      cout<<"\nPlayer 2 Won!"<<endl;
      cout<<"Player 1 Lost!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }

  else if(x=='s' && y=='r'){
      cout<<"\nPlayer 2 Won!"<<endl;
      cout<<"Player 1 Lost!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }

    else if(x==y){
      cout<<"\nIt's a tie!"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }


  else{
      cout<<"Invalid Input"<<endl;
      cout<<"Do you want to play another game? (Y/N)";
      cin>> choice;
  }
    }

  return 0;
}
