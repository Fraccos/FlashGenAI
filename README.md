## FlashGenAI

This simple Python script allows you to generate flashcards in the question-and-answer format from the text of a set of PDFs, using the large language model (LLM) OpenAI.

This tool is not meant to replace the active study process of thinking about a question (or a variation of an existing one) and providing an answer, but it can help you to quickly and easily create a large pool of questions to start with.

## Warning ⚠️

**⚠️** The OpenAI API is billed proportionally to the number of words sent as input to the GPT model, so it is strongly recommended to set a billing limit for the API key before using it, to avoid unwanted high API costs.

## Features

* Choose the language of the flashcard
* Buffer output
* JSON format
* Easy to use with the JFlashcard player

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

`OPENAI_API_KEY` = API KEY used for the script to generate the card



## Usage/Examples

```bash
python3 main.py --file sample.pdf --lang en
```

