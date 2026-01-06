intents = {
    # Basic conversation
    "greeting": ["hello", "hey", "good morning","hi", "good evening"],
    "goodbye": ["bye", "exit", "quit", "thank you"],

    # General symptoms
    "fever": ["fever", "high temperature"],
    "cold": ["cold", "cough", "sneeze", "runny nose"],
    "headache": ["headache", "migraine"],
    "body_pain": ["body pain", "body ache", "muscle pain"],
    "fatigue": ["tired", "fatigue", "weakness"],

    # Digestive issues
    "stomach_pain": ["stomach pain", "abdominal pain", "gas", "acidity"],
    "vomiting": ["vomiting", "nausea", "throw up"],
    "diarrhea": ["diarrhea", "loose motion"],
    "constipation": ["constipation", "hard stool"],
    "indigestion": ["indigestion", "bloating"],

    # Respiratory issues
    "breathing_problem": ["breathing problem", "shortness of breath"],
    "asthma": ["asthma", "wheezing"],
    "sore_throat": ["sore throat", "throat pain"],

    # Pain related
    "back_pain": ["back pain", "lower back pain"],
    "joint_pain": ["joint pain", "knee pain"],
    "toothache": ["toothache", "dental pain"],
    "ear_pain": ["ear pain", "earache"],

    # Skin & eye
    "skin_problem": ["skin rash", "itching", "allergy"],
    "eye_problem": ["eye pain", "red eye", "itchy eyes"],

    # Lifestyle & mental health
    "stress": ["stress", "anxiety", "tension"],
    "sleep_problem": ["sleep problem", "insomnia"],
    "depression": ["depression", "sadness"],

    # Chronic diseases
    "diabetes": ["diabetes", "blood sugar", "high sugar"],
    "blood_pressure": ["blood pressure", "bp", "hypertension"],
    "cholesterol": ["cholesterol", "lipid"],

    # Women health
    "menstrual_pain": ["period pain", "menstrual pain"],
    "pregnancy": ["pregnant", "pregnancy symptoms"],

    # Infections
    "covid": ["covid", "corona", "covid symptoms"],
    "flu": ["flu", "influenza"],
    "food_poisoning": ["food poisoning"],

    # First aid & emergency
    "injury": ["injury", "cut", "wound"],
    "burn": ["burn", "burn injury"],
    "emergency": ["chest pain", "severe bleeding", "unconscious"]
}

responses = {
    "greeting": "Hello! How can I assist you with your health today?",
    "goodbye": "Take care! Stay healthy.",

    "fever": "Fever detected. Drink fluids and consult a doctor if it persists.",
    "cold": "Cold symptoms detected. Take rest and drink warm fluids.",
    "headache": "Headache may be due to stress or dehydration. Rest is advised.",
    "body_pain": "Body pain detected. Take rest and avoid strenuous activity.",
    "fatigue": "Fatigue may be due to lack of sleep or stress. Proper rest is recommended.",

    "stomach_pain": "Stomach pain detected. Avoid spicy food and drink warm water.",
    "vomiting": "Vomiting detected. Take small sips of water and rest.",
    "diarrhea": "Diarrhea detected. Drink ORS and stay hydrated.",
    "constipation": "Constipation detected. Increase fiber intake and drink water.",
    "indigestion": "Indigestion detected. Avoid oily food and eat light meals.",

    "breathing_problem": "Breathing difficulty detected. Please consult a doctor immediately.",
    "asthma": "Asthma symptoms detected. Use prescribed inhaler and consult a doctor.",
    "sore_throat": "Sore throat detected. Gargle with warm salt water.",

    "back_pain": "Back pain detected. Maintain proper posture and avoid heavy lifting.",
    "joint_pain": "Joint pain detected. Avoid strain and consult a doctor if severe.",
    "toothache": "Toothache detected. Rinse with warm salt water and consult a dentist.",
    "ear_pain": "Ear pain detected. Avoid inserting objects and consult a doctor.",

    "skin_problem": "Skin allergy detected. Avoid scratching and consult a dermatologist.",
    "eye_problem": "Eye irritation detected. Avoid rubbing eyes and rest them.",

    "stress": "Stress detected. Practice relaxation techniques and take breaks.",
    "sleep_problem": "Sleep problem detected. Maintain a regular sleep schedule.",
    "depression": "Mental health concern detected. Please consider professional help.",

    "diabetes": "High blood sugar detected. Maintain diet and consult a doctor.",
    "blood_pressure": "Blood pressure issue detected. Monitor BP regularly.",
    "cholesterol": "Cholesterol concern detected. Follow a healthy diet.",

    "menstrual_pain": "Menstrual pain detected. Rest and warm compress may help.",
    "pregnancy": "Pregnancy related query detected. Please consult a healthcare professional.",

    "covid": "COVID symptoms suspected. Isolate yourself and get tested.",
    "flu": "Flu symptoms detected. Take rest and stay hydrated.",
    "food_poisoning": "Food poisoning suspected. Drink fluids and consult a doctor.",

    "injury": "Minor injury detected. Clean the wound and apply first aid.",
    "burn": "Burn injury detected. Cool the area with running water.",
    "emergency": "This is a medical emergency. Please contact emergency services immediately.",

    "default": "Sorry, I couldn't understand. Please consult a medical professional."
}
def normalize(text):
    replacements = {
        "paining": "pain",
        "hurting": "pain",
        "hurt": "pain",
        "aching": "pain",
        "ache": "pain"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def predict_intent(user_input):
    user_input = normalize(user_input.lower())
    words = user_input.split()

    for intent, keywords in intents.items():
        for keyword in keywords:
            keyword_words = keyword.split()


            if all(word in words for word in keyword_words):
                return intent

    return "default"


def chatbot_response(user_input):
    intent = predict_intent(user_input)
    return responses.get(intent, responses["default"])
