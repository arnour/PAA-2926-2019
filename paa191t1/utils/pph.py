import os
import almetro
import random
from almetro.instance import generator
from paa191t1.pph import Pair


def clean_line(line):
    return line.rstrip('\n').rstrip(' ').lstrip(' ')


def but_zero(num):
    if num is None or num == 0:
        return random.randint(10, 400)
    return num


def load_pairs(file):

    with open(file, 'r') as pph:
        instance_size = int(clean_line(pph.readline()))
        is_a = True
        aas = []
        bbs = []
        for line in pph.readlines():
            nums = list(map(int, clean_line(line).split(' ')))
            if is_a:
                aas += nums
            else:
                bbs += nums
            is_a = is_a and len(nums) > 1
        pairs = [Pair(but_zero(aas[i]), but_zero(bbs[i])) for i in range(instance_size)]
        instance_name = file.split('/')[-1].replace('pph_', '').replace('.dat', '')
        return {
            'name': f'{instance_name} ({instance_size})',
            'size': {'n': instance_size},
            'value': {
                'n': pairs[1:],
                't0': pairs[0]
            }
        }


def generate_pph_instances(instance_dir, size=10):
    i = 0
    for file in sorted(os.listdir(instance_dir)):
        i += 1
        yield load_pairs(f'{instance_dir}/{file}')
        if i == size:
            break


def almetro_pph(trials=5, instances=10, algorithm=None, complexity=None, instance_path=None):
    instance_generator = generate_pph_instances(instance_path, instances)
    return almetro\
        .new()\
        .with_execution(trials=trials, runs=1)\
        .with_instances(instances=instances, provider=generator(instance_generator))\
        .metro(algorithm=algorithm, complexity=complexity)
