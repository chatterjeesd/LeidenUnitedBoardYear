#!python
import math
import csv
import itertools
import time



print "##################################################################"
print"##   LEIDEN UNITED Group and Buddy Builder Algorithm            ##"
print"##                          version  1.1                        ##"
print"##                                                              ##"
print"##     @ Makes groups according to dinner days available        ##"
print"##     @ Suggest you group numbers, group size and combinations ##"
print"##     @ Suggests you member preferences to make buddies !!     ##"
print"##                                                              ##"                     
print"##                      Programmed by- Soumya Deep Chatterjee   ##"
print"##                                     Assessor Internal        ##"
print"##                                  Leiden United 2017-18       ##"                                                                                                                                     
print "##################################################################"
#print "PLEASE CURATE, ADD, MODIFY, EDIT YOUR EXCELSHEET (.csv) before running this program"
#print "Also make sure that there are no same or similar names. If present then put an identifier."
#print "For eg. Thomas Jefferson, Thomas Jefferson1"
# How many groups do you want to make?
numberofgroups=10
membersineachgroup=14
dinnerfile="dinners.txt"
buddyfile="buddies.txt"
#Write the preferred days of the groups
groups={
"Quintus":['monday', 'tuesday'],
"Catena":['monday', 'wednesday', 'thursday'],
"SSR":['thursday', 'monday', 'wednesday', 'friday'],
"Augustinus":['thursday', 'tuesday']
}


#If you have cancelled group(s), write down their group numbers
groupscancelled=['2', '10']

#File name of the excelsheet that you want to read from:
memadmin="test.csv"

# Write down  which column in the membership excelsheet
# refers to which column number. Write down only the column numbers 
# that you want to consider for group building. You might not want to 
# include email ids or phone numbers as group building criteria. So exclude them.
# PLEASE NOTE THAT IN PROGRAMMING, NUMBERS START FROM ZERO 
# AND NOT 1. So column zero in python is column 1 in excel sheet. and column 9 
# in python is column 10 in excel sheet. 
# PLEASE DO NOT CHANGE THE TOPIC NAME such as "name", "gender", 
# "nationality, dutchORinternational and groupleader as the program explicitly needs
#those values in the same way as written. For other preferences, you can add, edit or modify. 

preferences={
"name":'2',
"gender":'3',
"nationality":'6',
"dutchORinternational":'8',
"studysubject":'9',
"hobbies":'10',
"countriesvisit":'11',
"cuisines":'12',
"languages":'13',
"nationalitypreference":'14',
"donotpreferdinnerdays":'15',
"preferdinnerdays":'16',
"vegetarian":'17',
"dietaryrestrictions":'18',
"groupleader":'21',
"friendpreference":'22'
}

##########################----------PLEASE DO NOT CHANGE THE LINES BELOW------#######
gt=open(buddyfile, 'w')
gt.close()
rt=open(dinnerfile, 'w')
rt.close()
rtBAK=open(dinnerfile+"BAK", 'w')
rtBAK.close()


bigdata=[]
fm=open(dinnerfile, 'a')
fmbak=open(dinnerfile+"BAK", 'a')
masterlist=[]		
for grpnum in groups:
	list1=[]
	grpdaylist=groups[grpnum]
	for ty in grpdaylist:
		list1.append(str(grpnum)+str(ty))
	masterlist.append(list1)
masterlist= list(itertools.product(*masterlist))
big=open('bigdata.txt', 'w')
with open(memadmin, 'r') as fo:
	reader = csv.reader(fo, delimiter=',')
	for lines in reader:
		if "Timestamp" not in lines:
			bigdata.append(lines)
			big.write(str(lines)+"\n")
big.close()
#print "STEP1: Get the not-available dates from each participant and then assign pre-groups that means members can be in any of these groups."
#print " However these pre-groups may not be their preferred groups.",'\n'

		
for data in range(len(bigdata)):
	membername=bigdata[data][2].lower()
	nojoindates=bigdata[data][15].lower().replace(" ", "").split(',')
	
	#print "\n",membername, ":"
	fm.write(str(membername)+",")
	fmbak.write(str(membername)+",")
	for grpnum in groups:
		grpdaylist=groups[grpnum]
		#print membername, nojoindates, grpdaylist, set(nojoindates).intersection(grpdaylist), grpnum
		if len(set(nojoindates).intersection(grpdaylist))<len(grpdaylist):
			possibledates=list(set(grpdaylist).difference(set(nojoindates).intersection(grpdaylist)))
			for possibledateelement in possibledates:	
				fm.write(str(grpnum)+str(possibledateelement)+",")
				fmbak.write(str(grpnum)+str(possibledateelement)+",")
			#print "can join",  grpnum, "on", list(possibledates),"as person cannot join on", nojoindates,"and dinners are on", grpdaylist
		if len(set(nojoindates).intersection(grpdaylist))==len(grpdaylist):
			for possibledateelement in possibledates:
				fm.write(str(grpnum)+str('00')+",")
				fmbak.write(str(grpnum)+str('00')+",")
			#print "cannot join",  grpnum, "on any day as person cannot join on", nojoindates,"and dinners are on", grpdaylist
	fm.write("\n")
	fmbak.write("\n")
fm.close()
fmbak.close()


while True:
	time.sleep(1)
	counter=[]
	combi=[] #this list contains all possible combinations of groups based on days they can attend an association dinner. 
	membercombi=[] #this list contains all members in each possible combinations of groups based on days they can attend an association dinner. 
	candolist=[]
	lines0list=[]
	for grpcomb in masterlist:
		with open(dinnerfile, 'r') as fo:
			reader = csv.reader(fo, delimiter=',')
			for lines in reader:
		
				cando= list(set(grpcomb).intersection(lines))
				if cando not in combi:
					combi.append(cando)
				candolist.append(cando)
				lines0list.append(lines[0])
				#print cando, lines[0]
	
	for dfg in combi:
		dfglist=[]
		for index, fet in enumerate(candolist):
			if fet == dfg:
				if lines0list[index] not in dfglist:
					dfglist.append(lines0list[index])
		membercombi.append(dfglist)
	#print len(combi), len(candolist), len(lines0list), len(membercombi)


	refinedcombi=[]
	refinedmembercombi=[]
	membersineachcombi=[]
	allmemberscombi=[]

	for index, incomb in enumerate(combi):
		if len(groups)>=len(incomb)>len(groups)*2/3:
			refinedcombi.append(incomb)
			refinedmembercombi.append(membercombi[index])
			membersineachcombi.append(len(membercombi[index]))
			for allmembers in membercombi[index]:
				if allmembers not in allmemberscombi:
					allmemberscombi.append(allmembers)
			#print incomb, len(membercombi[index]), "members"
		
	for names in bigdata:
		if names[2].lower() not in allmemberscombi:
			continue
			#print "Groups could not be assigned to these persons because of dates they have chosen to be non-preferable:"
			#print"Please assign group manually for:",names[2]
			#if names[2].lower() not in counter:
				#counter.append(names[2].lower())
				
	###################################STEP 2###############
	#print "\n","STEP2: Now take the combination with the largest member base and get the number of unique members in other combinations"

	mem=open(buddyfile, "a")
	largest= max(membersineachcombi)
	templist=[]
	tempulist=[]
	for index, element in enumerate(membersineachcombi):
		if largest==element:
			if len(templist)==0:
				templist.append(index)
			elif len(templist)!=0:
				for av in templist:
					if len(set(refinedmembercombi[av])-set(refinedmembercombi[index])) !=0:
						templist.append(index)
			print "This combination",refinedcombi[index],"has ", element, "members"
			mem.write("This combination "+str(refinedcombi[index])+" has  "+str(element)+" members"+"\n")
			tempulist.append(index)
			for names in  refinedmembercombi[index]:
				if names not in counter:
					counter.append(names)

				
					
	for items in templist:
		#print "Now", refinedcombi[items], "is being compared to others"
		print "These are the members:", "\n"
		for indexy, elements in enumerate(refinedmembercombi):
			uniquemembers= list(set(elements)-set(refinedmembercombi[items]))
			#if len(uniquemembers) !=0:
				#print  refinedcombi[indexy], len(uniquemembers)
	
	print counter
	
	######## BUDDY BUILDING BLOCK------------

	
	
	#Create approximately equal sized groups:
	def partition(lst, n):
		increment = len(lst) / float(n)
		last = 0
		i = 1
		results = []
		while last < len(lst):
			idx = int(round(increment * i))
			results.append(lst[last:idx])
			last = idx
			i += 1
		return results
	numberofgroups=	len(counter)/membersineachgroup	
	remainder= len(counter)%membersineachgroup
	if remainder>2/3*membersineachgroup:
		finalnumberofgroups=numberofgroups+1
	elif remainder<2/3*membersineachgroup:
		finalnumberofgroups=numberofgroups
	groupcombination= [len(x) for x in partition(range(len(counter)), finalnumberofgroups)]
	#print numberofgroups, remainder, finalnumberofgroups
	print "\n", "For ", largest, "members:"
	mem.write("For "+str(largest)+" members"+"\n")
	for tyu in groupcombination:
		print "Make a group of:",tyu,"members."
		mem.write("Make a group of: "+str(tyu)+" members"+"\n")
	#print "\n", "###############################--MEMBER DETAILS AND PREFERENCES--#############"
	mem.write("###############################--MEMBER DETAILS AND PREFERENCES--#############"+"\n")
	mem.write("Name"+"\t")
	for tre in preferences:
		if 'name' not in tre:
			mem.write(str(tre)+"\t")
	mem.write("\n")
	
	genderlist=[]
	dutchORinternationallist=[]
	for counts in counter:
		bigg=open('bigdata.txt', 'r')
		for lines in bigg:
			if counts == str(eval(lines)[int(preferences['name'])]).lower():
				genderp= str(eval(lines)[int(preferences['gender'])]).lower()
				groupleaderp= str(eval(lines)[int(preferences['groupleader'])]).lower()
				dutchORinternationalp=str(eval(lines)[int(preferences['dutchORinternational'])]).lower()
				if genderp=='male':
					genderlist.append(1)
				if 'dutch' in dutchORinternationalp:
					dutchORinternationallist.append(1)
				#print counts, genderp, dutchORinternationalp, "GroupLeader", groupleaderp
				#print counts
				mem.write(str(counts)+"\t")
				for tre in preferences:
					if 'name' not in tre:
						#print tre,":", eval(lines)[int(preferences[tre])],",",
						mem.write(str(eval(lines)[int(preferences[tre])]+"\t"))
				#print "\n"
				mem.write("\n")
		bigg.close()
	

	
	print str(len(genderlist))," Male, ",str(len(counter)-len(genderlist))," Female, ",str(len(dutchORinternationallist))," Dutch, ",str(len(counter)-len(dutchORinternationallist))," International"
	print "IMPORTANT: DO  NOT FORGET TO CHECK ",dinnerfile, "and",buddyfile
	print dinnerfile, "contains members who could not be put to any groups"
	print buddyfile, "contains all the data that you need to make buddies and groups"
	print "-------------------------------------------------------------------------"
	mem.write(str(len(genderlist))+" Male, "+str(len(counter)-len(genderlist))+" Female, "+str(len(dutchORinternationallist))+" Dutch, "+str(len(counter)-len(dutchORinternationallist))+" International"+"\n\n")
	mem.close()	
		
		
		
		
		
	#--------Deleting the dinners.txt file
	lineap=[]
	fy= open(dinnerfile, 'r')
	dft=fy.readlines()
	for lines in dft:
		drt= lines.split(',')
		if drt[0] not in counter:
			lineap.append(lines)
	fy= open(dinnerfile, 'w')
	for aps in lineap:
		fy.write(str(aps))
	fy.close()	
	time.sleep(2)
