import sys

import cudf

def main():
    fpath = sys.argv[1]
    df = cudf.read_csv(fpath, sep=' ', skiprows=7, names=['discard', 'src', 'dst', 'wt'])
    df['src'] -= 1
    df['dst'] -= 1

    df = df.sort_values("src")
    df.to_csv(sys.argv[2], sep=" ", columns=['src', 'dst', 'wt'], header=False, index=False)

    with open(sys.argv[2], "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(str(df["src"].nunique()) + " " + str(df.shape[0]) + '\n' + content)

if __name__ == "__main__":
    main()