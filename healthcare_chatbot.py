import re

# --------------------
# INTENTS (UNCHANGED – MANY INTENTS)
# --------------------
intents = {
    # Basic conversation
    "greeting": ["hello", "hey", "good morning", "hi", "good evening"],
    "goodbye": ["bye", "exit", "quit", "thank you"],

    # General symptoms
    "fever": ["fever", "high temperature"],
    "cold": ["cold", "cough", "sneeze", "runny nose"],
    "headache": ["headache", "migraine", "head pain"],
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

# --------------------
# RESPONSES (AGE BASED)
# --------------------
responses = {

    "greeting": {
        "child": "Hello! How can I help you today?",
        "adult": "Hello! How can I assist you with your health today?",
        "elderly": "Hello! Please tell me your health concern."
    },

    "goodbye": {
        "child": "Take care!",
        "adult": "Take care! Stay healthy.",
        "elderly": "Wishing you good health."
    },

    "fever": {
        "child": "Monitor temperature and give plenty of fluids. Consult a pediatrician if fever persists.",
        "adult": "Drink fluids and rest. Consult a doctor if fever continues.",
        "elderly": "Fever in elderly can be serious. Seek medical advice promptly."
    },

    "headache": {
        "child": "Ensure hydration and rest. Reduce screen time.",
        "adult": "Headache may be due to stress or dehydration. Rest is advised.",
        "elderly": "Monitor blood pressure and consult a doctor if headache persists."
    },

    "body_pain": {
        "child": "Body pain may be due to activity. Rest is advised.",
        "adult": "Take rest and avoid strenuous activity.",
        "elderly": "Body pain may be joint-related. Medical consultation recommended."
    },

    "stomach_pain": {
        "child": "Avoid junk food and give light meals.",
        "adult": "Avoid spicy food and drink warm water.",
        "elderly": "Stomach pain should be evaluated by a doctor."
    },

    "breathing_problem": {
        "child": "Seek immediate medical attention.",
        "adult": "Please consult a doctor immediately.",
        "elderly": "Emergency symptoms detected. Get medical help urgently."
    },

    "diabetes": {
        "child": "Blood sugar issues in children require medical supervision.",
        "adult": "Maintain diet and monitor sugar levels.",
        "elderly": "Regular sugar monitoring and doctor consultation required."
    },

    "blood_pressure": {
        "child": "BP issues in children need medical evaluation.",
        "adult": "Monitor BP and reduce stress.",
        "elderly": "Strict BP monitoring and regular checkups needed."
    },

    "emergency": {
        "child": "This is an emergency. Contact medical services immediately.",
        "adult": "Medical emergency detected. Call emergency services.",
        "elderly": "Emergency detected. Seek immediate medical help."
    },

    "default": {
        "child": "Please consult a pediatrician.",
        "adult": "Please consult a medical professional.",
        "elderly": "Medical consultation is strongly recommended."
    }
}

# --------------------
# TEXT NORMALIZATION
# --------------------
def normalize(text):
    text = text.lower()

    replacements = {
        "paining": "pain",
        "aching": "ache",
        "hurting": "hurt",
        "hurts": "hurt",
        "painful": "pain"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

# --------------------
# INTENT PREDICTION (UNCHANGED)
# --------------------
def predict_intent(user_input):
    user_input = normalize(user_input)
    words = user_input.split()

    best_match = None
    max_score = 0

    for intent, keywords in intents.items():
        score = 0
        for keyword in keywords:
            keyword_words = keyword.split()

            if keyword in user_input:
                score += 3

            for w in keyword_words:
                if w in words:
                    score += 1

        if score > max_score:
            max_score = score
            best_match = intent

    return best_match if best_match else "default"

# --------------------
# CHATBOT RESPONSE (AGE BASED)
# --------------------
def chatbot_response(user_input, age_group="adult"):
    intent = predict_intent(user_input)
    intent_responses = responses.get(intent, responses["default"])
    return intent_responses.get(age_group, intent_responses["adult"])
