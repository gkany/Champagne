
#include <iostream>
#include <vector>
 
using std::cin;
using std::cout;
using std::endl;
using std::vector;
 
int main()
{
    vector<int> src;
 
    cout<<"请输入整形数组：";
    int temp;
    while (cin>>temp)
    {
        src.push_back(temp);
    }   
 
    cout<<"good: "<<cin.good()<<endl;
    cout<<"eof: "<<cin.eof()<<endl;
    cout<<"fail: "<<cin.fail()<<endl;
    cout<<"bad: "<<cin.bad()<<endl;
 
    cin.clear();
    cout<<"good: "<<cin.good()<<endl;
    cout<<"eof: "<<cin.eof()<<endl;
    cout<<"fail: "<<cin.fail()<<endl;
    cout<<"bad: "<<cin.bad()<<endl;
 
    int target;
 
    cout<<"请输入需查找数：";
    cin>>target;
}
