class unit-- : public CppUnit::TestCase
{
CPPUNIT_TEST_SUITE(unit--);
//[[[cog import dyno_cog; dyno_cog.cppunit_macros('unit--', cog.inFile) ]]]
//[[[end]]]
CPPUNIT_TEST_SUITE_END();


public:
unit--();
virtual void setUp();
virtual void tearDown();


//[[[cog import dyno_cog; dyno_cog.cppunit_defs('unit--', cog.inFile) ]]]
//[[[end]]]
};
