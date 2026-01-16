import re

# --------------------
# INTENTS
# --------------------
intents = {
    "greeting": ["hello", "hey", "good morning", "hi", "good evening"],
    "goodbye": ["bye", "exit", "quit", "thank you"],

    "fever": ["fever", "high temperature"],
    "cold": ["cold", "cough", "sneeze", "runny nose"],
    "headache": ["headache", "migraine", "head pain"],
    "body_pain": ["body pain", "body ache", "muscle pain"],
    "fatigue": ["tired", "fatigue", "weakness"],

    "stomach_pain": ["stomach pain", "abdominal pain", "gas", "acidity"],
    "vomiting": ["vomiting", "nausea", "throw up"],
    "diarrhea": ["diarrhea", "loose motion"],
    "constipation": ["constipation", "hard stool"],

    "breathing_problem": ["breathing problem", "shortness of breath"],
    "asthma": ["asthma", "wheezing"],
    "sore_throat": ["sore throat", "throat pain"],

    "back_pain": ["back pain", "lower back pain"],
    "joint_pain": ["joint pain", "knee pain"],
    "toothache": ["toothache", "dental pain"],
    "ear_pain": ["ear pain", "earache"],

    "diabetes": ["diabetes", "blood sugar", "high sugar"],
    "blood_pressure": ["blood pressure", "bp", "hypertension"],

    "emergency": ["chest pain", "severe bleeding", "unconscious"]
}

# --------------------
# INTENT PRIORITY (FIXES CONFLICTS)
# --------------------
INTENT_PRIORITY = [
    "emergency",
    "breathing_problem",
    "headache",
    "stomach_pain",
    "back_pain",
    "joint_pain",
    "toothache",
    "ear_pain",
    "body_pain"
]

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
        "child": "Give fluids and monitor temperature. Consult a pediatrician if it continues.",
        "adult": "Rest well and stay hydrated. Consult a doctor if fever persists.",
        "elderly": "Fever can be serious at this age. Seek medical advice promptly."
    },

    "headache": {
        "child": "Ensure rest and hydration. Reduce screen time.",
        "adult": "Headache may be due to stress or dehydration. Rest is advised.",
        "elderly": "Monitor BP and consult a doctor if headache continues."
    },

    "body_pain": {
        "child": "Body pain may be due to activity. Rest is advised.",
        "adult": "Take rest and avoid heavy physical work.",
        "elderly": "Body pain may be joint-related. Medical consultation recommended."
    },

    "stomach_pain": {
        "child": "Avoid junk food. Give light meals.",
        "adult": "Avoid spicy food and drink warm water.",
        "elderly": "Stomach pain should be evaluated by a doctor."
    },

    "breathing_problem": {
        "child": "Seek immediate medical attention.",
        "adult": "Please consult a doctor immediately.",
        "elderly": "Emergency symptoms detected. Get help urgently."
    },

    "diabetes": {
        "child": "Blood sugar issues in children need medical supervision.",
        "adult": "Maintain diet and monitor sugar levels.",
        "elderly": "Regular sugar monitoring and doctor visits are required."
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
# INTENT PREDICTION
# --------------------
def predict_intent(user_input):
    user_input = normalize(user_input)
    words = user_input.split()
    scores = {}

    for intent, keywords in intents.items():
        score = 0
        for keyword in keywords:
            if keyword in user_input:
                score += 3
            for w in keyword.split():
                if w in words:
                    score += 1
        if score > 0:
            scores[intent] = score

    if not scores:
        return "default"

    max_score = max(scores.values())
    top_intents = [i for i, s in scores.items() if s == max_score]

    for intent in INTENT_PRIORITY:
        if intent in top_intents:
            return intent

    return top_intents[0]

# --------------------
# CHATBOT RESPONSE
# --------------------
def chatbot_response(user_input, age_group="adult"):
    age_group = age_group.lower().strip()
    if age_group not in ["child", "adult", "elderly"]:
        age_group = "adult"

    intent = predict_intent(user_input)
    intent_responses = responses.get(intent, responses["default"])
    return intent_responses.get(age_group, intent_responses["adult"])
