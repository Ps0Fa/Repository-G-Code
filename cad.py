import sublime
import sublime_plugin
import re

class cadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		myRegion = sublime.Region(0, self.view.size())
		myMainText = self.view.substr(myRegion)
		myLinedText = myMainText.split('\n')

		myTextToPrint = re.sub(r"G0 G53 Z0", "", myMainText)
		myTextToPrint1 = re.sub(r"G0 G53 X0 Y0 A0", "", myTextToPrint)
		myTextToPrint = re.sub(r"G54 A-0", "", myTextToPrint1)
		myTextToPrint1 = re.sub(r"G0 A-0", "", myTextToPrint)
		myTextToPrint = re.sub(r"G0 G53 Z0 M9", "", myTextToPrint1)
		myTextToPrint1 = re.sub(r"G0 G53 X0 Y0 A0 M5", "", myTextToPrint)
		myTextToPrint = re.sub(r".*move up to.*", "", myTextToPrint1)


		
		self.view.replace(edit,myRegion,myTextToPrint)