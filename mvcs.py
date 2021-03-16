#!/usr/bin/env python3

import argparse
import os
import shutil
from distutils.dir_util import copy_tree

parser = argparse.ArgumentParser()
parser.add_argument(dest="command", help="""COMMANDS\n-init [folder] => initiliazes folder.\n-checkout [branch-name] => if branch exists it will point at it, else it will create it.\n-commit [message] => commits the project folder in the branch it's pointing to.\n-revert [commit-id] => it will revert the project to the state of the selected commit from the branch it's pointing at.\n-log [OPTIONAL-branch] => it will log all of the branches and their commits, if a branch is specified it will log all of its commits and messages.""")
parser.add_argument(dest="argument", nargs="?")

def main():
	args = parser.parse_args()
	
	if args.command == "init":
		init(args)
	elif args.command == "checkout":
		checkout(args)
	elif args.command == "commit":
		commit(args)
	elif args.command == "revert":
		revert(args)
	elif args.command == "log":
		log(args)

def init(args):
	if args.argument != None:
		try:
			os.mkdir("./.mvcs")

			f = open("./.mvcs/NAME", "w")
			f.write(args.argument)
			f.close()

			os.mkdir("./.mvcs/master")

			f = open("./.mvcs/master/COMMITS", "w")
			f.write("0")
			f.close()

			f = open("./.mvcs/POINTER", "w")
			f.write("master")
			f.close()

			f = open("./.mvcs/BRANCHES", "a")
			f.write("master\n")
			f.close()

			print("The folder was successfully initialized as an mvcs repository.")
		except:
			print("The folder is already initialized as an mvcs repository.")
	else:
		print("No folder was specified.")

def checkout(args):
	try:
		branch = args.argument

		path = "./.mvcs/" + branch

		if os.path.isdir(path):
			f = open("./.mvcs/POINTER", "w")
			f.write(branch)
			f.close()

			print("Now pointing to " + branch + " branch.")
		else:
			os.mkdir("./.mvcs/" + branch)

			f = open("./.mvcs/" + branch + "/COMMITS", "w")
			f.write("0")
			f.close()

			f = open("./.mvcs/BRANCHES", "a")
			f.write(branch + "\n")
			f.close()

			f = open("./.mvcs/POINTER", "w")
			f.write(branch)
			f.close()

			print("Created missing " + branch + " branch and pointing at it.")
	except Exception as e:
		print("An error occurred while trying to checkout: " + str(e))

def commit(args):
	try:
		f = open("./.mvcs/POINTER", "r")
		branch = f.readline()
		f.close()

		f = open("./.mvcs/" + branch + "/COMMITS", "r")
		commit = f.readline()
		f.close()

		path = "./.mvcs/" + branch + "/" + commit

		os.mkdir(path)

		f = open("./.mvcs/NAME", "r")
		name = f.readline()
		f.close()

		copy_tree("./" + name, path + "/" + name)

		message = args.argument

		f = open("./.mvcs/" + branch + "/" + commit + "/MESSAGE", "w")
		f.write(message)
		f.close()

		nextCommit = int(commit) + 1

		f = open("./.mvcs/" + branch + "/COMMITS", "w")
		f.write(str(nextCommit))
		f.close()

		print("The project was successfully committed to " + branch + " branch.")
	except Exception as e:
		print("An error occurred while trying to commit the project: " + str(e))

def revert(args):
	try:
		f = open("./.mvcs/POINTER", "r")
		branch = f.readline()
		f.close()

		f = open("./.mvcs/NAME", "r")
		name = f.readline()
		f.close()

		commit = args.argument

		path = "./.mvcs/" + branch + "/" + commit + "/" + name

		copy_tree(path, "./" + name)

		print("Successfully reverted the project to commit number: " + commit + " from " + branch + " branch.")
	except Exception as e:
		print("An error occurred while trying to revert the project: " + str(e))

def log(args):
	try:
		if args.argument == None:
			branches = get_branches()

			for branch in branches:
				path = "./.mvcs/" + branch

				f = open(path + "/COMMITS", "r")
				commits = f.readline()
				f.close()

				print("\nBRANCH: " + branch + " COMMITS: " + commits + "\n")
		else:
			branch = args.argument

			path = "./.mvcs/" + branch

			run = True

			commit = 0

			while run:
				path = "./.mvcs/" + branch + "/" + str(commit)

				if os.path.isdir(path):
					f = open(path + "/MESSAGE", "r")
					message = f.readline()
					f.close()

					print("\nCOMMIT ID: " + str(commit) + " MESSAGE: " + message + "\n")
					
					commit += 1
				else:
					run = False

	except Exception as e:
		print("An error occurred while trying to log: " + str(e))

def get_branches():
	branches_info = []

	f = open("./.mvcs/BRANCHES", "r")
	branches = f.readlines()
	f.close()

	for branch in branches:
		branches_info.append(branch.strip("\n"))

	return branches_info

main()