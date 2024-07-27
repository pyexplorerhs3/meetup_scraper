from bs4 import BeautifulSoup

BASE_URL = "https://www.meetup.com/pygda-pl/events/?type=past"

def print_hi():
    find_handle = "./output.html"
    var_list = []
    example_string = "https://www.meetup.com/pygda-pl/events/"
    string_len = len("https://www.meetup.com/pygda-pl/events/298348089/")
    with open(find_handle) as html:
        soup = BeautifulSoup(html, "html.parser")
        my_var = soup.findAll("a", {'href': True})
        for i in my_var:
            temp = i.attrs["href"]
            if example_string in temp and len(temp) == string_len:
                var_list.append(temp)
    for el in var_list:
        print(el)

if __name__ == '__main__':
    print_hi()
