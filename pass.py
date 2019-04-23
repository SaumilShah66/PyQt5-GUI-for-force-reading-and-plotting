import pickle
import hashlib

class passswo():
	def __init__(self):
		self.user = "saumil"
		self.pas = "hey_bro"
		self.l = []
		self.ppp = hashlib.sha512(self.pas.encode()).hexdigest()
		self.l.append([self.user, self.ppp])

if __name__=='__main__':
	pppp = passswo()
	with open("p.p",'wb') as f:
		pickle.dump(pppp.l, f)