import twitterHW2
#can only test certain tests on local

def test_compare():
#	assert twitterHW2.getMsgs("alexfatyga_") == 1 #1 denotes success
	assert twitterHW2.getMsgs(123) == 0 #0 denotes fail - a non string input is a fail
#	assert twitterHW2.getMsgs("johnmulaneybot") == 1
#	assert twitterHW2.getMsgs("fakefakefakeusername1234211") == 0
