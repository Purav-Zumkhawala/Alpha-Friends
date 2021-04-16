import sys
import os
import contractions
import re

def filterfiles(files):
    # Using readlines()
    for file in files:
        myfile = open(f"../Sequence_Utterences/{file}", 'r')
        Lines = myfile.readlines()

        try:
            newfile = open(file, 'x')
            newfile.close()
        except:
            pass

        for line in Lines:
            # print("here")
            text = line.strip()
            # print(text)
            # creating an empty list
            expanded_words = []    

            for word in text.split():
                # using contractions.fix to expand the shotened words
                expanded_words.append(contractions.fix(word))   

            expanded_text = ' '.join(expanded_words)

            expanded_text = expanded_text.replace('"', '')
            # text = text.rstrip('\'')
            # text = text.rstrip('\'')
            if expanded_text.find('\'') > 0:
                matches = re.findall('\'[^\']+\'.', expanded_text)
                if len(matches) > 0:
                    # print()
                    # print(expanded_text)
                    # print(matches)
                    # # for stuff in matches:
                    # #     if stuff.find('\'') != -1:
                    # #         print(stuff)
                    # #         print(matches)
                    # print()
                    # expanded_text = expanded_text.replace("\'", '')
                    continue
            # if len(matches) != 0:
            #     print(text)

            # single = [m.start() for m in re.finditer('\'', expanded_text)]
            # if len(single) != 0:
            #     # print(single)
            #     count = 0
            #     for quoteidx in single:
            #         count += 1
            #         if expanded_text[quoteidx + 1] != 's':
            #             print(expanded_text)

                # exit(-1)
            # expanded_text = expanded_text.replace('\'', '')

            newfile = open(file, 'a')
            newfile.write(text + '\n')
            newfile.close()
            # print(expanded_text)
            # exit(-1)
        # exit(-1)
    print("Done...")

def main():
    print("Filtering...")
    for (root,dirs,files) in os.walk('../Sequence_Utterences/', topdown=True):
        print("Getting all files...")
    # print(files)
    filterfiles(files)

if __name__ == "__main__":
    main()