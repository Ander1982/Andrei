from DZ_32_def import Info


def main():
    for i in range(1, 10):
        start = Info(f"https://www.say7.info/cook/kitchen/38-Salatyi/linkz_start-{i * 20}.html", 'say_7.txt')
        start.run()


if __name__ == "__main__":
    main()
