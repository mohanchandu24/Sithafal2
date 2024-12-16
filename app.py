from flask import Flask, request, jsonify
from utils.scrape_website import scrape_website
from utils.generate_embeddings import generate_embeddings
from utils.vector_store import create_vector_store, retrieve_similar_chunks
from utils.handle_queries import generate_response

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_website():
    data = request.json
    url = data['url']
    user_query = data['query']
    
    # Step 1: Scrape website and preprocess text
    text = scrape_website(url)
    chunks = chunk_text(text)
    
    # Step 2: Generate and store embeddings
    embeddings = generate_embeddings(chunks)
    vector_store = create_vector_store(embeddings)
    
    # Step 3: Retrieve relevant chunks
    relevant_chunks = retrieve_similar_chunks(user_query, vector_store)
    
    # Step 4: Generate response
    response = generate_response(user_query, relevant_chunks)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
