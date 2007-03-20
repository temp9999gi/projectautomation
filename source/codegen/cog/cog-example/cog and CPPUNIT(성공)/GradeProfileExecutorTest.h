class GradeProfileExecutorTest : public CppUnit::TestCase
{
CPPUNIT_TEST_SUITE(GradeProfileExecutorTest);
//[[[cog import dyno_cog; dyno_cog.cppunit_macros('GradeProfileExecutorTest', cog.inFile) ]]]
CPPUNIT_TEST(testSetsGradePercent_WithInitialTime);
CPPUNIT_TEST(testReturnsFalseAtEndOfGradeProfile_Time);
//[[[end]]]
CPPUNIT_TEST_SUITE_END();


public:
GradeProfileExecutorTest();
virtual void setUp();
virtual void tearDown();


//[[[cog import dyno_cog; dyno_cog.cppunit_defs('GradeProfileExecutorTest', cog.inFile) ]]]
void testSetsGradePercent_WithInitialTime();
void testReturnsFalseAtEndOfGradeProfile_Time();
//[[[end]]]
};
