import random
import json
import collections

main_character = 'Ross Geller'
dialogue_threshold = 0
word_threshold = 5
num_candidates = 19
history_threshold = 5

datasets = {'train': [], 'valid': [], 'test':[]}

corpus = []
scene_ids = {}
files = ['season_01', 'season_02', 'season_03', 'season_04', 'season_05', 'season_06', 'season_07', 'season_08', 'season_09', 'season_10']

for file in files:
	f = open("Sequence_Utterences/" + file + ".txt")
	file_corpus = [line.rstrip() for line in f]
	corpus += file_corpus
	json_file = open("Dataset/"  + file + ".json","r")
	scene_ids.update(json.load(json_file))


length = collections.defaultdict(int)
file_all_speakers = open("script_all_speakers_dialogue.txt","w")
file_all_speakers_per_scene = open("script_all_speakers_dialogue_per_scene.txt","w")

file_mg = open("script_mg_all_dialogue.txt","w")
file_mg_per_scene = open("script_mg_all_dialogue_per_scene.txt","w")

for scene_id in scene_ids:
	for speaker, dialogue in scene_ids[scene_id]['dialogues']:
		file_all_speakers.write(speaker+": "+dialogue+"\n")
		file_all_speakers_per_scene.write(speaker+": "+dialogue)
		if speaker == "Monica Geller":
			speaker_bos = "<" + speaker + ">"
			speaker_eos = "<\\" + speaker + ">"
			file_mg.write(speaker_bos+": "+dialogue+speaker_eos+"\n")
			file_mg_per_scene.write(speaker_bos+": "+dialogue+speaker_eos)
		else:
			file_mg.write(dialogue+"\n")
			file_mg_per_scene.write(dialogue)
	file_all_speakers_per_scene.write("\n")
	file_mg_per_scene.write("\n")
file_all_speakers.close()


for scene_id in scene_ids:
	if scene_ids[scene_id]['count'][main_character] < dialogue_threshold:
		continue

	id = random.choices(list(datasets.keys()),[8,1,1])[0]
	history = []
	history_speakers = []

	for speaker, dialogue in scene_ids[scene_id]['dialogues']:
		if len(history)> history_threshold and speaker == main_character:
			if len(dialogue.split()) < 5 or len(dialogue.split()) > 18:
				continue

			candidates = []
			candidates = random.sample(corpus, num_candidates)

			while dialogue in candidates:
				candidates = random.sample(corpus, num_candidates)

			candidates.append(dialogue)
			print("---")
			if len(history_speakers) > 1:
				print(history[-2])
				print(history[-1])
			print(dialogue)
			print("---")


			utterances = {"candidates": candidates, "history": history, "history_speakers" : history_speakers}
			sample = {"utterances": utterances}
			# print(sample)
			datasets[id].append(sample)

		length[len(dialogue.split())] += 1
		# print(speaker,": ", dialogue)
		history.append(dialogue)
		history_speakers.append(speaker)

print("train ", len(datasets['train']))
print("test ", len(datasets['test']))
print("valid ", len(datasets['valid']))
# print("length ", length)

for l in sorted(length):
	print(l,"->",length[l])
with open(main_character + '.json', 'w') as fp:
    json.dump(datasets, fp)


		   


