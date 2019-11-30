#define CATCH_CONFIG_MAIN
#include "catch.hpp"

unsigned int fact(unsigned int num) {
    return num <= 1 ? num : fact(num-1)*num;
}

TEST_CASE("fact are computed", "[fact]") {
    REQUIRE(fact(1) == 1);
    REQUIRE(fact(2) == 2);
    REQUIRE(fact(3) == 6);
    REQUIRE(fact(10) == 362880);
}

