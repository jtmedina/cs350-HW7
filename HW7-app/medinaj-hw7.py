###	<Medina, Jeremy> <10-26-2016> ###
## <Homework # 7> ##
import random

class Talker:
	def __init__(self, n, v):
		self.name = n
		self.vocab = v

	def getname(self):
		return self.name

	def getvocab(self):
		return self.vocab

def main():
	h_responses = ["Hi, I'm Hillary."]*10
	h_responses[hash("r1")%10] = "You know, I think when we talk about the Supreme Court, it really raises the central issue in this election."
	h_responses[hash("r2")%10] = "You are the most dangerous person for run for President of the United States in modern times."
	h_responses[hash("r3")%10] = "I have major disagreements with my opponent"
	h_responses[hash("r4")%10] = "I understand and respect the tradition of gun ownership."
	h_responses[hash("r5")%10] = "I support women's right to make their own difficult, personal decisions about their own bodies."
	h_responses[hash("r6")%10] = "I voted for border security. And the wall."
	h_responses[hash("r7")%10] = "HE used undocumented workers to build the Trump tower."
	h_responses[hash("r8")%10] = "I wan to keep employers like him from exploiting then deporting illegal aliens - it's not good for them, and it's not good for our country."
	h_responses[hash("r9")%10] = "We will have secure borders and we will have immigration reform."
	h_responses[hash("r10")%10] = "That's because he'd rather have a puppet as president."
	h_responses[hash("r11")%10] = "He's going to advocate for the biggest tax cuts we've ever seen."
	h_len = len(h_responses)


	t_responses = ["Trump is in the house."]*10
	t_responses[hash("r1")%10] = "Well, first of all, it's so great to be with you and thank you, everybody."
	t_responses[hash("r2")%10] = "You belong in jail [Hillary]."
	t_responses[hash("r3")%10] = "What a nasty woman."
	t_responses[hash("r4")%10] = "You can say you can rip a baby out of a womb, but that is not ok with me. Even though it's ok with her."
	t_responses[hash("r5")%10] = "Hillary wants to have no borders"
	t_responses[hash("r6")%10] = "Heroin...pours across our borders (were caused by Hillary Clinton and Barack Obama)"
	t_responses[hash("r7")%10] = "I want to build a wall."
	t_responses[hash("r8")%10] = "We're going to get - we have some bad hombres here - and we're going to get them out."
	t_responses[hash("r9")%10] = "You're the puppet!"
	t_responses[hash("r10")%10] = "Her plan will raise taxes and double your taxes."
	t_responses[hash("r11")%10] = "She deleted 31,000 emails after getting a subpoena from the FBI. She lied to the FBI, and she's going to be the president of the United States?"
	
	t_len = len(t_responses)


	while 1:
		badHombre = raw_input("Who's response would you like to receive? (Hillary or Trump): ")
		print 'hlen: ',h_len
		print 'tlen: ',t_len
		if badHombre in ("Trump","trump","T","t"):
			question = raw_input("What is your question? ")
			trump = Talker("Trump", t_responses[random.randint(0,t_len)])
			print '\nThe speaker is: ',trump.getname(),'\n'
			print trump.getname(),"says: ",trump.getvocab(),"\n"

		if badHombre in ("Hillary","hillary","H","h","hilly"):
			question = raw_input("What is your question? ")
			hillary = Talker("Hillary", h_responses[random.randint(0,h_len)])
			print '\nThe speaker is: ',hillary.getname(),"\n"
			print hillary.getname(),"says: ",hillary.getvocab(),"\n"

if __name__ == "__main__":
	main()