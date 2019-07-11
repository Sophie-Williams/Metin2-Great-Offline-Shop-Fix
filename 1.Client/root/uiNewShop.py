"""
	Author	: Valiant
	File	: uiNewShop.py
	Create	: 2019.07.11
"""

## 1.) Find this:
class ShopDialogCreate(ui.ScriptWindow):

## 2.) Add before this:
ENABLE_VALIANT = True
if ENABLE_VALIANT:
	ValiantDictionary = {
		'CharacterList' : [
			"!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]",
			"{","}","\\","|",";",":","'",'"',",","<",".",">","/","?","~","`"
		],
	}

## 1.) Find this:
	def CreateShop(self):
		if len(self.UI["nameEdit"].GetText()) <=0:
			self.PopupMessage(uiScriptLocale.SHOP_NAME_EMPTY)
			return

## 2.) Add after this:
		if ENABLE_VALIANT:
			ValiantNameCheck = self.UI["nameEdit"].GetText()
			if ValiantNameCheck.find(ValiantDictionary['CharacterList']) != -1 
				self.PopupMessage("You crazy bitch")
				return

## 1.) Find this:
	def OnChangeName(self,id):
		if not self.inputDialog:
			return
		name=self.inputDialog.GetText()
		if not len(name):
			return

## 2.) Add after this:
		if ENABLE_VALIANT:
			if name.find(ValiantDictionary['CharacterList']) != -1 
				self.PopupMessage("You crazy bitch")
				return






