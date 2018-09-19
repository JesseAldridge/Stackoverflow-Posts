import requests

resp = requests.get('https://duckduckgo.com/html/?q=is+letter+python')
# resp = requests.get('https://duckduckgo.com/?q=is+letter+python&t=h_&atb=v134-1__&ia=qa')
with open('out.html', 'w') as f:
  f.write(resp.content)
