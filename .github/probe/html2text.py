# Temporary: strips HTML to readable text so docs can be read from CI logs.
import sys, html.parser
class P(html.parser.HTMLParser):
    skip = 0
    out = []
    def handle_starttag(self, t, a):
        if t in ("script", "style", "nav", "header", "footer", "devsite-header", "devsite-footer-linkboxes"): self.skip += 1
        if t in ("p", "br", "li", "pre", "h1", "h2", "h3", "h4", "tr", "div"): self.out.append("\n")
    def handle_endtag(self, t):
        if t in ("script", "style", "nav", "header", "footer", "devsite-header", "devsite-footer-linkboxes") and self.skip: self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.out.append(d)
p = P(); p.feed(sys.stdin.read())
import re
print(re.sub(r"\n\s*\n+", "\n", "".join(p.out)))
