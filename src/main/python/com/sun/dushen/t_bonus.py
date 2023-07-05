from concurrent import futures

from com.sun.dushen.model.lottery import similarity


def main():
    # TODO
    # count = [8749216, 18080715]
    count = [8484692, 18077073]
    with futures.ProcessPoolExecutor(len(count)) as executor:
        fs = []
        for i in range(0, len(count)):
            f = executor.submit(similarity.run, count[i])
            fs.append(f)

        for f in futures.as_completed(fs):
            f.result()


if __name__ == '__main__':
    main()
