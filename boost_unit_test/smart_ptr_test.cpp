#define BOOST_TEST_MODULE maintest

#include <boost/test/unit_test.hpp>
#include <boost/smart_ptr.hpp>

using namespace boost;
using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE(suite_smart_ptr_test)

BOOST_AUTO_TEST_CASE(t_scoped_ptr) {
    scoped_ptr<int> p(new int(874));
    BOOST_CHECK(p);
    BOOST_CHECK_EQUAL(*p, 875);

    p.reset();
    BOOST_CHECK(p == 0);
}


BOOST_AUTO_TEST_SUITE_END()

