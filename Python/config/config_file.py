from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

print(config.sections())
print(list(config['account']))

config.add_section('bank')
config.set('bank', 'name','hsbc')
config.set('bank', 'code','2345')

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print(list(config['bank']))