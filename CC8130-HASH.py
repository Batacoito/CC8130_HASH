import hashlib

myText = 'Somente SHA256 correto'
SHA256_certo = hashlib.sha256(myText.encode('utf-8')).hexdigest()
MD5_certo = hashlib.md5(myText.encode('utf-8')).hexdigest()

SHA256_teorico = "5b22f6bf621c2116f0d4589c3b5405ed3b5d768b9ba1dfafbae9292331ce9827"
MD5_teorico = "cfe69ac7a0b07810b391c27b1ea838cd"

print("SHA256 = " + SHA256_certo)
print("MD5 = " + MD5_certo)

if (SHA256_teorico == SHA256_certo):
    print("SHA256 certo")
else:
    print("SHA256 incorreto");
if (MD5_certo == MD5_teorico):
    print("MD5 certo")
else:
    print("MD5 incorreto");


