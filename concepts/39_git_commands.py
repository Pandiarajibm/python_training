"""
Git Commands
"""

# ---------------
# PART-1: Make python_training folder as git repository in laptop
# ---------------
# - open command prompt
# - cd to python_training folder
# - then execute below command
#   git init
#
# Example:
#   C:\Users\mahad>cd C:\python_training
#   C:\python_training>git init
#
# NOW python_training folder is git repository
#############################

# ---------------
# PART-2: Add all files and folders to python_training git repository
# ---------------
#  command is
#   - C:\python_training>git add concepts programs
#   - C:\python_training>git commit -m "Adding all files and folders to git repository"
#############################


# ---------------
# PART-3: Create account and repository in github
# ---------------
#
# - Create account in: https://github.com/
# - Create new repository ''python_training"
#
#############################


# ---------------
# PART-4: Link python_training repository present in laptop with github repository
# ---------------
# We should link to our repository with python_training.git
# - cd to C:\python_training
# - C:\python_training>git remote add origin https://github.com/Pandiarajibm/python_training.git
# - C:\python_training>git remote add origin https://github.com/mahadevaprabhug/python_training_14.git

#############################

# ---------------
# PART-5: Send all files to git from laptop
# ---------------
#
# C:\python_training>git push -u origin master
#
#############################

# ---------------
# PART-6: pull trainer code
# ---------------
# 1. create empty directory 'trainer_code'
# 2. make trainer_code as git repository
#       git init
# 3. link
#   git remote add origin https://github.com/mahadevaprabhug/python_training_14.git
# 4. git pull origin master
#
#############################
#https://forms.office.com/r/6hZH3MdrHp - MCQ assessment
#########
#https://pypi.org/project/selenium/
#https://pypi.org/project/robotframework/
# 9986169696
# mahadevaprabhu.g@gmail.com
# Mahadeva Prabhu G
#########


###########
"""
…or create a new repository on the command line

echo "# python_training" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Pandiarajibm/python_training.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/Pandiarajibm/python_training.git
git branch -M main
git push -u origin main

##############
"""