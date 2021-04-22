import json

json_file = open("Ross_Geller_all.json","r")

datasets = json.load(json_file)

print("train ", len(datasets['train']))
print("test ", len(datasets['test']))
print("valid ", len(datasets['valid']))
# for d in datasets["valid"]:
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
