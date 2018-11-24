from address_searcher import AdressSearcher


def main():
    # ユーザーからの郵便番号を受け取る
    # 郵便番号を使って地名をとってくる
    # 地名をプリントする
    user_postal_code = input("郵便番号を入力してください> ")
    user = AdressSearcher()
    print(user.search(user_postal_code))


if __name__ == '__main__':
    main()
