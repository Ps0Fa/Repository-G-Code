import sublime
import sublime_plugin
import re

class millingdxfCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		myRegion = sublime.Region(0, self.view.size())
		myMainText = self.view.substr(myRegion)
		myLinedText = myMainText.split('\n')

		failCounter = 0
		clearText = ""
		myLinedText = myMainText.split('\n')
		for x in range(len(myLinedText)):
			if len(myLinedText[x]) & x != 1 > 0:
				if re.match(r"G1 Z  -0.118",myLinedText[x],re.I):
					failCounter = 1
				if re.match(r"G0 Z   0.591 ",myLinedText[x],re.I):
					failCounter = 0
				if failCounter == 0:
					clearText = clearText + myLinedText[x] + "\n"

		
		myTextToPrint = re.sub(r"G20", "G21", clearText)
		myTextToPrint1 = re.sub(r"I.*?\n", "\n", myTextToPrint)
		myTextToPrint = re.sub(r"(Units in inches)", "Units in mm", myTextToPrint1)
		
		self.view.replace(edit,myRegion,myTextToPrint)