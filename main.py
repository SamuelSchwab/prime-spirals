import argparse
import matplotlib.pyplot as plt
import numpy as np


def prime(n):
    """Returns a list of primes < n"""
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n-i*i-1) // (2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def polar_plot(
        n: int,
        size: float,
        dpi: int,
        name: str,
        show_numbers: bool,
        show_grid: bool
        ):
    """Plots (x,x) in polar coordinates, where x are primes and positive integers"""
    plt.style.use("dark_background")
    plt.rcParams["figure.dpi"] = dpi

    integers = np.arange(0,n)
    primes = prime(n)
    fig, ax = plt.subplots(1, 2, subplot_kw={"projection": "polar"})
    ax[0].scatter(integers, integers, s=size, marker=",", linewidths=0)
    ax[0].set_title("integers")
    ax[1].scatter(primes, primes, s=size, marker=",", linewidths=0)
    ax[1].set_title("primes")
    plt.setp(ax, xlim=(0, np.pi*2), ylim=(0, n))
    plt.setp(ax, xticks=[], yticks=[])
    if show_grid:
        ax[1].set_xticks((0, np.pi))
        ax[1].xaxis.grid(linewidth=0.1)
    if show_numbers:
        for x in integers:
            ax[0].annotate(
                str(x),
                (x, x),
                color="white", 
                fontsize=2,
                xytext=(0.8, 0.8),
                textcoords="offset points"
                )
        for x in primes:
            ax[1].annotate(
                str(x),
                (x, x),
                color="white",
                fontsize=2,
                xytext=(0.8, 0.8),
                textcoords="offset points"
                )
    fig.tight_layout()
    fig.savefig(name)
    plt.close


def parse_args():
    parser=argparse.ArgumentParser(
        description="Plots integers and primes < n in polar coordinates",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    parser.add_argument("-n", type=int, default=1000, help="Generate n numbers to plot")
    parser.add_argument("-s", type=float, default=1, help="Point size")
    parser.add_argument("-dpi", type=int, default=300, help="DPI of plot")
    parser.add_argument("-o", type=str, default="plot.png", help="Name/path of plot file")
    parser.add_argument("--show_numbers", action="store_true", help="Show numbers near points")
    parser.add_argument("--show_grid", action="store_true", help="Show the 0-180 degrees grid line for prime plot")
    args=parser.parse_args()
    return args


def main():
    args = parse_args()
    polar_plot(
        n=args.n,
        size=args.s,
        dpi=args.dpi,
        name=args.o,
        show_numbers=args.show_numbers,
        show_grid=args.show_grid
        )


if __name__ == "__main__":
    main()