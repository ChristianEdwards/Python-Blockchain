import datetime
import hashlib
import json
import os

os.system('clear')

global d
d = datetime.datetime.today()

class Block:
	def __init__(self, nonce, tstamp, transaction, prevhash=''):
		self.nonce = nonce
		self.tstamp = tstamp
		self.transaction = transaction
		self.prevhash = prevhash
		self.hash = self.calcHash()

	def calcHash(self):
		block_string = json.dumps({"nonce: ": self.nonce, "tstamp: ": self.tstamp, "transaction: ": self.transaction, "prevhash: ": self.prevhash}, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	def __str__(self):
		string = " nonce: " + str(self.nonce)
		string += " tstamp: " + str(self.tstamp)
		string += " transaction: " + str(self.transaction)
		string += " prevhash: " + str(self.prevhash)
		string += " hash: " + str(self.hash)
		return string

class BlockChain:
	def __init__(self):
		self.chain = [self.generateGenesisBlock(),]

	def generateGenesisBlock(self):
		return Block(0, "01/01/2019", "Genesis Block")

	def getLastBlock(self):
		return self.chain[-1]

	def addBlock(self, newBlock):
		newBlock.prevhash = self.getLastBlock().hash
		newBlock.hash = newBlock.calcHash()
		self.chain.append(newBlock)

root = BlockChain()
id = 0

while True:
	os.system('clear')

	cont = input("Would you like to add a new transaction:~# ")
	if cont == "yes":
		os.system('clear')

		id += 1

		b_date = str(d.month) + "/" + str(d.day) + "/" + str(d.year)
		block_transaction = float(input("Enter the amount to send:~# "))

		root.addBlock(Block(id, b_date, block_transaction))
		continue
	elif cont == "no":
		os.system('clear')

		break
	else:
		continue

for b in root.chain:
	print(b)
	