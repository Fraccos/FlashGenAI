import fitz
import openai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
bufferPath = "./buffers/"


def filterUselessText(text):
    removeLines = [
        "Antonio Ferrara | Fondamenti del Web (Ingegneria del Software e Fondamenti Web)",
        "Fondamenti del Web",
        "Corso di Laurea in Ingegneria Informatica e dell’Automazione",
        "Anno Accademico 2022/2023",
        "Prof. Antonio Ferrara ",
        "Ingegneria del Software e Fondamenti Web "
    ]
    for rem in removeLines:
        text = text.replace(rem, "")
    return text

def filterSlideName(text):
    #Ip: i titoli si trovano tra le prime righe (max prime 3) e jhanno
        #Un numero di parole <= 3
    lines = text.splitlines()

def formatOutput(text, isLastline):
    return text
    text = re.sub(r"^\[", "", text)
    lastSquareRep = ","
    if (isLastline):
        lastSquareRep = ""
    text = re.sub(r"\]$", lastSquareRep, text)
    return text

def getBufferPagePath(page):
    return bufferPath + str(page) + ".json"



def saveOutputToBuffer(output, page):
    with open(getBufferPagePath(page), "w") as file:
        file.write(output)
    file.close()



def isPageBuffered(page):
    return os.path.isfile(getBufferPagePath(page));

def isOutJSONExist(inputFilename):
    return os.path.isfile(getJSONPath(inputFilename))

def getJSONPath(inputFilename):
    return "./out/" + re.sub(r"\.pdf$", ".json", inputFilename) 

def genFlashCardPrompt(text):
    #type: "flashcard"
    res = 'In base al contesto, mi puoi generare delle flashcard,in Inglese, come array di oggetti JSON dove ogni flashcard è un oggetto che rispetta queste proprietà: { "question":"", "answer": ""}, la risposta deve essere un codice JSON valido senza commenti, a partire dal seguente testo:  '
    res += text
    return res

def fixJSONBufferError(text):
    splitted = text.splitlines()
    fistLine = splitted[0]
    lastLine = splitted[-1]
    if not re.match(r'^\[', fistLine):
        text = "[ " + text
    if not re.match(r'\]$', lastLine):
        text += "]"
    return text

def JSONfromBuffers(filename, buffersSize, startIndex):
    #with open(getJSONPath(filename), "w") as destfile:
    #    destfile.write("[\n")
    flashcardObj = {
        "filename": filename,
        "cards" : []
    }
    for pageIndex in range(startIndex,buffersSize+1):
        with open(getBufferPagePath(pageIndex), 'r') as srcFile:
            file_contents = srcFile.read()
            file_contents = fixJSONBufferError(file_contents)
            print("\n\n" + str(pageIndex))
            print(file_contents)
            array = json.loads(file_contents)
            flashcardObj.get("cards").append({
                pageIndex: array
            })
            srcFile.close()
    #Flush buffers 
    with open(getJSONPath(filename), "w") as destfile:
        destfile.write(json.dumps(flashcardObj))
        destfile.close()
    for pageIndex in range(startIndex,buffersSize+1):
         os.remove(getBufferPagePath(pageIndex))    


def runFile(filename): 
    if not os.path.isfile(filename):
        print("\nERRORE: File ", filename, "non esiste, controlla errori di battitura nel nome del file" )
        return False
    if isOutJSONExist(filename):
        return True
    doc = fitz.open(filename)
    text = ""
    pIndex = 0
    print("\n[---------]  " + filename + " [---------]" )
    for page in doc:
        text = page.get_text()
        text = filterUselessText(text)
        pIndex = pIndex + 1
        print("\n\nPage: " + str(pIndex) + "\n" )
        if (pIndex > 1):
            if not isPageBuffered(pIndex):
                completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=
                        [{
                            "role": "user", 
                            "content": genFlashCardPrompt(text)
                        }]
                )
                output = completion["choices"][0]["message"]["content"]
                print(output);
                isLastline = pIndex == len(doc) - 1
                output = formatOutput(output, isLastline)
                saveOutputToBuffer(output,pIndex)
            else:
                print(" * Page is already buffered!")
    JSONfromBuffers(filename, len(doc), 2)
    doc.close()
    print("\n\n*** COMPLETATO ***")

runFile("f.spl.securityprotection2.pdf")
print("\n*** TUTTI I FILE SONO STATI COMPLETATI ***\n")