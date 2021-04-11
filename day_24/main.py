#!/usr/bin/env python
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


from jinja2 import Environment, FileSystemLoader

template_dir = 'Input/Letters'
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('starting_letter.txt')

with open('Input/Names/invited_names.txt') as all_names:
    names = all_names.readlines()
    for name in names:
        output_from_parsed_template = template.render(name=name.rstrip("\n"))
        output_file = "Output/ReadyToSend/" + name.rstrip("\n") + ".txt"
        print(output_file)
        with open(output_file, 'w') as output:
            output.write(output_from_parsed_template)
