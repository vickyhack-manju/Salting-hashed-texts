import hashlib
import uuid
from module import sec
Texthash = (sec)
#print(sec)
secure = hashlib.sha256(Texthash.encode()).hexdigest()
print("the encoded code for the text is :", secure)
salt = uuid.uuid4().hex
print("the salt is : ", salt)
hashed = hashlib.sha256(Texthash.encode()).hexdigest() + ":" + salt #adding a secondary layer to a normal string
#used : to identityfy the salt in the salted code
print("the salted code is : ", hashed)
