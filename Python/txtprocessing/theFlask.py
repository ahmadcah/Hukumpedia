import json
import numpy as np
import tensorflow as tf
from flask import Flask, request
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

app = Flask(__name__)

model = tf.keras.models.load_model('../../BangkitCapstone/checkpoint/model')

with open('../../BangkitCapstone/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)


@app.route("/predict", methods=["POST"])
def predict():
    request_json = request.json
    print("data: {}".format(request_json))
    print("type: {}".format(type(request_json)))

    token_list = tokenizer.texts_to_sequences(request_json.get("data"))[0]
    token_list = pad_sequences([token_list], maxlen=1)

    predictions = model.predict(token_list)

    indices = np.argpartition(predictions, -10)[0][-10:]

    results = {}
    for index in indices:
        key = [k for (k, v) in tokenizer.word_index.items() if v == index]
        results.update({key[0]: predictions[0, index]})

        results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}

    prediction_string = [str(d) for d in results]
    response_json = {
        "prediction": list(prediction_string)
    }

    return json.dumps(response_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

