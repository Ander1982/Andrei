from jinja2 import Environment, FileSystemLoader

name = ['Руслан', 'Ульяна', 'Сергей', 'Влада']

file_loder = FileSystemLoader('DZ_40')
env = Environment(loader=file_loder)

tm = env.get_template('main.html')
msg = tm.render(rab=name, title='Домашнее задание', title_2='Ученики', total='Домашнее задание выполнено!!!')
print(msg)