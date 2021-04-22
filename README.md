# Alpha-Friends

## Data
We got our data from the emory NLP. Here is the link for the same: https://github.com/emorynlp/character-mining/tree/master/json

To generate the data required for our methods we have attached 2 files that would generate all the data required for both the methods Vanilla GPT2 and the Transfer Transfo method.

## Steps:
1. Run the ``Extract_data_from_emoryNLP.py`` file. This would generate the data for each season in the "Dataset" folder and the utternances in "Sequence Utterance" folder. 

2. ``Extract_data_from_emoryNLP.py`` will also generate character related data for the "vanilla gpt2". Please change the character name to the particular character that you want to generate data for. Currently it is set to "Ross Geller".

3. Two systems have been implemented. Vanilla GPT2 as the baseline and TransferTransfo as the updated system. For running the vanilla GPT2, please follow the steps in Models/vanilla-gpt2/train-LM-GPT2.ipynb

4. TransferTransfo system expects dataset in a different format as it is trained on a different task. We sample candidates and provide history for each utterance in the dataset. To generate the dataset for Transfer Transfo, please run the following command and replace "Monica Geller" with the desired character. ``Monica_Geller_all.json`` will be generated from this. 

```python
python .\character_dataset.py "Monica Geller"
```
5. Go to ``Model/transfer-learning-conv-ai`` and install the required libraries using ``requirements.txt`` with pip.

6. To start the model training, please provide the following options.

```python
python train.py --dataset_path "../../Data/Monica_Geller_all.json" --dataset_cache monica --character "Monica Geller" --max_history 4 --model gpt2 --train_batch_size 2 --valid_batch_size 2
```

  - The dataset_path should be sent for all updated datasets with a new dataset_cache name. If you don't pass it, the dataset_cache will be taken as default and that might already be used.
  - For every change in the dataset, use new dataset_path and dataset_cache.
  - Default character is "Ross Geller". Please change it for the respective character.
  - Depending upon the available GPU size, you might have to change the batch size. This setup has worked for us on google colab.

7. After training, the trained model is saved in ``runs`` directory. Please identify the runs directory for your training. It is generally the last upadted one. We recommend using a table to identify different runs. Use the following command to start interacting with the trained model (If ``Apr20_02-08-28_141f0048dcc3_gpt`` is your runs save directory)

```python
!python interact.py --model_checkpoint "runs/Apr20_02-08-28_141f0048dcc3_gpt2" --character "Monica Geller" --model gpt2
```



> ## Note for Model/transfer-learning-conv-ai
> It is adopted from the implementation by huggingface available at - https://github.com/huggingface/transfer-learning-conv-ai. The original repo was used for PERSONA-CHAT dataset. 
> We have implemented changes for it to work with the FRIENDS dataset. It is significantly different from PERSONA-CHAT. The main differences are removal of personality, arbitrary speakers in history and presence of multiple-speakers. We have also added options to train it for different characters. The changes that we have made can be seen at https://github.com/ShubhamSanghvi/transfer-learning-conv-ai.


