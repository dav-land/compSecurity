#!/usr/bin/python3

import sys
from collections import defaultdict, Counter

minKeyLength = 2
maxKeyLength = 13

# Hard coded cipher text that was used for creating this script
# Generated using identikey = yousefadala3200
# cipherText = "YWTSEIRADEYQQUHEKSVVISLKENLALHXMBWPKHHNRYWATXCYMCJOGTUMJAGAGEWWFDHNRQVZEKSVLGSNWIGECKOGLLQPLHXEKIELBHTGWOGFMHRLGDLTNQZQMNWTUMVSVXRALQGRMHNBCLHBNIMKDSMIYTJMNZUAJTGKXNGWEGNVENTVZEYIEAVKTXPFWHGUKEFKCHEYAETGKSMHNVJSLYWNGVGTAEUIODEMVRZADIMTYMDWYHNQBJWBHTGWOGFMHRPKDLPEZCULCHMRNQJTAIABQLHXMBWPDIZHGVQJWTSGPKKAELSWTLHXSBCPVOYSRDGJAEFBWVKTXPFZWFNBNTKCEETLEMCVYMOBCTWAKSNVFSSPEYWQCEWBNKMANMHRQTVIKEPBKGNTLVOJLTHSFQPYTHAALHJOTNQAVALERNXKVLRAQDCFCBNTAJGWXDGPCLOGEBNVZEGEJKQEEKSPITJIXDNTCFTXRAUAVETRFIKVMRMBBJWRLUQLGFLRTNSGLHXMBVGQAGDECPGNBAZOQANZTBNCANMTUQUOALCRZVSIGLLBJWEGDSWTTOMHBNWKIMHBCIZTAOJQEMRLEQBJWCHWNZFACXOSBJWNXITPDGUKSUWYABEAZMFEYIOBZOGTAEENQJHXRUWPWSMYNVFZEKGEMGVFHRUMTHALTSWQDHTRQQPWSLAALRJELEABYWADNRAUOEPEEMLMSMAGBJWLBTGTGTRBDTMDQGHOQNQJTNNRIPVIAEYXGVHXRGWVLEKIAOCKSAEJIULOMHRMFYEHFGPGTAGKJPGJELUEMGFONGUAJWGTVRIUAGAAALHWLEOAUAKHHUYLGJIWOAWVCNHWUWYAFHUALVZELTEMPYTATBLQATTTNTNSNWINUCXRTIQQVOALRBCIZLRDBVGTUMIZIPSGXDGWFJAZHRZFGWGTUMDSNDAALCDIMTYMYSYNNQMTLHXAEKJXAKTUMTACHUYLPGTFOIMJWRYOEBJWBKIQOGOALTBWNGWMOYMVEEWOZWTWTAAAKTSWEBRTQOIMSBBJWRXWRPCVTHSGIAEYFOGPGJAEMBAVWNMIEMNQEQPBAGVAGDOWVZOYUFEKLHBNRITKHHTBNVZEBNABJWLTSGWHLHXBYQPVMTNZGEMRBOFQVQIGAFMPKEPAFAVJOGGRZVZAGMLNGSRYOEQEGUEDAWVJEFAVVYZEKEVECKBNTPZGHTUAPSVGTAEOIPCAZAVVYZEGCRAJWLMEEQPYMRHRIFTEAIALCTULHBNDJOHMVUKYHMCBUOSNWTUMTGAWBRNQJEHUELQGRBWNAUUAKCRTAANIOFQVAOGEEMOQEGEZQGKBXGNVVGAKRVDGKEOEAWTWIZHGWHLHXMECPFIGGUITVTAEVZHWEMBRIVANZOHBQXTBMRINGNZTUMTGAWAALVZEFAAEKLHMHRTCFTXRAAQEEIAPMUANYRBVVLHKERUGFRTNGWIWTAEEPCFDBNUIPVAGDVUCVEHUGMXWNMHEWWYHMHRUKKTMHNBVZEFIQLNWMTNBNVZILTEQQOALTUMDDIGDOMIYAKTUMPWXMMBUGFTAIFDQACXSUWYWDFEGPCLIPAFZKYHMDBEPOIMHGPGVOHRUMEJIXDNGGSYXSVZCFSPEEMFLWHOEBJJEXAALCJULHJIUEAWEHXQFTAENLOARTLOMPTOPTUMNSNMEEVDWAKEENQDLHWVVISNWTUMPACHUYLUWEMHRURSULENVFZETRFXGWCAEFXCKSXDVVCDOPEESGQALISBJWYPEEMUMRIRVAGVTHFVVFLHXDBWTGPXNOCVLHXPNCUWWTSOZKWFYOEBJWBEIALOSNTGNQPASLURLJASVOZUCFDLHVAXGIVEFWWFDXDYWWVEKAALJAGAEEIUAFAEJMTWAYIEMYATAENOGJNXSFIPVRTGRQPANBNUMUZONTRLCFDVUEAGVTAEZNQJTAEVZFWLTYSWWJOKFVDGGFMHRUQTEREQIVGNVEGEQJEFAVVKFGHNGPGJOTDJQVZTAESWTEIWAOTGTEZGNZVZEKEJIUSPTU"

#taken from Wikipedia
letter_freqs = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02361, 0.00150, 0.01974, 0.00074]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

# guesses the key length of an inputted cipher text
def keyLength(cipherText):
    varArr = []

    # test keys lengths from 2 -> 13
    for keyLen in range(minKeyLength, maxKeyLength + 1):
        textSeq = ""
        # fetch sequence of letters based on length of key
        for i in range(0, len(cipherText), keyLen):
            textSeq += cipherText[i]

        # get population variance of sequence
        popVar = pop_var(textSeq)
        varArr.append(popVar)

    # # debug tools
    # print(varArr)
    # print(sorted(varArr, reverse = True))
    # print(varArr.index(sorted(varArr, reverse = True)[0]) + minKeyLength)

    # return length of key based on index of highest population variance
    lenKey = varArr.index(sorted(varArr, reverse = True)[0]) + minKeyLength
    return lenKey

# determine the frequency at which letters occur in a string
def letterFreq(textSeq, offsetVal, strLength):
    offset = []
    seqStr = [0] * 26
    # calculate letter value in sequence based on ascii value of character and the current offset being tested
    # algorithm: Ascii character of absolute difference between character in sequence and letter offset
    # i.e. sequence: DDAC..., current offset: A
    # first leter of sequence minus offset: D - A = 4
    # 4th letter of alphabet is D
    for i in range(len(textSeq)):
        offset.append(chr(((ord(textSeq[i]) - 97 - offsetVal) % 26) + 97))

    # count number of occurances
    for j in offset:
        seqStr[ord(j) - ord('a')] += 1

    # Divide every value by the total length of the sequence to get their frequency
    for k in range(len(seqStr)):
        seqStr[k] /= float(strLength)

    # # debug tools
    # print(offset)
    # print(seqStr)

    return seqStr

# run the Chi Squared on a passed in text sequence vs. the actual english frequency
def chiSquared(textSeq):
    chiSqrdArr = [0] * len(alphabet)
    # run a Chi Squared Test for every 26 letter offset
    for i in range(len(alphabet)):
        # Fetch the number of times a letter occurs in the sequence after tested offset
        seqStr = letterFreq(textSeq, i, len(textSeq))

        # run Chi Squared test on sequence string and the expected values
        chiSqrdVal = float(0)
        for j in range(len(alphabet)):
            chiSqrdVal += (pow(seqStr[j] - float(letter_freqs[j]), 2)) / float(letter_freqs[j])
        chiSqrdArr[i] = chiSqrdVal

    # use the smallest chi squared value
    keyChar = chiSqrdArr.index(sorted(chiSqrdArr)[0])
    # return value as an ascii character
    return chr(keyChar + 97)

# calculates the key given the ciphertext and key length
# Algorithm based on concepts found in these videos: youtube.com/watch?v=LaWp_Kq0cKs and youtube.com/watch?v=P4z3jAOzT9I
def guessKey(cipherText, lenKey):
	key = ''
	for i in range(lenKey):
		textSeq=""
        # generates a sequence
		for j in range(0,len(cipherText[i:]), lenKey):
			textSeq += cipherText[i+j]

        # runs chi squared on the text sequence and adds each returned character to the key
		key += chiSquared(textSeq)
	return key

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all lower case
    # (changed to lower case because of ord() function)
    cipherText = sys.stdin.read().replace("\n", "").replace(" ", "").lower()
    print(guessKey(cipherText, keyLength(cipherText)))
