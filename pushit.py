#!/usr/bin/env python3
'''
   Date: September 21, 2021
   From: Mark Mollere, mmollere@alta3.com
Subject: pushit.py
     To: You

push_it.py is a simple process to knock out a "git push" to GitHub. This code is
imperfect. The intent is for you to gaze upon the building blocks and engage in
critcal thinking for the next iteration...
'''
# Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt        # C-style parser for command line options.
import git           # Library used to interact with git repositories.
import os            # Operating system dependent functionality.
import sys           # System-specific parameters and functions.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def scan_for_arguments(git_comment):
  argumentList = sys.argv[1:]
  options      = "c:hmsv"
  long_options = ["comment","help","man-page","symbolic-link","version"]
  version      = '1.7'
  try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
      if currentArgument in ("-c", "--comment"):
        return currentValue
      elif currentArgument in ("-h", "--help"):
        print ("WIP: Help me...")
      elif currentArgument in ("-m", "--man-page"):
        print ("WIP: Install " + os.path.basename(sys.argv[0]) + " man page.")
      elif currentArgument in ("-s", "--symbolic-link"):
        print ("WIP: Symbolic link...")
      elif currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    print("Error 101")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def run_the_4_commands(git_comment):
  if len(sys.argv) == 1 or git_comment:
    if bool(git_comment):
      commit_message    = git_comment
    else:
      commit_message    = input('Commit Comment: ')
    repo=git.Repo('/home/student/mycode')
    repo.git.add('*')
    repo.git.commit(m=commit_message)
    repo.git.push()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
  run_the_4_commands(scan_for_arguments(""))
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
