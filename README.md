# Alpha-Friends

## Data
We have gotten our data from the emory NLP. Here is the link for the same: https://github.com/emorynlp/character-mining/tree/master/json

To generate the data required for our methods we have attached 2 files that would generate all the data required for both the methods Vanilla GPT2 and the Transfer Transfero method.

###Steps:
	1. Run the Extract_data_from_emoryNLP.py file. This would generate the data for each season in the "Dataset" folder and the utternances in "Sequence Utterance" folder.  

	2. This code would also generate character related data for the "vanilla gpt2". Please change the character name to the particular character that you want to generate data for. Currently it is set to "Ross Geller".

	3. For running the vanilla GPT2, do the following:


	4. Transfer Transfo method expects dataset in a different format as it is trained on a different task. We sample candidates and provide history for each utterance in the dataset. To generate the dataset for Transfer Transfo, please run the following command and replace "Monica Geller" with the desired character. 
	```python
	python .\character_dataset.py "Monica Geller"
	```

	Monica_Geller_all.json will be generated from this. 
