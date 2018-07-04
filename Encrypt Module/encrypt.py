"""Encrypt 2.4.2

This module is made for simple and advanced encryption.
"""
def ceasar(message, shift):
    """simple cipher shifts each letter over a specified number"""
    import pickle
    if shift > 26:
        print("ValueError: shift value excedes limit")
        return "ERROR"
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5","6","7","8","9","0"]
    ciMESS = 0
    # how far into message encryption the program is
    mR = [""]
    for i in range(20):
        mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
    # message result (encoded)
    for i in range(len(message)):
        alphIndex = alphabet.index(message[ciMESS])
        if alphIndex + shift > 26:
            alphIndex = alphIndex - len(alphabet)
        if alphIndex + shift < 0:
            alphIndex = alphIndex + len(alphabet)
        mR[ciMESS] = alphabet[alphIndex + shift]
        ciMESS += 1
    mR = "".join(mR)
    return mR
def crack_ceasar(message):
    """program created to crack the simple ceasar cipher"""
    # ceasar cipher shift amount.
    shift = 0
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5","6","7","8","9","0"]
    # how far into message encryption the program is
    ciMESS = 0
    # message result (decoded)
    mR = []
    aR = []
    fR = []
    for i in range(20):
        mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
    for s in range(26):
        mR = [""]
        for i in range(20):
            mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
        ciMESS = 0
        for i in range(len(message)):
            alphIndex = alphabet.index(message[ciMESS])
            if alphIndex + shift > 26:
                alphIndex = alphIndex - len(alphabet)
            if alphIndex + shift < 0:
                alphIndex = alphIndex + len(alphabet)
            mR[ciMESS] = alphabet[alphIndex + shift]
            ciMESS += 1
        mR = "".join(mR)
        aR.append(mR)
        shift += 1
    return aR
def polyalph(message, shift_word):
    """takes a message and a short word to encode"""
    strShiftKey = shift_word
    # ceasar cipher shift amount.
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5","6","7","8","9","0"]
    lShiftWord = []
    # Number equivelents for strShiftKey
    iShiftWordNum = 0
    iAlphNum = 0
    # helps find letter from alphabet
    iAlphShiftNum = 0
    # alphabet assist for encryption adds shift in
    iMessageData = 0
    # how far into message encryption the program is
    strResult = " "
    strResult1 = " "
    # message result (encoded)
    while iMessageData < len(strShiftKey):
        if alphabet[iAlphNum] in strShiftKey[iMessageData]:
            while iAlphNum > 26:
                iAlphNum = iAlphNum - len(alphabet)
                # checks if the alph num is over string length
            lShiftWord.append (iAlphNum)
            # adds number to shift word list
            iMessageData = iMessageData + 1
            iAlphNum = 0
        else:
            iAlphNum = iAlphNum + 1
            # if the letter tried does not come out true a differnt letter is tried
    iMessageData = 0
    while iMessageData < len(message):
        if alphabet[iAlphNum] in message[iMessageData]:
            print (" ")
            iAlphShiftNum = iAlphNum + lShiftWord[iShiftWordNum]
            while iAlphShiftNum > 26:
                iAlphShiftNum = iAlphShiftNum - len(alphabet)
            strResult1 = alphabet[iAlphShiftNum]
            strResult = strResult + strResult1
            # renders answer
            iMessageData = iMessageData + 1
            # changes what letter program is evaluated 
            iAlphNum = 0
            if iShiftWordNum == (len(lShiftWord) - 1):
                iShiftWordNum = 0
                # siplifies expression if over allowed amount
            else:
                iShiftWordNum = iShiftWordNum + 1
            # if the letter tried does not come out true a differnt letter is tried
    #       if messrec == len(shiftword)-1:
    #            messloop = 0
        else:
            iAlphNum = iAlphNum + 1
    return strResult
def crack_polyalph(message, maxLen):
    """program created to break messages encoded with poly alphabetic ciphers"""
    import pickle
    # ceasar cipher shift amount.
    shift = 10
    shiftPoss = 0
    shiftlist = []
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5","6","7","8","9","0"]
    progress = 1
    # how far into message encryption the program is
    ciMESS = 0
    # message result (decoded)
    mR = []
    aR = []
    fR = []
    # replace code \/ \/ \/
    for i in range(20):
        mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
    # replace code /\ /\ /\
    shiftlist = list(str(shift))
    for i in range(0, len(str(shift))):
        shiftlist[i] = int(shiftlist[i])
    while len(shiftlist) < maxLen:
        # regulates shift(var is shiftlist)
        shiftlist[-1] += 1
        for b in range(0, len(shiftlist)):
            if shiftlist[b] > len(alphabet) and b > 0:
                shiftlist[b - 1] += 1
                shiftlist[b] = 0
            elif shiftlist[b] > len(alphabet) and b == 0:
                shiftlist[b] = 0
                shiftlist.insert(0,0)
        # reset vars
        mR = [""]
        for i in range(20):
            mR.extend(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",])
        ciMESS = 0
        # iterates through given message
        for i in range(len(message)):
            # searches alphabet for item ciMESS of message
            alphIndex = alphabet.index(message[ciMESS])
            # wraps shift around if to high or low
            if alphIndex + shiftlist[shiftPoss] > len(alphabet):
                alphIndex = alphIndex - len(alphabet)
            if alphIndex + shift < 0:
                alphIndex = alphIndex + len(alphabet)
            # implements shift calculated above
            mR[ciMESS] = alphabet[alphIndex + shiftlist[shiftPoss] - 1]
            ciMESS += 1
            shiftPoss += 1
            # resets shift possition if to high
            if shiftPoss > len(shiftlist)-1:
                shiftPoss = 0
        # writes result to all results list (var is aR)
        mR = "".join(mR)
        aR.append(str(shift)+"."+str(shiftlist)+". "+ mR)
        shift += 1
    return tuple(aR)
def data_en(password):
    """data encryption not secure makes it not readable for more options use the base64 module"""
    import base64
    return base64.b64encode(bytes(password, 'utf-8'))
def data_de(password):
    """data encryption not secure makes it not readable for more options use the base64 module"""
    import base64
    return base64.b64decode(bytes(password, 'utf-8'))
def ascii_(key, message, operation = "en"):
    """adds the ascii value of the key and the string to generate a coded message note: the third parameter can be set to de for decryption, leave blank for encryption"""
    if operation == "en":
        encoded = ''
        for i in range(len(message)):
            key_c = ord(key[i % len(key)])
            string_c = ord(message[i % len(message)])
            encoded += chr((key_c + string_c) % 127)
        return encoded
    else:
        msg = []
        for i, c in enumerate(message):
            key_c = ord(key[i % len(key)])
            enc_c = ord(c)
            msg.append(chr((enc_c - key_c) % 127))
        return ''.join(msg)
def sha(message, type_=1):
    """uses sha hashing to hash a message choices for the type field are 1, 224, 256, 384, and 512 for more advanced tools with sha use the hashlib module"""
    import hashlib
    return eval("hashlib.sha"+str(type_)+"(bytes(message, 'utf-8')).hexdigest()")
def substitution(letters, message, type_ = "en"):
    """input a list of letters and a message every letter corresponds to a letter in the alphabet"""
    result = []
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    if type_ == "en":
        for i in message:
            result.append(letters[alphabet.index(i)])
        return "".join(result)
    else:
        for i in message:
            result.append(alphabet[letters.index(i)])
        return "".join(result)
def alphabet():
    """returns list with alphabet"""
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
"""
def crack_substitution(message, type_ = "de"):
    import pickle
    Aresults = []
    result = []
    keys = pickle.load(open("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/encrypt_resources/keys_substitution.p", "rb"))
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    if type_ == "en":
        for item in keys:
            for i in message:
                result.append(letters[alphabet.index(i)])
            Aresults.append("".join(result))
            result = []
        return "".join(Aresult)
    else:
        for item in keys:
            for i in message:
                result.append(alphabet[item.index(i)])
            Aresults.append("".join(result))
            result = []
        return "".join(Aresult)
"""
