class INN:
    CHECK_10 = (2, 4, 10, 3, 5, 9, 4, 6, 8)

    @classmethod
    def is_valid(cls, inn):
        if len(inn) != 10 or not inn.isdigit():
            return False
        sum_num = 0
        for i in range(9):
            sum_num += int(inn[i]) * cls.CHECK_10[i]
        if (str(sum_num % 11))[-1] == inn[-1]:
            return True
        else:
            return False


class OGRN:
    @classmethod
    def is_valid(cls, ogrn):
        if len(ogrn) != 13 or not ogrn.isdigit():
            return False
        ogrn = int(ogrn)
        ogrn_12 = ogrn % 100
        if (str(ogrn_12 % 11))[-1] == str(ogrn)[-2]:
            return True
        else:
            return False
