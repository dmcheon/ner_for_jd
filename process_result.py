import json
import csv


def get_text(path='predictions.txt'):
    f = open(path, "r")
    predict = []
    for line in f:
        predict.append(line)

    for i, line in enumerate(predict):
        predict[i] = line.split(' ')

    return predict


def get_json(path='token_data.json'):
    with open(path, "r") as f:
        json_data = json.load(f)

    origin = []
    for d in json_data:
        temp = d["tokens"]
        temp.insert(0, d["id"])
        origin.append(temp)
    return origin


def combine_data(predict, origin):
    origin_predict_result = []
    for i in range(len(predict)):
        origin_predict_result.append(origin[i])
        temp = predict[i]
        temp.insert(0, origin[i][0])
        origin_predict_result.append(temp)
    return origin_predict_result


def save_csv(result, path = 'origin_predict_result.csv'):
    with open(path, 'w') as f:
        write = csv.writer(f)
        write.writerows(result)


def open_csv(path='origin_predict_result_with_num.csv'):
    with open('origin_predict_result_with_num.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def extract_loc_and_org(data):
    description_idx = 0
    description = []
    b_tag = {'B-ORG', 'B-LOC'}
    tag = {'I-ORG', 'I-LOC'}
    location = []
    organization = []
    results = []
    for i, line in enumerate(data):
        idx = int(line[0].split('-')[0])
        # 새 job description에 도달한 경우 이전 description 정보들 results에 저장
        if idx > description_idx:
            result = []
            result.append(description_idx)
            result.append(list(set(location)))
            result.append
            results.append(result)

            location.clear()
            organization.clear()
            description_idx = idx

        # 짝수일 경우 문장 따로 저장
        if i % 2 == 0:
            description.clear()
            description = line

        # 홀수일 경우 tag들 보면서 저장해야 하는 단어인지 판별
        else:
            temp_words = []

            for j, word in enumerate(line):
                # B tag 이전의 단어들(완성된 단어들) organization이나 location 리스트에 추가.
                if word in b_tag:
                    if len(temp_words) > 0:
                        if temp_words[0] == 'B-LOC':
                            location.append(temp_words[1])
                        else:
                            organization.append(temp_words[1])
                        temp_words.clear()

                    # tag 정보 추가
                    temp_words.append(word)
                    # 실제 단어 추가
                    temp_words.append(description[j])

                elif word in tag:
                    # 간혹 B tag없이 I tag로 시작하는 케이스일때
                    if len(temp_words) == 0:
                        temp_words.append(word)
                        temp_words.append(description[j])
                    else:
                        temp_words[1] = temp_words[1] + ' ' + description[j]
    return results
