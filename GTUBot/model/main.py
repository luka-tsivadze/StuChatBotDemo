
# ეს არის საქართველოს უნივერსიტეტის ჩატბოტის კოდი რომელიც ინფორმაციას აწვდის chat-bot component ს
# install necessary libraries
# pip install quart quart-cors
# გახსენი მთლიანი GTU-BOT ფოლდერი შემდეგ კი გაუშვი ეს ფაილი 
from difflib import SequenceMatcher, get_close_matches
from quart import Quart, request, jsonify, render_template, session, send_from_directory
from quart_cors import cors, route_cors
from datetime import datetime
import re, uuid, random, json, time

app = Quart(__name__)
app = cors(app, allow_origin="*")  # Enable CORS for all origins
app.secret_key = 'your_secret_key'

class QABot:
    def __init__(self):
        self.datasets = self.load_datasets()
        self.questions, self.answers = self.qa_extract(self.datasets)
        self.rules = {
            'greetings': ['გამარჯობა', 'ჰელო', 'გაუ', 'გაუმარჯოს', 'ზდაროვა', 'სალამი', 'ჰეი', 'მოგესალმებით'],
            'farewells': ['კარგად', 'ნახვამდის', 'აბა შენ იცი', 'კარგად იყავი', 'ბაი', 'გუდბაი']
        }
        self.stop_words = ['ჩამომითვალე', 'გთხოვ', 'თუ შეიძლება', 'მითხარი', 'გთხოვთ', 'გეჩვენება', 'შეიძლება', 'მაინტერესებს']
        self.all_stop_words = self.stop_words + self.rules['greetings'] + self.rules['farewells']

    def load_datasets(self):
        general = self.load_data('data/qa-dataset/handwriten-qa.json')
        rectors = self.load_data('data/qa-dataset/rectors-qa.json')
        faculties = self.load_data('data/qa-dataset/faculties-qa.json')
        return [general, rectors, faculties]

    def load_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def qa_extract(self, datasets):
        questions = []
        answers = []
        for dataset in datasets:
            questions.extend([pair["question"] for pair in dataset])
            answers.extend([pair["answer"] for pair in dataset])
        return questions, answers

    def find_best_match(self, user_question):
        cleaned_question = self.remove_stop_words(user_question)
        best_match = None
        highest_similarity = 0
        for i, question in enumerate(self.questions):
            cleaned_dataset_question = self.remove_stop_words(question)
            similarity = SequenceMatcher(None, cleaned_question, cleaned_dataset_question).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = self.answers[i]
        if highest_similarity > 0.8:
            return best_match
        else:
            return ("ბოდიშს გიხდით, დასმულ შეკითხვაზე არასაკმარისი ინფორმაციის გამო ვერ გცემთ პასუხს "
                    "ან შეკითხვა გაუგებარია ჩემთვის. გთხოვთ გაიმეოროთ თქვენი შეკითხვა. "
                    "საჭიროების შემთხვევაში შეგიძლიათ მოგვმართოთ საკონტაქტო გზების საშუალებით: "
                    "\nტელეფონი: (+995 32) 2 77 11 11; \nE-mail: info@gtu.ge; contact@gtu.ge")

    def remove_stop_words(self, question):
        pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in self.all_stop_words) + r')\b', re.IGNORECASE)
        return pattern.sub('', question).strip()
    
    def greet(self, session_id):
        if session.get(f'{session_id}_greeting_counter', 0) > 2:
            greetings = ["კიდევ გამარჯობა!", "კიდევ მოგესალმებით!"]
            return random.choice(greetings)
        else:
            greetings = ["გამარჯობა!", "მოგესალმებით!"]
            return random.choice(greetings)

    def farewell(self):
        farewells = ["ნახვამდის!", "ბაი!", "გუდბაი!"]
        return random.choice(farewells)
    
    def prompt_greet(self, session_id):
        if session.get(f'{session_id}_greeting_counter', 0) > 2:
            greetings = ["კიდევ გამარჯობა, მითხარით რაში გჭირდებათ დახმარება?", "კიდევ მოგესალმებით! რით შემიძლია დაგეხმაროთ?", "ისევ მოგესალმებით! მითხარით რაში გჭირდებათ დახმარება?"]
            return random.choice(greetings)
        else:
            greetings = ["გამარჯობა, რით შემიძლია დაგეხმაროთ?", "მოგესალმებით! რით შემიძლია დაგეხმაროთ?", "გამარჯობა!"]
            return random.choice(greetings)
        
    def increment_greeting_counter(self, session_id):
        session[f'{session_id}_greeting_counter'] = session.get(f'{session_id}_greeting_counter', 0) + 1
    
    def find_close_match(self, user_input, categories, cutoff=0.6):
        all_keywords = []
        for keywords in categories.values():
            all_keywords.extend(keywords)
        matches = get_close_matches(user_input, all_keywords, n=1, cutoff=cutoff)
        if matches:
            matched_word = matches[0]
            for category, keywords in categories.items():
                if matched_word in keywords or matched_word.lower() in keywords:
                    return category
        return None

    def handle_other_rules(self, user_question, session_id):
        words = user_question.split()
        for word in words:
            category = self.find_close_match(word, self.rules)
            if category:
                if category == 'greetings':
                    session[f'{session_id}_greeting_counter'] = session.get(f'{session_id}_greeting_counter', 0) + 1
                    if len(words) < 3:
                        return self.prompt_greet(session_id)
                    else:
                        return self.greet(session_id)
                elif category == 'farewells':
                    return self.farewell()
        return None

    def answer_question(self, user_question, session_id):
        special_response = self.handle_other_rules(user_question, session_id)
        if special_response:
            if any(greeting in special_response for greeting in ["გამარჯობა", "მოგესალმებით"]) and len(user_question.split()) >= 3:
                return f"{special_response} {self.find_best_match(user_question)}"
            else:
                return special_response
        else:
            return self.find_best_match(user_question)

bot = QABot()

@app.route("/")
async def index():
    session_id = request.cookies.get('session_id', str(uuid.uuid4()))
    session['session_id'] = session_id
    if f'{session_id}_greeting_counter' not in session:
        session[f'{session_id}_greeting_counter'] = 0
    current_time = datetime.now().timestamp()
    return await render_template('index.html', current_time=current_time)


@app.route('/ask', methods=['POST'])
@route_cors(allow_origin="*")  # Allow requests from any origin for this route
async def chat():
    try:
        content = await request.get_json()
        user_question = content['question']
        session_id = content.get('session_id')  # Retrieve session ID from JSON request body
        if session_id is None:
            return jsonify({'error': 'Session ID not found'})
        bot.increment_greeting_counter(session_id)
        answer = bot.answer_question(user_question, session_id)
        response = {'question': user_question, 'answer': answer}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/static/<path:filename>')
async def static_files(filename):
    return await send_from_directory('static', filename, cache_timeout=0)

if __name__ == '__main__':
    app.run(debug=True)
