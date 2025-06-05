import builtins
import threading
import reprlib
import sys

class A:

    def __init__(self, m=3000, n=6000):
        self._a = builtins.print
        self._b = builtins.len
        self._c = builtins.sum
        self._d = reprlib.Repr()
        self._e = threading.local()
        self._f = set()
        self._g = m
        self._h = set()
    def i(self, j):
        self._e.xyz = True
        try:
            if isinstance(j, str):
                if len(j) > self._g:
                    k = j[:self._g] + '...'
                    return repr(k)
                else:
                    return repr(j)
            if isinstance(j, (list, tuple, set, dict)):
                try:
                    l = len(j)
                except Exception:
                    l = '?'
                return f'<{type(j).__name__} len={l}>'
            m = id(j)
            if m in self._f:
                return f'<{type(j).__name__} Recursion Detected>'
            self._f.add(m)
            n = self._d.repr(j)
            self._f.remove(m)
            return n
        except RecursionError:
            return f'<{type(j).__name__} RecursionError>'
        except Exception as o:
            return f'<unprintable {type(j).__name__}: {o}>'
        finally:
            self._e.xyz = False

    def _p(self, q):
        self._e.xyz = True
        try:
            self._a(q)
        finally:
            self._e.xyz = False

    def r(self, *s, **t_):
        if getattr(self._e, 'xyz', False) or getattr(self._e, 'in_print', False):
            return self._a(*s, **t_)
        self._e.in_print = True
        try:
            self._a(*s, **t_)
            u = ', '.join((self.i(v) for v in s))
            w = ('print', u)
            if w not in self._h:
                self._h.add(w)
                self._a(f'[DETECT] print({u}) -> None')
        finally:
            self._e.in_print = False

    def x(self, y):
        if getattr(self._e, 'xyz', False):
            return self._b(y)
        self._e.xyz = True
        try:
            z = self._b(y)
            aa = self.i(y)
            ab = ('len', aa)
            if ab not in self._h:
                self._h.add(ab)
                self._p(f'[DETECT] ({aa}) -> {z}')
            return z
        finally:
            self._e.xyz = False

    def ac(self, ad):
        if getattr(self._e, 'xyz', False):
            return self._c(ad)
        self._e.xyz = True
        try:
            ae = self._c(ad)
            af = self.i(ad)
            ag = ('sum', af)
            if ag not in self._h:
                self._h.add(ag)
                self._p(f'[DETECT] sum({af}) -> {ae}')
            return ae
        finally:
            self._e.xyz = False

    def ah(self):
        builtins.print = self.r
        builtins.len = self.x
        builtins.sum = self.ac

    def ai(self):
        builtins.print = self._a
        builtins.len = self._b
        builtins.sum = self._c

    def aj(self, ak, al, am):
        self._e.xyz = True
        try:
            an = ak.f_code
            ao = an.co_name
            ap = ak.f_lineno
            aq = an.co_filename
            if al == 'call':
                return self.aj
            elif al == 'line':
                for ar, as_ in ak.f_locals.items():
                    pass
            elif al == 'return':
                self._a(f'[RETURN] {ao} -> {self.i(am)}')
            elif al == 'exception':
                at, au, _ = am
                self._a(f'[EXCEPTION] {ao}: {at.__name__}: {au}')
            return self.aj
        finally:
            self._e.xyz = False

    def start(self):
        self.ah()
        sys.settrace(self.aj)
    def stop(self):
        sys.settrace(None)
        self.ai()
scp = __import__('inspect').getsource(A)
try:
    file = __import__('sys').argv[1]
    tfile = open(file, 'r', encoding='utf8').read()
except:
    __file__ = __file__.split('\\')[-1]
    print(f'using : python {__file__} <filename> ')
    quit()
wttrace = f"""
__file__ = '{file}'
import builtins
import threading
import reprlib
import sys
{scp}
tracer = A()
tracer.start()
{tfile}
tracer.stop()"""
totrace = f'tracer-{file}'
with open(totrace, 'w', encoding='utf8') as au:
    au.write(wttrace)
__import__('subprocess').run(['python', totrace])
