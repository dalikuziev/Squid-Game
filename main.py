print("""Squid Game o'yiniga xush kelibsiz!
O'yin qoidasini tushuntiradigan bo'lsam, sizga bir marta imkon beriladi!
Bu o'yinda jami 5ta savol bor, oxiriga yetib borsangiz sizga $5 mlrd beriladi, oxiriga yetib borolmasangiz o'lasiz!""")
play = input("O'yinni boshlaysizmi? yes/no: ")
if play == "yes":
  question1 = input("1-savol. 26 + 79 = ?\nA)115 B)105 C)95\nanswer: ").upper()
  if question1 == "B":
    print("to'g'ri topdingiz davom eting")
    question2 = input("2-savol. 94 - 58 = ?\nA)42 B)38 C)36\nanswer: ").upper()
    if question2 == "C":
      print("to'g'ri topdingiz davom eting")
      question3 = input("3-savol. 23 * 15 = ?\nA)405 B)345 C)375\nanswer: ").upper()
      if question3 == "C":
        print("to'g'ri topdingiz davom eting")
        question4 = input("4-savol. 96 / 30 = ?\nA)3 B)3.2 C)3.6\nanswer: ").upper()
        if question4 == "B":
          print("to'g'ri topdingiz davom eting")
          question5 = input("5-savol. 88 % 7 = ?\nA)4 B)12 C)18\nanswer: ").upper()
          if question5 == "A":
            print("to'g'ri topdingiz va siz $5 mlrd yutib oldingiz, karta raqamingizni yuboring!")
            card = input("card number: ")
            print("$5 mlrd kartangizga muvoffaqqiyatli o'tkazildi")
          else:
            print("Siz o'ldingiz!")
        else:
          print("Siz o'ldingiz!")
      else:
        print("Siz o'ldingiz!")
    else:
      print("Siz o'ldingiz!")
  else:
    print("Siz o'ldingiz!")
else:
  print("afsus $5 mlrd dan quruq qoldingiz")
