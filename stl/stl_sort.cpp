#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <functional>
#include <string>
using namespace std;

void test_sort1()
{
    vector<int> v1 {99, 77, 33, 66, 22, 11, 44, 37};
    sort(v1.begin(), v1.end());
    std::copy(v1.begin(), v1.end(), std::ostream_iterator<int>{ std::cout, " " });
    cout << endl;
}

void test_sort2()
{
    vector<int> v1 {99, 77, 33, 66, 22, 11, 44, 37};
    //sort(std::begin(v1), std::end(v1), std::greater<int>());
    sort(std::begin(v1), std::end(v1), [](int a, int b)->bool { return a > b; });
    std::copy(v1.begin(), v1.end(), std::ostream_iterator<int>{ std::cout, " " });
    cout << endl;
}

void test_sort3()
{
    vector<int> v1 {99, 77, 33, 66, 22, 11, 44, 37};
    sort(std::begin(v1)+2, std::end(v1)-1, std::less<int>());
    //sort(std::begin(v1), std::end(v1), [](int a, int b)->bool { return a > b; });
    std::copy(v1.begin(), v1.end(), std::ostream_iterator<int>{ std::cout, " " });
    cout << endl;
}

//sort struct Name
class Name
{
public:
    Name(const std::string& n1, const std::string& n2)
        : first(n1), second(n2) {}
    Name() = default;

    std::string get_first() const { return first; }
    std::string get_second() const { return second; }

    friend std::istream& operator>> (std::istream& in, Name& name);
    friend std::ostream& operator<<(std::ostream& out, const Name& name);

private:
    std::string first {};
    std::string second {};    
};


inline std::istream& operator>> (std::istream& in, Name& name)
{
    return in >> name.first >> name.second;
}
inline std::ostream& operator<<(std::ostream& out, const Name& name)
{
    return out << name.first << ", " << name.second;
}

void test_name_sort()
{
    std::vector<Name> names;
    std::cout <<  "Enter names as first name followed by second name. Enter Ctrl+Z to end:";
    std::copy(std::istream_iterator<Name>(std::cin), std::istream_iterator<Name>(), std::back_insert_iterator<std::vector<Name>>(names));
    
    std::cout << "size: " << names.size() << ", names sort:" << endl;
    std::sort(std::begin(names), std::end(names), [](const Name& n1, const Name& n2) { return n1.get_second() < n2.get_second(); });

    std::copy(std::begin(names), std::end(names), std::ostream_iterator<Name>{ std::cout, " " });
}

void test_sort()
{
    vector<int> v1 {99, 77, 33, 66, 22, 11, 44, 37};
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " " });
    std::cout << std::endl << "------------ sort:" << std::endl;
    test_sort1();
    test_sort2();
    test_sort3();
    test_name_sort();
}

void test()
{
    test_sort();
}

int main()
{
    test();

    return 0;
}
