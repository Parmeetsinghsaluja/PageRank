# Task2
# Implementing Page Rank Algorithm

# Importing Collections Library to use functions like counter
import collections

# Importing Math Library to use functions like log,pow
import math

# Importing itemgetter Library to perform operations on dict
from operator import itemgetter

#Global Variables
temp_dict=dict()       #dict used to store temp rank value of a page
outlink_dict=dict()    #dict used to store outlinks of a page
inlink_list=list()     #list used to store the pages which are pointing to the current page
rank_dict=dict()       #dict used to store final rank values
d=0.85                 #given value of d
count=0                # used to calculate consecutive convergence


#Function for assgining default rank to pages.
def defaultpagerank(g):


	#Accessing global varaibles
	global rank_dict
	with open(g, 'r') as f:
		lines=f.readlines()

	#Calculate Number of Pages
	N=len(lines)

	#Assigning Default Values
	for line in lines:
		temp_dict ={line.split(" ")[0] : 1/N}
		rank_dict.update(temp_dict)

#Function for calculate no. of outlinks of pages.
def outlink_dicts(g):


	#Accessing global varaibles
	global outlink_dict
	with open(g, 'r') as f:
		lines=f.readlines()

	#Using Counter object to count no of outlinks
	c=collections.Counter()
	for line in lines:
		c.update(line.split())
	
	#Converting the counter object to dict 
	outlink_dict=dict(c)


#Function to find inlinks of pages.
def inlink_lists(s,g):
	with open(g, 'r') as f:
		lines=f.readlines()

	#Finding the inlinks of a page
	for line in lines:
		if s == line.split(" ")[0]:
			return line.split(" ")[1:(len (line.split(" "))-1)]
	
#Function to calculate pagerank
def pagerank(g):

	#Accessing global varaibles	
	global outlink_dict
	global rank_dict

 
 	#Default value of sinkpr should be 0(given)
	sinkpr=0

	#Making dict of old page rank values.
	temp_dict.update(rank_dict)
	
	#Calculating sinkpr
	for link in outlink_dict:
		if (outlink_dict.get(link,None) ==1):
			sinkpr=sinkpr+temp_dict.get(link,None)

	#Calculating new rank
	for link in rank_dict:
		rank_dict[link]= (1-d)/len(temp_dict)
		rank_dict[link]=rank_dict[link]+ d*sinkpr/len(temp_dict)
		inlink_list=inlink_lists(link,g)
		for a in inlink_list:
			if outlink_dict.get(a,None) - 1 > 0 :
				rank_dict[link]=rank_dict[link]+d*temp_dict.get(a,None)/((outlink_dict.get(a,None))-1)
			else :
				continue
		
	#Clearing the temporary dict.
	temp_dict.clear()

#Main_Function which call other functions till the pagerank gets converged.
def main():

	#Accessing global varaibles
	global count
	global rank_dict


	#Defining varaibale for entropy
	entropy=0

	#Defining varaibale for perplexity
	current_perplexity=0
	old_perplexity=0
	change_in_perplexity=0

	#Taking Input the Graph File Name
	g = input('Enter the Graph File Name with extension (.txt)- ')

	#Taking Input the Perplexity File Nmae
	pf= input('Enter the File Name in which you want to store Perplexities with extension(.txt)- ')

	#Defining the default Graph File Name
	if g=="1":
		g="G1.txt"
	if g=="2":
		g="G2.txt"

	#Defining the default Perplexity File Name
	if pf=="1":
		pf="Perplexity_G1.txt"
	if pf=="2":
		pf="Perplexity_G2.txt"


	#Calling the helper functions
	defaultpagerank(g)
	outlink_dicts(g)

	#Opening File in which records perplexity values
	f=open(pf,"w+")

	#Loop which runs until pagerank converges
	while count< 4:

		#Assigning 0 to entropy for every loop turn
		entropy=0


		#Calling pagearank function
		pagerank(g)


		#Updating Entropy Values
		for rank in rank_dict:
			entropy=entropy+(rank_dict.get(rank)*math.log(rank_dict.get(rank))/math.log(2))


		#Caluclating Current Perplexity
		current_perplexity=math.pow(2,-entropy)


        #Caluclating Change in Perplexity
		change_in_perplexity=current_perplexity-old_perplexity


		#Entering the data in the file.
		f.write("Perplexity is " +str(current_perplexity)+ "\n")


        #Checking if page rank converges or not
		if(abs(change_in_perplexity)<1):
			count=count+1
		else:
			count=0
		old_perplexity=current_perplexity


	#Closing the File
	f.close()


    #Displaying the output.
	print(sorted(rank_dict.items(),key=itemgetter(1), reverse= True))




#Calling the main function of program
main()

	




