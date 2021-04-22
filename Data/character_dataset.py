import random
import json
import collections

main_character = 'Monica Geller'
dialogue_threshold = 0
word_threshold = 5
num_candidates = 19
history_threshold = 5
generate_scripts = False


datasets = {'train': [], 'valid': [], 'test':[]}

corpus = []
scene_ids = {}
files = ['season_01', 'season_02', 'season_03', 'season_04', 'season_05', 'season_06', 'season_07', 'season_08', 'season_09', 'season_10']

for file in files:
	f = open("Sequence_Utterences_all/" + file + ".txt")
	file_corpus = [line.rstrip() for line in f]
	corpus += file_corpus
	json_file = open("Dataset/"  + file + ".json","r")
	scene_ids.update(json.load(json_file))


length = collections.defaultdict(int)

initials = ''.join([s[0] for s in main_character.split(" ")])

if generate_scripts:
	file_all_speakers = open("script_all_speakers_dialogue.txt","w")
	file_all_speakers_per_scene = open("script_all_speakers_dialogue_per_scene.txt","w")
	file_char = open("script_"+ initials +"_all_dialogue.txt","w")
	file_char_per_scene = open("script_"+ initials +"_all_dialogue_per_scene.txt","w")

	for scene_id in scene_ids:
		for speaker, dialogue in scene_ids[scene_id]['dialogues']:
			file_all_speakers.write(speaker+": "+dialogue+"\n")
			file_all_speakers_per_scene.write(speaker+": "+dialogue)
			if speaker == main_character:
				speaker_bos = "<" + speaker + ">"
				speaker_eos = "<\\" + speaker + ">"
				file_char.write(speaker_bos+dialogue+speaker_eos+"\n")
				file_char_per_scene.write(speaker_bos+dialogue+speaker_eos)
			else:
				file_char.write(dialogue+"\n")
				file_char_per_scene.write(dialogue)
		file_all_speakers_per_scene.write("\n")
		file_char_per_scene.write("\n")
	file_all_speakers.close()


for scene_id in scene_ids:
	id = random.choices(list(datasets.keys()),[8,1,1])[0]
	print("id: ",id)
	history = []
	history_speakers = []

	for speaker, dialogue in scene_ids[scene_id]['dialogues']:
		# print("speaker: ", speaker)
		# print("dialogue: ", dialogue)
		# for sp, h in zip(history,history_speakers):
		# 	print("--",sp,h)

		if speaker == main_character:
			candidates = []
			candidates = random.sample(corpus, num_candidates)

			# while dialogue in candidates:
			# 	candidates = random.sample(corpus, num_candidates)

			candidates.append(dialogue)
			print("---")
			if len(history_speakers) > 1:
				print(history[-2])
				print(history[-1])
			print(dialogue)
			print("---")

			utterances = {"candidates": candidates, "history": history.copy(), "history_speakers" : history_speakers.copy()}
			sample = {"utterances": utterances}
			datasets[id].append(sample)

		length[len(dialogue.split())] += 1
		history.append(dialogue)
		history_speakers.append(speaker)

print("train ", len(datasets['train']))
print("test ", len(datasets['test']))
print("valid ", len(datasets['valid']))
# print("length ", length)

for l in sorted(length):
	print(l,"->",length[l])

with open('_'.join(main_character.split()) + '_all.json', 'w') as fp:
    json.dump(datasets, fp)


# for d in datasets["valid"][-5:]:
# 	print("-"*40)
# 	print("CANDIDATES")
# 	print("-"*40)
# 	for candidate in d["utterances"]["candidates"]:
# 		print(candidate)
# 	print("-"*40)
# 	print("HISTORY")
# 	print("-"*40)
# 	for sp,h in zip(d["utterances"]["history_speakers"],d["utterances"]["history"]) :
# 		print(sp,":",h)
# 	print("="*40)
