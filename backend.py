from flask import Flask, request, jsonify
import json
import google.generativeai as genai

app = Flask(__name__)

with open("knowledge_base.json", "r") as file:
    knowledge = json.load(file)

# Set your Gemini API key
genai.configure(api_key="AIzaSyAEho69-SwcfSIy0WEWeQe0HGwsraXGJKg")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.json
    question = data.get("question", "")

    context = f"""
    BSA: {knowledge['bsa']}
    BNS: {knowledge['bns']}
    Legal Terms: {knowledge['legal_terms']}
    Case Summaries: {', '.join(knowledge['case_summaries'])}
    """

    prompt = f"""
    You are a helpful legal assistant for Indian professionals.

    Context: {context}

    Question: {question}

    Answer clearly and concisely.
    """

    response = model.generate_content(prompt)

    answer = response.text
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=5001)
