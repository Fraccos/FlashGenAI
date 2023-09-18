
# FlashGenAI

This simple Python script allows you to generate flashcards in the question-and-answer format from the text of a set of PDFs, using the large language model (LLM) OpenAI. 

This tool is not meant to replace the active study process of thinking about a question (or a variation of an existing one) and providing an answer, but it can help you to quickly and easily create a large pool of questions to start with.


## Warning ⚠️	:

⚠️	The OpenAI API are billed proportionally the words sent as input to GPT model, so it's strongly suggested to put a billing limit ti the API Key before using it, to avoid unwanted high API cost
## Features

- Choose lang of the Flashcard
- Buffer to save the output
- JSON Format
- Use regex to filter PDF text before the generation of the flashcards
- Easy to use with the JFlashcard player


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY` = API KEY used for the script to generate the card



## Usage/Examples

```javascript
python3 main.py --file sample.pdf --lang en
```

