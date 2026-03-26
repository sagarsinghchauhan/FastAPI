import  pickle
import sklearn.compose._column_transformer as _ct

import pandas as pd

# Patch for loading models pickled with sklearn 1.6.x in sklearn 1.8+
if not hasattr(_ct, '_RemainderColsList'):
    class _RemainderColsList(list):
        def get_indexer(self, target):
            return list(range(len(target)))
    _ct._RemainderColsList = _RemainderColsList

# import the ml model
with open ('model/model.pkl','rb') as f:
    model = pickle.load(f)

#MLFlow
MODEL_VERSION = "1.0.0"

# get class labels from model (important fro mactching probabilites to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])
    output =model.predict(input_df)[0]

    # get probalilties for all class 
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    #create mapping : {class_name : probabilities}
    class_probs  = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))

    return {
        "predicted_category": output,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }

