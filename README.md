Парсинг днс конфига (Parser.py) и пинг записей типа A, с записью удачно и неудачно пропингованных адресов (pingpong.py).
Изначальный файл днс содержал дубликаты, поэтому файл, полученный после parser.py лучше обработать стандартными средствами линукса:
python parser.py [FILENAME]

sort [FILENAME] | uniq > [FILENAME2]

python pingpong.py [FILENAME]
