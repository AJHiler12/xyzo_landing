from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        # Do not let the Preview browser reuse a stale 304 response after
        # promoting a static prototype into index.html.
        if "If-Modified-Since" in self.headers:
            del self.headers["If-Modified-Since"]
        if "If-None-Match" in self.headers:
            del self.headers["If-None-Match"]
        return super().send_head()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 5000), NoCacheHandler).serve_forever()