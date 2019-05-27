import os
import almetro
from almetro.instance import generator

def load_bottles(_file, bottles):
    with open(_file) as instance_file:
        num_bits, num_instances = instance_file.readline().replace("\n", "").split(" ")
        for instance in instance_file.readlines():
            number = instance.replace("\n", "")
            kwargs = {
                "max_height": int(num_bits),
                "break_point": number
            }
            size = {
                "n": num_bits
            }
            if bottles != "ilimitado":
                size['k'] = bottles
                kwargs["test_bottles"] = bottles
            yield {
                'name': f'{num_bits} ({bottles})',
                'size': size,
                'value': kwargs
            }

def generate_bottles_instances(instance_dir, bottles, size=10):
    i = 0
    for _file in sorted(os.listdir(instance_dir)):

        for instance in load_bottles(f'{instance_dir}/{_file}', bottles):
            i += 1
            yield instance
            if i == size:
                break
        if i == size:
            break

def almetro_bottles(trials=5, instances=10, complexity=None, instance_path=None, bottles_function=None, bottles="ilimitado"):
    instance_generator = generate_bottles_instances(instance_path, bottles, instances)    

    return almetro\
        .new()\
        .with_execution(trials=trials, runs=1)\
        .with_instances(instances=instances, provider=generator(instance_generator))\
        .metro(algorithm=bottles_function, complexity=complexity)