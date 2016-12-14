import configparser
import sys

config = configparser.RawConfigParser()
config.optionxform = str  # To preserve case

config.read(sys.argv[1])


# Make the gadget file
for section in config.sections():
    for item in config[section]:
        if not section in ['Gas', 'Stars']:
            print("{} {}".format(item, config[section][item]))
