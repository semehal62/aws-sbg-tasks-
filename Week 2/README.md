# Mini Semantic Search

A small semantic search engine over a set of FAQs. It finds answers by meaning rather than exact keywords.

## What it does

1. Loads a CSV of FAQs with Pandas
2. Cleans the text and splits it into chunks
3. Embeds each chunk with `all-MiniLM-L6-v2` (sentence-transformers)
4. Stores the embeddings in a Chroma vector database
5. Takes a query and prints the top 3 matches

## Files

- `semantic_search.ipynb`: the notebook with all the code
- `FAQ.csv`: the FAQ dataset
- `requirements.txt`: Python dependencies

## How to run

1. Open `semantic_search.ipynb` in Google Colab (or Jupyter)
2. Run all cells from top to bottom (**Runtime → Run all**)
3. Or install the dependencies locally with `pip install -r requirements.txt`

## Example queries

**Query:** "I forgot my login details"

Top match: [paste the top FAQ question here] (similarity: [score])

**Query:** "How can I get my money back?"

Top match: [paste the top FAQ question here] (similarity: [score])

**Query:** "The app is really laggy"

Top match: [paste the top FAQ question here] (similarity: [score])

## How it works

- **Cleaning:** removes missing rows, duplicates, HTML tags and extra whitespace
- **Chunking:** splits text into chunks of up to 100 words with a 20-word overlap
- **Embedding:** each chunk becomes a 384-number vector that represents its meaning
- **Search:** the query is embedded the same way, and Chroma returns the 3 closest chunks by cosine similarity

## Notes

[One or two sentences on what you noticed, for example: which queries worked well, or one that returned a surprising result and why.]