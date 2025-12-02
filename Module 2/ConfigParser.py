#####################
### Read INI file ###
#####################
import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\shanzlla\.spyder-py3\spyder.ini")
config.sections()
[option for option in config['help']]

##########################
### Create Dictionaru ###
#########################
parser = configparser.ConfigParser()
parser.read_dict(
    {'section1':
        {'tag1': '1','tag2': '2','tag3': '3'},
    'section2':
        {'tagA': 'A','tagB': 'B','tagC': 'C'},
    'section3':
        {'foo': 'x','bar': 'y','baz': 'z'} })
parser.sections()  #['section1', 'section2', 'section3']
[option for option in parser['section1']] # ['foo', 'bar', 'baz']

##############################
### Read Text/String file ###
#############################
sample_config = """
[My Settings]
user = username
profile = /my/directory/to/profile.png
gender = male
[My new Settings]
user = hanzllasoomro
profile = /my/directory/to/profile.png
gender = female
"""
# creates an instance of ConfigParser called config
config = configparser.ConfigParser()

#read the instance of string using read_string() method
config.read_string(sample_config)

config.sections()  #['My Settings']
user = config["My new Settings"]["user"]  #'username'
user
