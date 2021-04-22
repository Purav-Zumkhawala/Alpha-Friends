
# For Alpha-Friends

python train.py --dataset_path '.\Monica Geller.json' --dataset_cache monica_5-18 --character "Monica Geller" --max_history 4 --model_checkpoint gpt2 --train_batch_size 2 --valid_batch_size 2

The dataset_path should be sent for all updated datasets with a new dataset_cache name. If you don't pass it, the dataset_cache will be taken as default and that might already be used.

For every change in the dataset, use new dataset_path and dataset_cache.

Default character is "Ross Geller". Please change it for the respective character.


