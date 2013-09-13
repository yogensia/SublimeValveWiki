# code modified by yogensia
# based on Stackoverflow Search Plugin by Eric Martel (emartel@gmail.com / www.ericmartel.com)
# and Search WordPress Codex by Matthias Krok (www.welovewordpress.de)

# available commands
#   valve_wiki_open_selection
#   valve_wiki_search_selection
#   valve_wiki_search_from_input

import sublime
import sublime_plugin
import subprocess

def OpenInBrowser(url):
    sublime.active_window().run_command('open_url', {"url": url})

def SearchValveWikiFor(text):
    url = 'https://developer.valvesoftware.com/w/index.php?title=Special%3ASearch&fulltext=Search&search=' + text.replace(' ','%20')
    OpenInBrowser(url)

def OpenValveWikiReference(text):
    url = 'https://developer.valvesoftware.com/wiki/' + text.replace(' ','%20')
    OpenInBrowser(url)

class ValveWikiOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)

            # if the search string doesn't contain '$' add it to it
            if not '$' in text:
                text = '$' + text

            OpenValveWikiReference(text)

class ValveWikiSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            SearchValveWikiFor(text)

class ValveWikiSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search Valve Wiki for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchValveWikiFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass