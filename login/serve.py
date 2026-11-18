"""Local preview server with byte ranges for native video seeking."""
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import os,re,argparse
class Handler(SimpleHTTPRequestHandler):
    def send_head(self):
        self.span=None
        path=self.translate_path(self.path)
        if os.path.isfile(path) and self.headers.get('Range'):
            f=open(path,'rb');size=os.fstat(f.fileno()).st_size
            match=re.fullmatch(r'bytes=(\d+)-(\d*)',self.headers['Range'])
            if not match:f.close();self.send_error(416);return None
            start=int(match[1]);end=min(int(match[2]) if match[2] else size-1,size-1)
            if start>end:f.close();self.send_error(416);return None
            self.send_response(206);self.send_header('Content-type',self.guess_type(path));self.send_header('Content-Length',str(end-start+1));self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.send_header('Accept-Ranges','bytes');self.end_headers();f.seek(start);self.span=end-start+1;return f
        return super().send_head()
    def copyfile(self,source,outputfile):
        if self.span is None:return super().copyfile(source,outputfile)
        left=self.span
        while left:
            data=source.read(min(left,1024*1024))
            if not data:break
            outputfile.write(data);left-=len(data)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8932);a=p.parse_args();os.chdir(Path(__file__).resolve().parent);ThreadingHTTPServer(('127.0.0.1',a.port),Handler).serve_forever()
