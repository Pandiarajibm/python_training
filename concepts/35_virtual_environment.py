"""
Virtual Environment:
"""

"""
If we are working on multiple projects
then
instead of using same python-installation for
all project,
We can create separate  copy of python-installation for each project

Creating copy of python-installation is called VIRTUAL ENVIRONMENTS 

# for shared system, admin will give one copy of python-intallation to employee1, another separate copy of 
python-installation to employee2 and so on. so the impact one project work will not affect other employee's project 
with the help of virtual environment.we are not installing python for each employee or each project. it is just a copy with minimal files and no libraries 
so that user can add or make code changes private to that environments. if all employee given same copy and if one 
employee corrupt the file, it will affect other employee projects.

if i am working in multiple projects,i can create a virtual environment for each project. so it will not impact among 
project i can have libraries only specific to that project in the virtual environment. i will have minimal things.
virtual environment will have minimal files.lib folder will be empty. standard libraries will not be there in that 
virtual environment. still it will make use of base python. whatever libraries installed in one virtual environment
will not impact the other environment. user can add libraries which is needed. different version of libraries. if all 
code changes are in same python installation it will be messup and problem. we cannot have same libraries of 
different version on same python installation. so use virtual environments.
"""

"""
How to create separate copy of python-installation
OR
other way to say
How to create virtual environment
"""

"""
2 ways to create virtual environments
1-way: through terminal/command-prompt
    python -m venv myvenv1
    python -m venv myvenv2
    python -m venv myvenv3
    python -m venv myvenv4

2-way through Few IDEs like pycharm, VS Code
    In pycharm,
    File -> Settings -> project: python_training -> python interpreter -> add interpreter

"""

"""
Create 2 virtual environments
my_virtual_environment_1
my_virtual_environment_2
and use
my_virtual_environment_1 for tomorrow training
"""
"""
my virtual environment 1 , there will be no libraries

"""

# Example
# Go command program say c: python training folder.
#  C:\python_training> python -m venv myvenv1
#  C:\python_training> cd myvenv1
# C:\python_training\myvenv1> cd scripts
# (myvenv1) PS C:\python_training\concepts> activate or ./activate
 # we will go back to python training folder using cd ../..
# cd ..
# cd ..
#cd concepts
# (myvenv1) PS C:\python_training\concepts> python  1_how_to_provide_description_and_comments.py
# Hello
# (myvenv1) PS C:\python_training\concepts>







