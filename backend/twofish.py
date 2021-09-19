from twofish import Twofish

T = Twofish(b'*secret*')
x = T.encrypt(b'TECHMATRIX')
print(T.decrypt(x).decode())