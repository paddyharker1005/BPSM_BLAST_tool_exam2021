#!/usr/local/bin/python3

import os, sys, subprocess, re, numpy as np


##function for building a BLAST database
def build_database(file, dbtype):
	try:
		build_command = "makeblastdb -in {} -dbtype {} -out query_database".format(file, dbtype)
		subprocess.check_output(build_command, shell=True)
	except subprocess.CalledProcessError:
		print("Error with provided database file. Please check that it is the required format. Exiting programme")
		sys.exit()


#ask the user for a fasta file to build a BLASTable database
while True:
	database_file = input("Please specify a fasta file to build BLAST database from.\n\n\t>")
	if os.path.exists(database_file):
		print("Database file found.")
		break
	else:
		print("Database file '{}' doesn't exist. Please try again.".format(database_file))
		continue

#ask the user what type of database they would like to build
while True:
	database_type = input("Which type of database would you like to build? (nucl/prot)\n\n\t>")
	if database_type in ('nucl', 'prot'):
		print("Building {} database...".format(database_type))
		break
	else:
		print("Database type '{}' doesn't exist. Please try again.".format(database_type))
		continue


#call build_database function
build_database(database_file, database_type)
print("Done.")

##function for performing BLAST analysis
def blast_analysis(file, database, flavour):
	try:
		blast_command = "{} -db {} -query {} > blastoutput_standard.out".format(flavour, database, file)
		blast_command2 = "{} -db {} -query {} -outfmt 7 > blastoutput_tabular.out".format(flavour, database, file)
		subprocess.check_output(blast_command, shell=True)
		subprocess.check_output(blast_command2, shell=True)
	except subprocess.CalledProcessError:
		print("Error ocurred when performing BLAST analysis. Please check that your query file is of the required type. Exiting programme.")
		sys.exit()

#determine which blast tools the user can use based on the type of database created
if database_type == 'nucl':
	blast_flavours = ['blastn', 'tblastn']
elif database_type == 'prot':
	blast_flavours = ['blastx', 'blastp']

#ask the user which blast tool they would like to user from those available
while True:
	print("Available blast analyses based on database type:\n\t")
	count = 0
	for flavour in blast_flavours:
		count += 1
		print("({})".format(count), flavour)
	blast_option = input("Which type of blast analysis would you like to perform?\n\n\t>")
	if blast_option in blast_flavours:
		print("{} analysis selected.".format(blast_option))
		break
	else:
		print("Incorrect input. Please try again")
		continue
#ask the user for a query file containing fasta sequence(s) to search database for
while True:
	query_file = input("Please specify a query file to search against BLAST database.\n\n\t>")
	if os.path.exists(database_file):
		print("Query file found.")
		break
	else:
		print("Query file '{}' doesn't exist. Please try again.".format(query_file))
		continue

print("Performing BLAST search...")
#call blast_analysis function
blast_analysis(query_file, "query_database", blast_option)
print("Done.")

##function for extracting the top 10 HSPs from the BLAST analysis
def top_hits(tab_file):
	with open(tab_file, 'r') as blasttab:
		line_number = 0
		print("Top ten HSPs:\n\n")
		for line in blasttab:
			if line.startswith("# Query: "):
				line_number = 0
				sequence = line.split("# Query: ")[1]
				print("Query sequence: ", sequence)
				print("Sequence:\tquery acc.ver\tsubject acc.ver\tpercent identity\talignment length\tmismatches\tgap opens\tq. start\tq. end\ts. start\ts. end\tevalue\tbit score")
			if line.startswith("#"):
				continue
			line_number += 1
			if line_number <= 10:
				print(line_number,"\t", line)

#ask the user if they want to show the top 10 HSPs - if so, call the top_hits function
while True:
	show_hits = input("Would you like to view the ten highest HSPs?(y/n)\n\n\t>")
	if show_hits == 'y':
		top_hits("blastoutput_tabular.out")
		break
	elif show_hits == 'n':
		break
	else:
		print("Wrong input! Please try again.")
		continue

print("Analysis complete.")







