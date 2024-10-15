# BERT based NER for JDs

My personal project - extracting information using pre-trained language models!

### Key takeaway from this project
* Utilize PLMs (Finetune on benchmark dataset, Inference on real-world text data)
* Data collection from real-world (webpage crawling)


### Further steps
Utilize LLMs to make data for entity types that do not have benchmark datasets i.e. without pre-existing annotations.

<hr>

## Quick start steps
1. Crawl data - (a)
2. Tokenize
3. Prepare PLM - fine-tune BERT on CoNLL data - (b)
4. Inference prepared data (a) using trained PLM (b)
5. Postprocessing
6. Gather data and use it on downstream applications (e.g. Visualization)

## Environments
Please see `requirements.txt`
Tested on Python 3.10.

## How to crawl

See `crawldata.py`.

Output of the code: `data.json` 
<i><b>(Omitted to avoid potential (unforeseen) license issue)</b></i>

Format (example):
```python
{
	"data": [
		{
			"university": "Center for ABC | Harvard & Smithsonian",
			"department": "",
			"job_code": "FELLOWS",
			"job_title": "Center for ABC Fellowship | Harvard",
			"deadline": "2023/11/12 11:59PM*",
			"apply_link": "https://<URLs>",
			"description": "The Center for ABC | Harvard and DEF is a joint (omitted)"
		},
    ]
}
```

Learned: TBA

## Tokenize

Using off-the-shelf NLP model [stanza](https://stanfordnlp.github.io/stanza/index.html) by StanfordNLP group ([Qi et al 2020 and Zhang et al. 2021](https://stanfordnlp.github.io/stanza/index.html#citing-stanza-in-papers))


## Prepare PLM - fine-tune BERT on CoNLL data

Using Transformers library (version 4.35.2) and BERT, we trained (fine-tune) and inferenced our datasets.

Main code: `run_ner.py` will `conll2003` data from HugginfFace hub.

```bash
# training
export OUTPUT_PATH="./outputs"
python run_ner.py \
  --model_name_or_path bert-base-uncased \
  --dataset_name conll2003 \
  --output_dir ${OUTPUT_PATH} \
  --do_train \
  --do_eval
```

Check [`./outputs`](./outputs) for report. 

Our models performance is:
* Precision: 0.9429
* Recall: 0.9497
* F1: 0.9463
* Accuracy: 0.9896

`pytorch_model.bin` is omitted as it is too large (435 MB) for uploading to a github repo. (added in `.gitingnore`)

## Inference prepared data using trained PLM

Main code: `run_ner.py` will load our custom data processing scripts located in `custom_data/custom_data.py`.
<br>The model will load our trained model from `$OUTPUT_PATH`.

Note that <b>I omitted train/dev/test dataset</b> to avoid potential (unforeseen) license issue. These should be in `custom_data` folder.

```bash
# prediction
python run_ner.py \
  --model_name_or_path ${OUTPUT_PATH} \
  --dataset_name custom_data \
  --output_dir ${OUTPUT_PATH}/eval \
  --do_eval --do_predict
```

Check [`./eval`](./eval) for report. Note that our inference run is on non-annotated data, which means there are no true labels. So F1 score of 0 is normal.
<br>`./eval/predictions.txt` is the final output for our prediction.

## Postprocessing 
TBA
Outputs: `origin_predict_result.csv`


## Visualization

TBA!
