'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = range(65,90+1)
    
    for i in alphabet:
        letterInput = ord(letter)
        shiftInput = int(shift)
        newLetter = letterInput + shiftInput
        
        if letterInput == 32:
            return chr(32)
        
        if newLetter > 90:
            difference = newLetter - 90
            
            if difference > 26:
                letter1 = chr(difference%26 + 64)
                return letter1
        
            else:
                letter2 = chr(difference + 64)
                return letter2
            
        else:
            return chr(newLetter)

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    letters = list(message) 
    list1 = [ord(i)+shift for i in letters]
    
    for l in list1:
        list2 = [32 if l-shift == 32 else l for l in list1]
        
        for m in list2:
            list3 = [(64+shift) if m > 90 and shift <= 26 else m for m in list2]
            
            for n in list3:
                list4 = [(((n-90)%26) + 64) if shift > 26 and (n+shift) > 90 and n!=32 else n for n in list3]
                
    listToStr = ''.join([chr(n) for n in list4])
                
    return listToStr

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    actual_l = str(letter).upper()
    actual_s = str(letter_shift).upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output2 = ""
    for p in alphabet:
        if actual_l != " ":
        #if alphabet.index(actual_s) <= 26:  
            shift_number = alphabet.index(actual_s) + alphabet.index(actual_l)
            if shift_number <= 26:
                output2 = alphabet[shift_number]
            else:
                output2 = alphabet[shift_number%26]
        else:
            output2 = " "
    return output2

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    msglist = list(message)
    msglistNum = [ord(letter) for letter in msglist]
    keylist = list(key)
    
    keydict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
                'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
                'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    
    for k in keylist:
        if len(msglist) > len(keylist):
            keylist.append(k)
            keylistNum = [keydict[keylett] for keylett in keylist] 
        
        else:
            keylistNum = [keydict[keylett] for keylett in keylist]
  
    for m in msglistNum:  
        addedlist = [x + y for x, y in zip(msglistNum, keylistNum)]   
            
    for a in addedlist:
        modifiedlist = [32 if 32<a<57 else a for a in addedlist]
        
    for m in modifiedlist:
        finallist = [m-90+64 if m>90 else m for m in modifiedlist]
        
        vinegarStr = ''.join([chr(f) for f in finallist])
                
        return vinegarStr

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    scymsg = list(message)
    shiftNum = int(shift)
    copyscy = []
    
    while len(scymsg)%shiftNum != 0:
        scymsg.append('_')
    
    for z in range(len(scymsg)):
        copyscy.append((z//shiftNum) + (len(scymsg)//shiftNum) * (z%shiftNum))
        
    for x in copyscy:
        newciph = [scymsg[x] for x in copyscy] 
        
        scystr = ''.join([str(y) for y in newciph])          
        return scystr

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    descymsg = list(message)
    deshiftNum = int(shift)
    decopyscy = []
    message_length = len(descymsg)
    rows = message_length // deshiftNum
    columns = deshiftNum

    for col in range(columns):
        for row in range(rows):
            index = row * columns + col
            if index < message_length:
                decopyscy.append(descymsg[index])

    descystr = ''.join(decopyscy)

    return descystr
