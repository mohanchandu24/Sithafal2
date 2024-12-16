import openai

openai.api_key = "your_openai_api_key"

def generate_response(query, relevant_chunks):
    context = "\n".join(relevant_chunks)
    prompt = f"Based on the following data:\n{context}\nAnswer the question: {query}"
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5
    )
    return response['choices'][0]['text']
