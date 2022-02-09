import numpy as np
import matplotlib.pyplot as plt


def exo1():
    foo = np.random.randint(0, 10, (np.random.randint(50, 60), np.random.randint(42, 69)))
    print(len(foo))
    print(len(foo[0]))
    print(foo.size)
    print(foo.shape)
    print(foo.dtype)
    bar = foo.astype(float)
    print(bar)
    print(foo > 8)
    print(np.where(foo < 5, foo, 2 * foo))
    return True


def exo2():
    short_sides = np.random.randint(1, 10, (200, 2))
    hypo = pow(pow(short_sides[:, 0], 2) + pow(short_sides[:, 1], 2), .5)
    print(hypo)
    triangles = np.column_stack((short_sides[:, 0], short_sides[:, 1], hypo))
    print(triangles)
    return True


def coquilles():
    # data = np.loadtxt("coquilles.txt")
    # datanp = np.save("coquilles.npy", data)
    data = np.load("coquilles.npy")

    def plot():
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(data[np.where(data[:, 0] == 42), 1], data[np.where(data[:, 0] == 42), 2],
                   data[np.where(data[:, 0] == 42), 3])
        ax.set_xlabel("time")
        ax.set_ylabel("latitude")
        ax.set_zlabel("longitude")
        plt.show()

    # plot()

    def stade5():
        a = data[:, 4] == 5  # stage 5
        b = data[:, 1] < 61  # avant le 60e temps
        print(a*b)  # a AND b
        print(data[np.where(a*b), 0])  # résultat

    # stade5()

    # print(data[np.where(data[:, 1] == 0), 2:4])

    def switched():
        stg = data[:, 4]
        a = stg == 5
        diff = np.roll(stg, -1) - stg
        b = (diff == -4)
        print(np.argsort(data[np.where(b), 1]))

    switched()
    return True


if __name__ == "__main__":
    # exo1()
    # exo2()
    coquilles()
