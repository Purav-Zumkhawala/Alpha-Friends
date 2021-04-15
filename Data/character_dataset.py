import random
import json

main_character = 'Ross Geller'
dialogue_threshold = 2
word_threshold = 5
num_candidates = 19
history_threshold = 5

datasets = {'train': [], 'valid': [], 'test':[]}
with open("Sequential Utterances/s1_utterances.txt") as f:
    corpus = [line.rstrip() for line in f]

json_file = open("Dataset/s1_dataset.json","r")
scene_ids = json.load(json_file)

for scene_id in scene_ids:
	print(scene_id)
	if scene_ids[scene_id]['count'][main_character] < dialogue_threshold:
		continue

	id = random.choices(list(datasets.keys()),[8,1,1])[0]
	history = []
	history_speakers = []

	for speaker, dialogue in scene_ids[scene_id]['dialogues']:
		if len(history)> history_threshold and speaker == main_character:
			candidates = []
			candidates = random.sample(corpus, num_candidates)

			while dialogue in candidates:
				candidates = random.sample(corpus, num_candidates)

			candidates.append(dialogue)

			utterances = {"candidates": candidates, "history": history, "history_speakers" : history_speakers}
			sample = {"utterances": utterances}
			print(sample)
			datasets[id].append(sample)

		history.append(dialogue)
		history_speakers.append(speaker)



with open('ross_s1.json', 'w') as fp:
    json.dump(datasets, fp)


		   


