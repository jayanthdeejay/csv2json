import csv
import json
import sys


def main():
    
    csvFile = open(sys.argv[1], 'r', encoding='utf-8')
    
    if len(sys.argv) == 3:
        jsonFile = open(sys.argv[2], 'w', encoding='utf-8')
    elif len(sys.argv) == 2:
        jsonFile = open('convertedTo.json', 'w', encoding='utf-8')
    else:
        print(repr("Usage: $ python csv2json.py [input].csv [output].json"))
        sys.exit(1)

    reader = csv.DictReader(csvFile)
    fieldNames = reader.fieldnames
    # print(fieldNames)
    fieldCount = {}
    arrayOfWorks = []
    dictOfWork = {}

    for x in fieldNames:
        key = value = ''
        for char in x:
            if(char >= '0' and char <= '9'):
                value += char
            else:
                key += char
        if((key in fieldCount) and (fieldCount[key] < int(value))):
            fieldCount[key] = int(value)
        elif(value.isnumeric()):
            fieldCount[key] = int(value)
        else:
            fieldCount[key] = 0

    # print(fieldCount)

    for row in map(dict, reader):
        for key in fieldCount.keys():
            value = fieldCount[key]
            if value == 0:
                dictOfWork[key] = row[key]
            else:
                dictValues = []
                for i in range(1, value+1):
                    if row[key+str(i)] == '':
                        break
                    else:
                        dictVal = row[key+str(i)]
                    dictValues.append(dictVal)
                dictOfWork[key] = dictValues

        # print(type(dictOfWork))
        # arrayOfWorks.append(dictOfWork)
        # print(type(json.dumps(dictOfWork, indent=4)))
        arrayOfWorks.append(eval(json.dumps(dictOfWork, indent=4)))
        # also checkout literal_eval
        # jsonFile.write(json.dumps(dictOfWork))
        # jsonFile.write(json.dumps(arrayOfWorks, indent=4))
        # jsonFile.write(json.dumps(arrayOfWorks, indent=4))

    # jsonFile.write(json.loads(arrayOfWorks), indent=4, sort_keys=True)
    # print(arrayOfWorks)
    jsonFile.write(json.dumps(arrayOfWorks))
    # Use python -m json.tool convertedTo.json >> pretty.json
    # to prettify the json file.


if __name__ == '__main__':
    main()
