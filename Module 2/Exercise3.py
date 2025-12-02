#  • Your team has just finished up creating a software product for a marketing
#  company. The software reports summary statistics for data plugged in.
#  • You are required to create a configuration file that takes the following infor
#  mation for the software to pick up and use
#  • root directory
#  • Username
#  • numberof databases connected.
#  • summary unit [percent or absolute values]
#  • Create your own default values. Save your file as configuration.txt. Use the
#  appropriate library.

import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Add a section and some default settings
config['DEFAULT'] = {
    'RootDirectory': '/home/user/project',
    'Username': 'hanzllasoomro',
    'NumberOfDatabases': '3',
    'SummaryUnit': 'percent'
}

# Write to a file
with open('configuration.txt', 'w') as configfile:
    config.write(configfile)

print("Configuration file created successfully.")

# read the file
config.read("configuration.txt")

# Access the values
root_Directory = config['DEFAULT']['RootDirectory']
Username = config['DEFAULT']['Username']
NumberOfDatabases = int(config['DEFAULT']['NumberOfDatabases'])
summary_Unit = config['DEFAULT']['SummaryUnit']

print("Root Dictionary",root_Directory)
print("Username",Username)
print("NumberOfDatabases",NumberOfDatabases)
print("SummaryUnit",summary_Unit)
