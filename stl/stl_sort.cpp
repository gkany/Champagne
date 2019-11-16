#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <functional>
#include <string>
using namespace std;

// g++ stl_sort.cpp -std=c++11

//1. sort
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
    return out << name.first << " " << name.second << ", ";
}

void test_name_sort()
{
    std::vector<Name> names;
    std::cout <<  "Enter names as first name followed by second name." << endl;
    std::cout << "[linux] Ctrl+D | [windows] Ctrl+Z" << endl;
    std::copy(std::istream_iterator<Name>(std::cin), std::istream_iterator<Name>(), std::back_insert_iterator<std::vector<Name>>(names));
    
    std::cin.clear();
    std::cin.sync();

    std::cout << "size: " << names.size() << ", names sort:" << endl;
    std::sort(std::begin(names), std::end(names), [](const Name& n1, const Name& n2) { return n1.get_second() < n2.get_second(); });

    std::copy(std::begin(names), std::end(names), std::ostream_iterator<Name>{ std::cout, " " });
    std::cout << std::endl;
}

void test_sort()
{
    std::cout << "1. test stl sort" << std::endl;
    vector<int> v1 {99, 77, 33, 66, 22, 11, 44, 37};
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " " });
    std::cout << std::endl << "------------ sort:" << std::endl;
    test_sort1();
    test_sort2();
    test_sort3();
    //test_name_sort();
}

//stable_sort
void test_stable_sort()
{
    std::cout << std::endl << "2. test stl  stable sort" << std::endl;
    vector<int> v1 {99, 77, 33, 66, 22, 77, 11, 44, 37};
    std::cout << "before sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::stable_sort(std::begin(v1), std::end(v1));
    std::cout <<  std::endl << "after sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    //std::cout << std::endl;
    //std::stable_sort(std::begin(v1), std::end(v1), [](int a, int b){ return a > b; });
    std::stable_sort(std::begin(v1), std::end(v1), std::greater<int>());
    std::cout <<  std::endl << "after sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::cout << std::endl;

}

//partial_sort
void test_partial_sort()
{
    std::cout << std::endl << "3. test stl  partial sort" << std::endl;
    vector<int> v1 {22, 7, 93, 45, 19, 56, 88, 12, 8, 7, 15, 10}; 
    std::cout << "before sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});

    size_t count = 5;
    std::partial_sort(std::begin(v1), std::begin(v1)+count, std::end(v1));
    std::cout <<  std::endl << "after sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});

    //std::cout << std::endl;
    //std::stable_sort(std::begin(v1), std::begin(v1)+count, std::end(v1), [](int a, int b){ return a > b; });
    std::partial_sort(std::begin(v1), std::begin(v1)+count, std::end(v1), std::greater<int>());
    std::cout <<  std::endl << "after sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::cout << std::endl;

}

//partial_sort_copy
void test_partial_sort_copy()
{
    std::cout << std::endl << "4. test stl  partial sort" << std::endl;
    vector<int> v1 {22, 7, 93, 45, 19, 56, 88, 12, 8, 7, 15, 10}; 
    std::cout << "before sort:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});

    size_t count = 5;
    std::vector<int> v2(count);
    std::partial_sort_copy(std::begin(v1), std::end(v1), std::begin(v2), std::end(v2));
    //std::cout <<  std::endl << "after sort: v1: " << std::endl;
    //std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::cout <<  std::endl << "result v2: " << std::endl;
    std::copy(std::begin(v2), std::end(v2), std::ostream_iterator<int>{ std::cout, " "});
    
    std::partial_sort_copy(std::begin(v1), std::begin(v1)+count, std::begin(v2), std::end(v2));
    //std::cout <<  std::endl << "after sort: v1: " << std::endl;
    //std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::cout <<  std::endl << "result v2: " << std::endl;
    std::copy(std::begin(v2), std::end(v2), std::ostream_iterator<int>{ std::cout, " "});
    
    //std::cout << std::endl;
    //std::stable_sort(std::begin(v1), std::begin(v1)+count, std::end(v1), [](int a, int b){ return a > b; });
    //std::partial_sort(std::begin(v1), std::begin(v1)+count, std::end(v1), std::greater<int>());
    std::partial_sort_copy(std::begin(v1), std::end(v1), std::begin(v2), std::end(v2), std::greater<int>());
    //std::cout <<  std::endl << "after sort: v1: " << std::endl;
    //std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::cout <<  std::endl << "result v2: " << std::endl;
    std::copy(std::begin(v2), std::end(v2), std::ostream_iterator<int>{ std::cout, " "});
    std::cout << std::endl;

}


//nth_element
void test_nth_element()
{
    std::cout << std::endl << "5. test stl nth element" << std::endl;
    std::vector<int> v1 {22, 7, 93, 45, 19, 56, 88, 12, 8, 7, 15, 10};
    std::cout << "origin data:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{std::cout, " "});
    size_t count = 5;
    std::nth_element(std::begin(v1), std::begin(v1)+count, std::end(v1));
    std::cout << std::endl << "after nth element:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{std::cout, " "});
    std::cout << std::endl;

    
    std::nth_element(std::begin(v1), std::begin(v1)+count, std::end(v1), std::greater<int>());
    std::cout << std::endl << "after nth element:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{std::cout, " "});
    std::cout << std::endl;
}

void test_is_sorted()
{
    std::cout << std::endl << "6. test stl is_sorted" << std::endl;
    std::vector<int> v1 {22, 7, 93, 45, 19, 56, 88, 12, 8, 7, 15, 10};
    std::cout << "origin data:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{std::cout, " "});
    std::cout << std::endl << ((std::is_sorted(std::begin(v1), std::end(v1))) ? "is sorted" : "not sorted") << std::endl;
    
    std::sort(std::begin(v1), std::end(v1));
    std::cout << std::endl << "after nth element:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{std::cout, " "});
    std::cout << std::endl << ((std::is_sorted(std::begin(v1), std::end(v1))) ? "is sorted" : "not sorted") << std::endl;
    std::cout << std::endl << ((std::is_sorted(std::begin(v1), std::end(v1), std::greater<int>())) ? "is sorted" : "not sorted") << std::endl;
}

void test_is_sorted_until()
{
    std::cout << std::endl << "7. test stl is_sorted_until" << std::endl;
    std::vector<int> v1 {1, 2, 3, -1, 10, 11, 30, 9, 40, 42};
    std::cout << "origin data:" << std::endl;
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{std::cout, " "});
    std::cout << std::endl << "result: " << std::endl;
    std::copy(std::begin(v1), std::is_sorted_until(std::begin(v1), std::end(v1)), std::ostream_iterator<int>{std::cout, " "});
    std::cout << std::endl;
}

void test_merge()
{
    std::cout << std::endl << "8. test stl merge" << std::endl;
    vector<int> v1 {1, 21, 11, 9, 39, 7, 5};
    vector<int> v2 {3, 17, 9, 33, 42, 6, 8, 16, 6};

    std::cout << "sort v1: " << std::endl;
    std::stable_sort(std::begin(v1), std::end(v1));
    std::copy(std::begin(v1), std::end(v1), std::ostream_iterator<int>{ std::cout, " "});
    std::cout << std::endl << "sort v2: " << std::endl;
    std::stable_sort(std::begin(v2), std::end(v2));
    std::copy(std::begin(v2), std::end(v2), std::ostream_iterator<int>{ std::cout, " "});

    std::cout << std::endl << "merge v1, v2 => v3:" << std::endl;
    std::vector<int> v3(v1.size()+v2.size());
    std::merge(std::begin(v1), std::end(v1), std::begin(v2), std::end(v2), std::begin(v3));
    std::copy(std::begin(v3), std::end(v3), std::ostream_iterator<int>{ std::cout, " "});
    std::cout << std::endl;
}

void test()
{
    test_sort();
    test_stable_sort();
    test_partial_sort();
    test_partial_sort_copy();
    test_nth_element();
    test_is_sorted();
    test_is_sorted_until();
    test_merge();
}

int main()
{
    test();

    return 0;
}

