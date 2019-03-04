
class UnionFind:
    def __init__(self, n):
        # 親の番号を格納する。親だった場合は-(その集合のサイズ)
        self.parent = [-1] * n

    # a がどのグループに属しているか調べる。
    def root(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.root(self.parent[a])
        return self.parent[a]

    # 自分のいるグループの頂点数を調べる。
    def size(self, a):
        # 親を見つけて、親の - (その集合のサイズ)
        return -1 * self.parent[self.root(a)]

    # aとbを繋ぐ。
    def connect(self, a, b):
        # a と b を直接つなぐのではなく、a の親と b の親を繋げるので、
        # 各 a b の親を取得する。
        a = self.root(a)
        b = self.root(b)

        if a == b:
            # 既に繋がっている場合は、処理を行わない。
            return

        if self.size(a) < self.size(b):
            # a よりも b のサイズが大きい場合、２つの値を入れ替える。
            b, a = a, b

        # サイズの大きい a のサイズを更新する。
        self.parent[a] += self.parent[a]
        # b の親を a に変更する。
        self.parent[b] = a


if __name__ == '__main__':
    # ABC120 D

    # 入力を変数へ代入
    n, m = map(int, input().split())
    a, b = {}, {}
    for i in range(m):
        a[i], b[i] = [int(n) - 1 for n in input().split()]

    # 最後の不便さは、全ての繋がりが無くなるので、mC2で求められる。
    ans = {m - 1: n * (n - 1) / 2}

    Uni = UnionFind(n)

    # 繋がりが1のパターン(0は上で計算した)から遡って計算する。
    for i in range(m - 1, 0, -1):

        if Uni.root(a[i]) != Uni.root(b[i]):
            # a と b が同じグループでない場合、繋がりが増えるので、不便さを減らす
            ans[i - 1] = ans[i] - Uni.size(a[i]) * Uni.size(b[i])
            Uni.connect(a[i], b[i])
        else:
            # 同じグループだった場合、結果は変わらないので同値を代入する。
            ans[i - 1] = ans[i]

    # 答えの描画
    for i in range(m):
        print(int(ans[i]))

