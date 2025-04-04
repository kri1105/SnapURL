from flask import Flask, render_template, request, redirect, url_for
import hashlib
import string
import random

app = Flask(__name__)

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.short_url_map = {}
        self.domain = "http://localhost:5000/"
        self.short_length = 6
        
    def _generate_short_key(self, original_url):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(self.short_length))
    
    def shorten_url(self, original_url):
        if original_url in self.url_map:
            return self.domain + self.url_map[original_url]
        
        short_key = self._generate_short_key(original_url)
        while short_key in self.short_url_map:
            short_key = self._generate_short_key(original_url + str(random.random()))
        
        self.url_map[original_url] = short_key
        self.short_url_map[short_key] = original_url
        return self.domain + short_key
    
    def expand_url(self, short_url):
        short_key = short_url.replace(self.domain, "")
        return self.short_url_map.get(short_key)

shortener = URLShortener()

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            if not original_url.startswith(('http://', 'https://')):
                original_url = 'http://' + original_url
            short_url = shortener.shorten_url(original_url)
    return render_template('index.html', short_url=short_url)

@app.route('/<short_key>')
def redirect_to_original(short_key):
    original_url = shortener.expand_url(f"http://localhost:5000/{short_key}")
    if original_url:
        return redirect(original_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)