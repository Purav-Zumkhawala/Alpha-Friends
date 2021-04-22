#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import os
from pathlib import Path

def extractData(filepath):
    with open (filepath) as f:
        data = json.loads(f.read())
    required_data = {}
    episodes_data = data["episodes"]
    for episode in episodes_data:
        scenes_data = episode["scenes"]
        for scene in scenes_data:
            dialogue_list = []
            count_dict = {"Total":0,"Ross Geller":0, "Rachel Green":0, "Monica Geller":0, "Chandler Bing":0, "Joey Tribbiani":0,"Phoebe Buffay":0}
            for utterance in scene["utterances"]:
                if len(utterance["speakers"]) > 0:
                    temp_list = [",".join(utterance["speakers"]),utterance["transcript"]]
                    dialogue_list.append(temp_list)
                    if temp_list[0] in list(count_dict.keys()):
                        count_dict[temp_list[0]]+=1
                        count_dict["Total"]+=1
            required_data[scene["scene_id"]] = {"dialogues":dialogue_list,"count":count_dict}
    return required_data

def getSequenceWiseUtterences(filepath):
    count=0
    with open (filepath) as f:
        data = json.loads(f.read())
    dialogue_list = []
    episodes_data = data["episodes"]
    for episode in episodes_data:
        scenes_data = episode["scenes"]
        for scene in scenes_data:
            for utterance in scene["utterances"]:
                if len(utterance["speakers"]) > 0:
                    count+=1
                    dialogue_list.append(utterance["transcript"])
    return dialogue_list,count


def getCharacterDialogues(filepath,character):
    with open (filepath) as f:
        data = json.loads(f.read())
    episodes_data = data["episodes"]
    with open(character.split()[0]+'_dialogues_all.txt', 'a+') as result:
        for episode in episodes_data:
            scenes_data = episode["scenes"]
            for scene in scenes_data:
                temp = ""
                for utterance in scene["utterances"]:
                    if len(utterance["speakers"]) > 0:
                        if len(utterance["speakers"]) == 1 and  character in utterance["speakers"]:
                            temp += "<"+character.split()[0]+">" + utterance["transcript"] + "<end"+character.split()[0]+">"
                        else:
                            temp += utterance["transcript"]
                result.write(temp+"\n")
    
        

filepath = "Raw Data"
filenames = os.listdir(filepath)
storePath = ""
tcount = 0

if not os.path.exists(os.path.join(storePath,"Dataset")):
    os.mkdir("Dataset")
if not os.path.exists(os.path.join(storePath,"Sequence Utterances")):
    os.mkdir("Sequence Utterances")
    
for i in filenames:
    data_dict = extractData(os.path.join(filepath,i))
    json_save_path = Path(os.path.join(storePath,"Dataset",i.split(".")[0][8:]+".json"))
    json_save_path.write_text(json.dumps(data_dict))
    dialogue_list,count = getSequenceWiseUtterences(os.path.join(filepath,i))
    tcount+=count
    
    f = open(os.path.join(storePath,"Sequence Utterances",i.split(".")[0][8:]+".txt"), "w")
    for dialog in dialogue_list:
        f.write(dialog+"\n")
    f.close()
#     Change character name to generate required data file for Vanilla GPT2 method
    character = "Ross Geller"
    getCharacterDialogues(os.path.join(filepath,i),character)
    
    
print("Number of dialogues extracted",tcount)

