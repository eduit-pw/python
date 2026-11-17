import json
import time
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs

ALBUMY=[{"id":7,"tytul":"Poranek","pobrania":120},{"id":12,"tytul":"Wieczór","pobrania":80}]

class Obsluga(BaseHTTPRequestHandler):
    def odpowiedz(self,status,dane,typ="application/json"):
        tekst=json.dumps(dane,ensure_ascii=False) if typ=="application/json" else dane
        bajty=tekst.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type",typ+"; charset=utf-8")
        self.send_header("Content-Length",str(len(bajty)))
        self.end_headers()
        try:self.wfile.write(bajty)
        except (BrokenPipeError,ConnectionResetError):pass
    def do_GET(self):
        adres=urlparse(self.path)
        if adres.path=="/albumy":
            try:prog=int(parse_qs(adres.query).get("min",["0"])[0])
            except ValueError:self.odpowiedz(400,{"blad":"Błędny próg"});return
            self.odpowiedz(200,[a for a in ALBUMY if a["pobrania"]>=prog])
        elif adres.path=="/nie-json":self.odpowiedz(200,"to nie jest JSON","text/plain")
        elif adres.path=="/wolno":
            time.sleep(0.5)
            self.odpowiedz(200,{"stan":"ok"})
        else:self.odpowiedz(404,{"blad":"Brak zasobu"})
    def do_POST(self):
        if urlparse(self.path).path!="/ai-demo":self.odpowiedz(404,{"blad":"Brak zasobu"});return
        if self.headers.get("Authorization")!="Bearer demo_token":
            self.odpowiedz(401,{"blad":"Błędny token demonstracyjny"});return
        try:
            dane=json.loads(self.rfile.read(int(self.headers.get("Content-Length","0"))))
            tekst=dane["tekst"]
            if not isinstance(tekst,str):raise ValueError()
        except (ValueError,KeyError,TypeError):self.odpowiedz(400,{"blad":"Błędne dane"});return
        self.odpowiedz(200,{"odpowiedz":"Demo: "+tekst})

if __name__ == "__main__":
    serwer=ThreadingHTTPServer(("127.0.0.1",8000),Obsluga)
    try:serwer.serve_forever()
    except KeyboardInterrupt:pass
    finally:serwer.server_close()
