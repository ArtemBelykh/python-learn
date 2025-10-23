from helpers import slugify

def main():
    title = "Меня зовут Артём мне 23"
    print("Выход:", slugify(title))

if __name__ == "__main__":
    main()
