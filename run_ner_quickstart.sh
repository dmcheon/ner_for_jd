#transformers.__version__ 
#4.35.2

export OUTPUT_PATH="./outputs"

# training
python run_ner.py \
  --model_name_or_path bert-base-uncased \
  --dataset_name conll2003 \
  --output_dir ${OUTPUT_PATH} \
  --do_train \
  --do_eval

# prediction
python run_ner.py \
  --model_name_or_path ${OUTPUT_PATH} \
  --dataset_name "./custom_data" \
  --output_dir ${OUTPUT_PATH}/eval \
  --do_eval --do_predict