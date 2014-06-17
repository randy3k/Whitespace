import sublime, sublime_plugin
import re


class RemoveTrailingWhitespace(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        self.trim_whitespace(edit)
        if view.settings().get("ensure_single_trailing_newline", False):
            self.ensure_single_trailing_newline(edit)

    def trim_whitespace(self, edit):
        view = self.view
        pat = r"( |\t)+$"
        if view.settings().get("ignore_whitespace_only_lines", False):
            pat = r"(?<=\S)" + pat
        regions = view.find_all(pat)
        if regions:
            regions.reverse()
            for r in regions:
                if view.settings().get("ignore_whitespace_on_current_line", False) and \
                        any([r.intersects(view.line(s.b)) for s in view.sel()]):
                    continue
                view.erase(edit, r)

    def is_empty(self, row):
        view = self.view
        return re.match(r"^\s*$", view.substr(view.line(view.text_point(row, 0))))

    def ensure_single_trailing_newline(self, edit):
        view = self.view
        lastrow = view.rowcol(view.size())[0]
        if not self.is_empty(lastrow):
            view.insert(edit, view.size(), "\n")
            lastrow = lastrow + 1
        row = lastrow
        while row>=1:
            if self.is_empty(row-1):
                R = view.line(view.text_point(row, 0))
                a = R.a
                b = R.b
                view.erase(edit, sublime.Region(a-1,b))
                row = row-1
            else:
                break

class WhitespaceEventListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if view.is_scratch() or view.settings().get('is_widget'): return
        if view.settings().get("remove_trailing_whitespace_on_save", False):
            view.run_command("remove_trailing_whitespace")
