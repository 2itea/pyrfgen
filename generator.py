# -*- coding: utf-8 -*-
#!/usr/bin/env python3

carTable = {
		"A": "10",
		"B": "11",
		"C": "12",
		"D": "13",
		"E": "14",
		"F": "15",
		"G": "16",
		"H": "17",
		"I": "18",
		"J": "19",
		"K": "20",
		"L": "21",
		"M": "22",
		"N": "23",
		"O": "24",
		"P": "25",
		"Q": "26",
		"R": "27",
		"S": "28",
		"T": "29",
		"U": "30",
		"V": "31",
		"W": "32",
		"X": "33",
		"Y": "34",
		"Z": "35"
}


def normalizeRef(ref):
    return ref.replace(" ", "").upper() # remove spaces and uppercase

def replaceChars(ref):
    tempRef = ""
    for x in ref: # loop over ref
        if x.isalpha(): # check if letter
            tempRef = tempRef + carTable[x] # replace letter by number
        else:
            tempRef = tempRef + x # add int to tempRef

    return tempRef

def calculateRfChecksum(ref):
    preResult = ref + "RF00" # add 'RF00' to the end of ref
    preResult = replaceChars(preResult) # replace to numeric
    checksum = ( 98 - (int(preResult) % 97) ) # calculate checksum
    return str(checksum).rjust(2, '0') # pad left 0 if under 10


def generateRfReference(input):
    normalizedRef = normalizeRef(input)
    checksum = calculateRfChecksum(normalizedRef)
    rfReference = "RF{}{}".format(str(checksum), str(normalizedRef)) # generate rf creditor
    if validateRfReference(rfReference): # check if the reference is valid
        return rfReference
    else:
        return False

def validateRfReference(ref):
    pre = normalizeRef(ref)
    if not pre.isalnum(): # allow only alphanumeric
        return False
    ref = pre[4:] + pre[:4] # move 4 chars to the end
    num = replaceChars(ref)
    if len(pre) < 26 and (int(num) % 97) == 1: # check if reference up to 25 characters long and modulo is 1
        return True
    else:
        return False


## print(generateRfReference("asdfsdfgdgdfgddfsdf"))
