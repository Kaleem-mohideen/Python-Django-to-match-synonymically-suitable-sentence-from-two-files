from sentence_transformers import SentenceTransformer, util
import tensorflow as tf
import numpy as np
model = SentenceTransformer('all-MiniLM-L6-v2')

def compare(request, sentences1, sentences2):
	#Compute embedding for both lists
	embeddings1 = model.encode(sentences1, convert_to_tensor=True)
	embeddings2 = model.encode(sentences2, convert_to_tensor=True)

	#Compute cosine-similarities
	cosine_scores = util.cos_sim(embeddings1, embeddings2)
	cosine_scores1 = np.squeeze(cosine_scores) # making one dimensional list
	print(tf.shape(cosine_scores1))
	
	maxCosineValue = tf.argmax(cosine_scores1, axis=None, name=None) # highest cosine value index
	similarsentence = sentences2[maxCosineValue] # most similar sentence amongst
	print('max', similarsentence)

	#Output the pairs with their score
	for i in range(len(sentences2)):
	    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[0], sentences2[i], cosine_scores[0][i]))
	return  {'similarSentence':similarsentence}
