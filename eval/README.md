---
tags:
- generated_from_trainer
datasets:
- /content/custom_data
model-index:
- name: eval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# eval

This model is a fine-tuned version of [/content/outputs](https://huggingface.co//content/outputs) on the /content/custom_data dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.4540
- eval_precision: 0.0
- eval_recall: 0.0
- eval_f1: 0.0
- eval_accuracy: 0.9236
- eval_runtime: 195.3595
- eval_samples_per_second: 199.417
- eval_steps_per_second: 24.928
- step: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.1+cu117
- Datasets 2.15.0
- Tokenizers 0.13.3
