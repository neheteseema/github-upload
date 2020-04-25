#!/usr/bin/env python
# Implementation of collaborative filtering recommendation engine
 
from recommendation_data1 import dataset
from math import sqrt
 
def similarity_score(person1,person2):


	# Returns ratio Euclidean distance score of person1 and person2 
 
	both_viewed = {}		# To get both rated items by person1 and person2
	for item in dataset[person1]:
		if item in dataset[person2]:
			#print("common items between"+person1+" and "+person2+"are"+item)
			both_viewed[item] = 1
	no = len(both_viewed)
	#print("total no of common items in "+person1 +" and "+person2+ " are")
	#print(no)
			# Conditions to check they both have an common rating items	
	if no == 0:
		return 0
 
		# Finding Euclidean distance 
	sum_of_eclidean_distance = 0
	a=0
 
	for item in dataset[person1]:
		if item in dataset[person2]:
			a=pow(dataset[person1][item] - dataset[person2][item],2)
			#sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item],2) for item in both_viewed)
		sum_of_eclidean_distance = sum_of_eclidean_distance + a
 
	return 1/(1+sqrt(sum_of_eclidean_distance))		
def most_similar_users(person,number_of_users):
	# returns the number_of_users (similar persons) for a given specific person.
	scores = [(similarity_score(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	print(scores)
	# Sort the similar persons so that highest scores person will appear at the first
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]
for person in dataset:
	print(" similar users for given user  "+person) 
	print (most_similar_users(person,3))
	print("----")


#b=similarity_score('Elizabeth Fonzino','Amanda')

#a=similarity_score('Enjolras','Amanda')
#a=similarity_score('Gene Zafrin','H. Schneider')
#a=similarity_score('Eric Anderson','H. Schneider')
#print(b)
def user_reommendations(person):
 
	# Gets recommendations for a person by using a weighted average of every other user's rankings
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in dataset:
		# don't compare me to myself
		if other == person:
			continue
		sim = similarity_score(person,other)
 
		# ignore scores of zero or lower
		if sim <=0: 
			continue
		for item in dataset[other]:
 
			# only score movies i haven't seen yet
			if item not in dataset[person] or dataset[person][item] == 0:
 
			# Similrity * score
				totals.setdefault(item,0)
				totals[item] += dataset[other][item]* sim
				# sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+= sim
 
		# Create the normalized list
 
	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	# returns the recommended items
	recommendataions_list = [recommend_item for score,recommend_item in rankings]
	return recommendataions_list
print("************Recommendation for all users************")
for person in dataset: 
	print (" Recommendations for user "+person)
	print (user_reommendations(person))