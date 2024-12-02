import configparser

## Reset Configuration ##
conf = configparser.ConfigParser()
conf.read('setting.conf', encoding='utf-8')
conf['coordinates']['first_x'], conf['coordinates']['first_y'],\
      conf['coordinates']['second_x'], conf['coordinates']['second_y'] = str('0'), str('0'), str('0'), str('0')
conf['flag']['first_time'] = str('True')

with open("setting.conf", "w") as file:
    conf.write(file)