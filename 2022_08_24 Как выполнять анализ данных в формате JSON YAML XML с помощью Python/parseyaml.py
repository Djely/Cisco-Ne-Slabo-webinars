import json
import yaml

with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

print(ouryaml)

print("The access tocen is {}".format(ouryaml['acess_tocken']))
print("The  tocen expires is {}".format(ouryaml['expires_in']))

print("\n\n---")
print(json.dumps(ouryaml, indent=4))

