import json, io, re, HTMLParser

import xmltodict
from lxml import etree

with open('posts.xml') as f:
  xml_str = f.read()
d = xmltodict.parse(xml_str)

class CodeSnippet:
  def __init__(self, html_code, answer_id):
    self.html_code = html_code
    self.clean_code = HTMLParser.HTMLParser().unescape(html_code)
    self.answer_id = answer_id

# json_str = json.dumps(d, indent=2)
# print json_str

code_snippets = []
for row in d['xml']['row']:
  if row["@PostTypeId"] == '2':
    match = re.search('<code>(.+?)</code>', row["@Body"], re.DOTALL|re.MULTILINE)
    if match:
      html_code = match.group(1)
      code_snippets.append(CodeSnippet(html_code, row["@Id"]))

html_str = ''
answer_link = (
  '<div><a href="https://stackoverflow.com/a/{}">https://stackoverflow.com/a/{}</a></div>'
)
for snippet in code_snippets:
  html_str += answer_link.format(snippet.answer_id, snippet.answer_id)
  html_str += '<pre style="margin:5px; border: solid 2px">{}</pre>'.format(snippet.html_code)
with open('code_snippets.html', 'w') as f:
  f.write(html_str)

# code_snippets_json = json.dumps(code_snippets, indent=2)
# with open('code_snippets.json', 'w') as f:
#   f.write(code_snippets_json)
