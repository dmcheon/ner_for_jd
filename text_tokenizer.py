from tqdm.notebook import tqdm
import json
import stanza

def get_json() :
    with open("/content/drive/MyDrive/Colab Notebooks/2023project/data.json", "r") as json_file:
        json_origin = json.load(json_file)
    return json_origin
   
# variable for checking first description
# example_sentences = json_origin['data'][0]['description']

def get_tokens(json_origin):
    data = json_origin['data']
    description_list = []
    for i, d in enumerate(data):
        description_list.append(d['description'])

    nlp = stanza.Pipeline(lang='en', processors='tokenize')
    token_dict_list = []

    for i, description in tqdm(enumerate(description_list), total=len(description_list)):
        doc = nlp(description)
        token_list = []

        for sentence in doc.sentences:
            token_list.append([token.text for token in sentence.tokens])

        for j, token in enumerate(token_list):
            token_dict_list.append(
                {"id": str(i) + "-" + str(j),
                "tokens": token,
                "chunk_tags": [0 for i in range(len(token))],
                "pos_tags": [0 for i in range(len(token))],
                "ner_tags": [0 for i in range(len(token))]}
                )
            
    return token_dict_list

def save_toknized_json(token_dict_list):
    file_path = "./token_data.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(token_dict_list, file, indent="\t")
        



# code to check first description result
# nlp = stanza.Pipeline(lang='en', processors='tokenize')
# doc = nlp(example_sentences)
# for i, sentence in enumerate(doc.sentences):
#     print(f'====== Sentence {i+1} tokens =======')