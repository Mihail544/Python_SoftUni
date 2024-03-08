squares = [x**2 for x in range(10) if x != 2]
print(squares)


my_list = ["Gosho e gotin", "Mi6o e po gotin", "Nema nikoi jiv"]



# Първото words е нещото което ще остане в спъсъкът или с други думи нещо като my_list[] = my_new_list[]
# После се чете for words като това новото е нещото което ще заема памета на думите през които ще преминем.
# return е всичко на което условието му съвпада и то става част от първото words и заема информацията на новият лист


my_list = [words for words in my_list if "Mi6o" in words]
print(my_list)