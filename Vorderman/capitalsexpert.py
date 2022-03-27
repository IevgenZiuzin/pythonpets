from tkinter import Tk, simpledialog, messagebox
print('Capitals Expert')
root = Tk()
root.withdraw()
the_world = {}

def read_from_file():
    country_list = []
    with open('capitals_la.txt', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
            #country_list.append(city)
    #return country_list
#print(read_from_file())
            
def write_to_file(country_name, city_name):
    with open('capitals_la.txt', 'a', encoding='utf-8') as file:
        file.write('\n' + country_name + '/' + city_name)

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type name of country')
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', query_country + \
                            ' - ' + result + '!')      
    else:
        new_city = simpledialog.askstring('Don\'t know. Teach me', 'What is the capital of '\
                                          + query_country + '!')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

#добавлять отсутсвующую столицу для существующей страны
        
