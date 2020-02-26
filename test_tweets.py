import twitterHW2
#can only test certain tests on local

def test_compare(): #these tests test the threading system set up but cannot test the multiprocessing set up
	assert twitterHW2.startUp(['BU_tweets',0]) == 1
	assert twitterHW2.getMsgs(123) == []
	assert twitterHW2.startUp(["thegoldenratio4", 1]) == 1
	assert twitterHW2.startUp(["dog_rates", 3]) == 1
	assert twitterHW2.startUp(["onlyhiphopfacts", 6]) == 1
	assert twitterHW2.startUp(["busasquatch", 0]) == 1
	assert twitterHW2.startUp(["johnmulaneybot", 12]) == 1
	assert twitterHW2.startUp(["mileycyrus", 8]) == 1


#to test the multiprocessing set up (hw3queue.py), modify the restartProgram.bat or restartProgram.sh - details in github readme