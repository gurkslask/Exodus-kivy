

class ExodusTrade:
	def __init__(self):
		
		self.PlayerStash = {'Red' : 0, 'Green' : 0, 'Blue' : 0}
		self.RatioSell2P = {1:5, 2:3}
		self.RatioBuy2P = {1:3, 2:5}
		self.RatioSell3P = {1:5, 2:4, 3:3}
		self.RatioBuy3P = {1:3, 2:4, 3:5}
		self.RatioSell4P = {1:5, 2:4, 3:4, 4:3}
		self.RatioBuy4P = {1:3, 2:4, 3:5, 4:6}
		self.RatioSell5P = {1:5, 2:5, 3:4, 4:3, 5:3}
		self.RatioBuy5P = {1:3, 2:4, 3:4, 4:5, 5:6}		
		self.RatioSell6P = {1:5, 2:5, 3:4, 4:4, 5:3, 6:3}
		self.RatioBuy6P = {1:3, 2:4, 3:4, 4:5, 5:5, 6:6}	
		self.AdvancedTrading = False
		self.OnlyBuy = False
		self.OnlySell = False


	def CheckIfRightTurn(self):
		assert self.Turn <= len(self.RatioSell), 'Wrong turn'

	def SetAdvancedTrading(self, Active):
		self.AdvancedTrading = Active

		
	def SetRatio(self, Players):
		self.Players = Players
		assert 2 <= Players <= 6, 'Wrong number of players, must be 2-6'
		if Players == 2:
			self.RatioSell = self.RatioSell2P
			self.RatioBuy = self.RatioBuy2P
		elif Players == 3:
			self.RatioSell = self.RatioSell3P
			self.RatioBuy = self.RatioBuy3P
		elif Players == 4:
			self.RatioSell = self.RatioSell4P
			self.RatioBuy = self.RatioBuy4P	
		elif Players == 5:
			self.RatioSell = self.RatioSell5P
			self.RatioBuy = self.RatioBuy5P	
		elif Players == 6:
			self.RatioSell = self.RatioSell6P
			self.RatioBuy = self.RatioBuy6P

	def SetTurn(self, Turn):
		self.Turn = Turn

	def GetPlayerStash(self):
		temp = str(self.PlayerStash)
		temp = temp.replace('{', '')
		temp = temp.replace('}', '')
		temp = temp.replace("'", '')
		return temp

	def SellGreen(self):
		if self.AdvancedTrading == 0 and not self.OnlyBuy:
			self.OnlySell = True
		self.CheckIfRightTurn()
		self.PlayerStash['Green'] = self.PlayerStash['Green'] - 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] + self.RatioSell[self.Turn] + self.AdvancedTrading

	def SellRed(self): 
		if self.AdvancedTrading == 0 and not self.OnlyBuy:
			self.OnlySell = True
		self.CheckIfRightTurn()
		self.PlayerStash['Red'] = self.PlayerStash['Red'] - 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] + self.RatioSell[self.Turn] + self.AdvancedTrading

	def BuyRed(self):
		if self.AdvancedTrading == 0 and not self.OnlySell:
			self.OnlyBuy = True
		self.CheckIfRightTurn()
		self.PlayerStash['Red'] = self.PlayerStash['Red'] + 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] - (self.RatioBuy[self.Turn] - self.AdvancedTrading)

	def BuyGreen(self):
		if self.AdvancedTrading == 0 and not self.OnlySell:
			self.OnlyBuy = True
		self.CheckIfRightTurn()
		self.PlayerStash['Green'] = self.PlayerStash['Green'] + 1
		self.PlayerStash['Blue'] = self.PlayerStash['Blue'] - (self.RatioBuy[self.Turn] - self.AdvancedTrading)

	def ClearPlayerStash(self):
		self.PlayerStash = {'Red' : 0, 'Green' : 0, 'Blue' : 0}
		self.OnlyBuy = False
		self.OnlySell = False








def main():
	Test = ExodusTrade()
	Test.SetRatio(2)
	Test.SetTurn(1)
	Test.SellGreen()
	Test.SellGreen()
	print(len(Test.RatioSell))
	print(Test.GetPlayerStash())


if __name__ == '__main__':
	main()