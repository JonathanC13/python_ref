
class Arabic_to_roman:
    def numerals():
        #scan for arabic numeral for console arg or textfile
        # do conversion to roman
        String s_roman = "";
        while (ar_num >= 1000):
            ar_num -= 1000;
            s_roman += "M";
        while (ar_num >= 900):
            ar_num -= 900:
            s_roman += "CM";
        while (ar_num >= 500):
            ar_num -= 500;
            s_roman += 'D';
