import twitterHW2
#can only test certain tests on local

def test_compare(): #these tests test the threading system set up but cannot test the multiprocessing set up
	assert twitterHW2.startUp(['a'], 0) == 0
	assert twitterHW2.startUp(['BU_tweets',0]) == 1
	assert twitterHW2.getMsgs(123) == 0 
	assert twitterHW2.getMsgs("fakefakefakeusername1234211") == 1

#to test the multiprocessing set up (hw3queue.py), modify the restartProgram.bat or restartProgram.sh - details in github readme