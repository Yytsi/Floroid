import functions # Contains helper functions.
import itertools
import math
import functools
import fractions

class Floroid(object):
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode

    def source(self, code):
        self.sourceCode = code

    def parse(self):
        mappings = {
            "p" : "all",
            "q": "zip",
            "r": "any",
            "s": "tuple",
            "t": "sorted",
            "u": "True",
            "v": "int",
            "w": "range",
            "x": "ord",
            "y": "join",
            "z": "print",
            "A": "def ",
            "B": "lambda ",
            "C": "not ",
            "D": "[::-1]",
            "E": "return ",
            "F": "if ",
            "G": "else",
            "H": "or ",
            "I": "in ",
            "J": "split()",
            "K": "for",
            "L": "input()",
            "M": "and ",
            "N": "while",
            "O": "str",
            "P": "chr",
            "Q": "list",
            "R": "map",
            "S": "bin",
            "T": "sum",
            "U": "eval",
            "V": "abs",
            "W": "set",
            "X": "min",
            "Y": "max",
            "Z": "len",
            "aa": "functions.getPrime",
            "ab": "bool",
            "ac": "try",
            "ad": "yield",
            "ae": "hex",
            "af": "del",
            "ag": "None",
            "ah": "float",
            "ai": "enumerate",
            "aj": "round",
            "ak": "break",
            "al": "elif",
            "am": "[::2]",
            "an": "except",
            "ao": "functions.isPrime",
            "ba": "keys",
            "bb": "float(input())",
            "bc": "exec",
            "bd": "dict",
            "be": "int(input())",
            "bf": "values",
            "bg": "list(input())",
            "bh": "tuple(input())",
            "bi": "replace",
            "bj": "translate",
            "bk": "zfill",
            "bl": "[1::2]",
            "bm": "startswith",
            "bn": "endswith",
            "bo": "index",
            "ca": "itertools.product",
            "cb": "itertools.permutations",
            "cc": "itertools.combinations",
            "cd": "itertools.combinations_with_replacement",
            "ce": "itertools.accumulate",
            "cf": "itertools.chain",
            "cg": "itertools.chain_from_iterable",
            "ch": "itertools.compress",
            "ci": "itertools.dropwhile",
            "cj": "itertools.filterfalse",
            "ck": "itertools.islice",
            "cl": "itertools.starmap",
            "cm": "itertools.takewhile",
            "cn": "itertools.zip_longest",
            "co": "itertools.count",
            "da": "itertools.cycle",
            "db": "itertools.repeat",
            "dc": "divmod",
            "dd": "filter",
            "de": "open",
            "df": "type",
            "dg": "pop",
            "dh": "math.ceil",
            "di": "math.pi",
            "dj": "math.floor",
            "dk": "math.factorial",
            "dl": "math.tan",
            "dm": "math.sin",
            "dn": "math.cos",
            "do": "math.log",
            "ea": "math.log10",
            "eb": "math.log2",
            "ec": "math.lgamma",
            "ed": "math.exp",
            "ee": "math.degrees",
            "ef": "math.radians",
            "eg": "math.e",
            "eh": "math.fsum",
            "ei": "math.trunc",
            "ej": "math.sqrt",
            "ek": "100",
            "el": "1000",
            "em": "functions.getPrimeIndex",
            "en": "functions.sieveOfAtkin",
            "eo": "functions.fibonacci",
            "fa": "functions.int2base",
            "fb": "functions.lexicographic_index",
            "fc": "functions.getPermutationOnIndex",
            "fd": "functions.toASCIICodes",
            "fe": "functions.deleteAt",
            "ff": "functions.first",
            "fg": "functions.last",
            "fh": "find",
            "fi": "key",
            "fj": "end",
            "fk": "upper()",
            "fl": "lower()",
            "fm": "count",
            "fn": "split",
            "fo": "functools.reduce",
            "ga": "fractions.gcd",
            "gb": "functions.lcm",
            "gc": "functions.lcmm",
            "ge": "functions.gcdm",
            "gf": "functions.lowest",
            "gg": "functions.highest",
            "gh": "sep"
        }

        parsed = self.sourceCode # The (result) parsed string.
        replace_indexes = {} # An dictionary that will hold the tags and their index lists.

        for tag in mappings.keys():
            # Find every index that needs to be replaced for the current iterated key (escaping strings).
            indexes = self.getIndexesOfSubstrings(parsed, tag, escapeString = True)
            if len(indexes):
                replace_indexes[tag] = indexes # Mark the key to hold it's own index list.

            #DEBUG: print(replace_indexes)
            #DEBUG: print("\n")

        replace_tags = replace_indexes.keys()
        for tag in replace_tags:
            fullForm = mappings[tag] # Find the full name for the tag.
            rightShift = len(fullForm) - len(tag) # Calculate the required amount of shifting.
            tagIndexList = replace_indexes[tag] # Hold the <tag>s index list.

            minusIndex = 0

            for i, tagIndex in enumerate(tagIndexList):
                tagCounter = i + 1
                # Increase <replace_indexes[tag]>s every index.
                while len(tagIndexList) != tagCounter:
                    replace_indexes[tag][tagCounter] += rightShift
                    tagCounter += 1

                # Shift every other lists index.
                for otherTag in replace_tags:
                    if otherTag == tag:
                        continue # Same tag -> discard.

                    if tagIndex == -1:
                        continue # Already inserted -> discard.

                    # Loop over the other index lists, and increment if necessary.
                    for j in range(len(replace_indexes[otherTag])):
                        otherIndex = replace_indexes[otherTag][j]

                        if otherIndex >= tagIndex:
                            replace_indexes[otherTag][j] += rightShift

                # Insert the current full-form to the <tagIndex>.
                parsed = self.insertToString(parsed, fullForm, tagIndex + len(tag))
                # Delete the tag.
                parsed = self.deleteCharsAtIndex(parsed, len(tag), tagIndex)
                # Mark as a rotten tag.
                replace_indexes[tag][minusIndex] = -1
                minusIndex += 1
                
                #DEBUG: print(parsed)
                #DEBUG: print(replace_indexes)
                #DEBUG: print("-------------------------------------------------------")

        return parsed
        

    def run(self):
        exec(self.parse())

    # Tested.
    def insertToString(self, string, content, index):
        return string[:index] + content + string[index:]

    # Tested.
    def deleteCharsAtIndex(self, string, count, index):
        lst = list(string)

        for i in range(count):
            del lst[index]

        return "".join(lst)

    # Tested.
    def getIndexesOfSubstrings(self, string, subString, escapeString = False):
        """Returns all indexes of <subString> inside string in sorted order.\n
        <escapeString> determines whether we should escape strings marked with \"."""
        subLength = len(subString)
        indexes = []
        
        doubleQuoteStack = 0


        for i in range(len(string) - subLength + 1):
            if string[i] == "\"":
                if doubleQuoteStack:
                    doubleQuoteStack -= 1
                else:
                    doubleQuoteStack += 1

            # We dismiss the loop, since we're at even number of double quotes.
            if escapeString and doubleQuoteStack:
                continue

            if string[i:i + subLength] == subString:
                indexes.append(i)

        return indexes
