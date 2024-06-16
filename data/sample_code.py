import json 

# load the training json file 
with open("train.json") as f:
	train_data = json.load(f) # train_data is a list of dictionaries, where each dictionary is an instance

count_data = len(train_data)
count_embodied_emotion = len([k for k in train_data if k['label'] == 'Embodied Emotion'])

print(f"There are", count_data, "training instances.")
print()
print(f"Among them, there are", count_embodied_emotion, "Embodied Emotion instances and",count_data - count_embodied_emotion, "Neutral instances.")
print()
# show one instance below  
instance = train_data[0]
preceding_sentences = " ".join([" ".join(ps) for ps in instance['preceding_context_tokens']])
sentence = " ".join(instance['tokens'])

print("Preceding Context:", preceding_sentences)
print()
print("Sentence:", sentence)
print()
print("Body Part to Classify:",  instance['tokens'][instance['body_part_token_idx']])
print()
print("Label:", instance['label'])

