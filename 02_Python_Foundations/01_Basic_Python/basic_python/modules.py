import math  #builtin module
print(math.sqrt(25))
import platform
print(platform.version())
import platform
peint("System:", platform.system())
print("Node:", platform.node())
print("Release:", platform.release())
print("Version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
# https://docs.python.org/3/py-modindex.html
# import ipartzixmodule
# ipartzixmodule.ipartzix()
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

