from configparser import ConfigParser

config = ConfigParser()
config.read("configuaration.ini")
config.add_section('bank')
config.set('bank', 'name','hsbc')
config.set('bank', 'code','2345')

print(config.sections())
print(list(config['bank']))