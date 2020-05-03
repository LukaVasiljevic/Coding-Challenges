# Kaprekarova konstanta je broj 6174 i on se dobija po algoritmu koji je smislio
# indijski matematicar Kaprekar.
# Rutina za dobijanje Kaprekarove konstante je sledeca:
# uzima se bilo koji cetvorocifren broj
# sortirati cifre po rastucem i opadajucem redosledu
# oduzeti manji broj od veceg i dobij rezultat
# postupak se ponavlja sa rezultatom sve dok ne stignemo do broja 6174


def mostCommonDig(arr):
    set(arr)
    g = 0
    l = max(set(arr), key=arr.count)
    for i in range(0, len(arr)):
        if arr[i] == l:
            g += 1
    return g


def sortedNormal(list1):
    list1.sort()
    return list1



def sortedReversed(list1):
    list1.sort(reverse=True)
    return list1


def sortedNormalToInt(list1):
    list1.sort()
    b = "".join(map(str, list1))
    return b


def sortedReversedToInt(list1):
    list1.sort(reverse=True)
    b = "".join(map(str, list1))
    return b


def CreatingList(num):
    numList=[]
    for d in str(num):
        numList.append(int(d))
    return (numList)


number = 0
constant = 6174
num = input("Enter 4-digit number. Number shouldn't start with 0 and shouldn't have more than 2 digits repeating.")
m = []
m = CreatingList(num)
#example line 56, 57
#g= int(sortedReversedToInt(m))-int(sortedNormalToInt(m))
#print(sortedReversedToInt(m), '-', sortedNormalToInt(m), '=', g)
a = mostCommonDig(m)
if num.isdigit() and len(num) == 4 and a < 3 and m[0] != 0:
        #print("Entry is valid!")
        while num != constant:
            z = []
            z = CreatingList(num)
            num = int(sortedReversedToInt(z)) - int(sortedNormalToInt(z))
            print(sortedReversedToInt(z), '-', sortedNormalToInt(z), '=', num)
else:
    print("Entry is not valid!(Number is not 4-digit number or number has more than 2 digits repeating or 0 is "
          "starting digit of number.")
