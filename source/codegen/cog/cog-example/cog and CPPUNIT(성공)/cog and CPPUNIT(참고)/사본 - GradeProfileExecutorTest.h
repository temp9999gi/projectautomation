class GradeProfileExecutorTest : public CppUnit::TestCase
{
CPPUNIT_TEST_SUITE(GradeProfileExecutorTest);
//[[[cog import dyno_cog; dyno_cog.cppunit_macros('GradeProfileExecutorTest', cog.inFile) ]]]
CPPUNIT_TEST(testSetsFirstGradePercentInProfile_Time);
CPPUNIT_TEST(testSetsSecondGradePercent_Time);
CPPUNIT_TEST(testSetsGradePercent_WithInitialTime);
CPPUNIT_TEST(testReturnsFalseAtEndOfGradeProfile_Time);
CPPUNIT_TEST(testExecutorEndsWithFinalGradeValue);
CPPUNIT_TEST(testClearsStateAtEndOfProfile_Time);
CPPUNIT_TEST(testSetsFirstGradePercentInProfile_Distance);
CPPUNIT_TEST(testSetsLaterGradePercent_Distance);
CPPUNIT_TEST(testSetsLaterGradePercentStartingPartWayThroughProfile_Distance);
CPPUNIT_TEST(testSetsLaterGradePercentWhenInitialDistanceNotZero_Distance);
CPPUNIT_TEST(testSetsLaterGradePercentWhenInitialDistanceNotZero_DistanceResetInMiddle);
CPPUNIT_TEST(testEndsWhenMaxDistanceInProfileIsReached);
CPPUNIT_TEST(testConstructorThatTakesProfile);
CPPUNIT_TEST(testClearsInternalStateWhenFinished);
CPPUNIT_TEST(testProfileLoopsOnceWhenSetToRepeat_Distance);
CPPUNIT_TEST(testProfileLoopsOnceWhenSetToRepeat_Time);
CPPUNIT_TEST(testProfileLoopsManyTimesWhenSetToRepeat_Time);
CPPUNIT_TEST(testEmptyProfile);
//[[[end]]]
CPPUNIT_TEST_SUITE_END();


public:
GradeProfileExecutorTest();
virtual void setUp();
virtual void tearDown();


//[[[cog import dyno_cog; dyno_cog.cppunit_defs('GradeProfileExecutorTest', cog.inFile) ]]]
void testSetsFirstGradePercentInProfile_Time();
void testSetsSecondGradePercent_Time();
void testSetsGradePercent_WithInitialTime();
void testReturnsFalseAtEndOfGradeProfile_Time();
void testExecutorEndsWithFinalGradeValue();
void testClearsStateAtEndOfProfile_Time();
void testSetsFirstGradePercentInProfile_Distance();
void testSetsLaterGradePercent_Distance();
void testSetsLaterGradePercentStartingPartWayThroughProfile_Distance();
void testSetsLaterGradePercentWhenInitialDistanceNotZero_Distance();
void testSetsLaterGradePercentWhenInitialDistanceNotZero_DistanceResetInMiddle();
void testEndsWhenMaxDistanceInProfileIsReached();
void testConstructorThatTakesProfile();
void testClearsInternalStateWhenFinished();
void testProfileLoopsOnceWhenSetToRepeat_Distance();
void testProfileLoopsOnceWhenSetToRepeat_Time();
void testProfileLoopsManyTimesWhenSetToRepeat_Time();
void testEmptyProfile();
//[[[end]]]
};
