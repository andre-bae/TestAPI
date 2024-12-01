from tkinter import *
from tkinter import ttk

dict_crypta_all = {
    "Bitcoin": "btc",
    "Ethereum": "eth",
    "Tether": "usdt",
    "Solana": "sol",
#    "Binance Coin": "bnb",
    "Ripple": "xrp",
    "Dogecoin": "doge",
    "Cardano": "ada",
#    "USDC": "usdc",
#    "EOS": "eos",
#    "Litecoin": "ltc",
#    "Stablecoin": "stable",
    "Stellar": "xlm"
}

dict_fiat_all = {
    "Дирхам ОАЭ": "AED",
    "Афганский афгани": "AFN",
    "Албанский лек": "ALL",
    "Армянский драм": "AMD",
    "Нидерландский антильский гульден": "ANG",
    "Ангольская кванза": "AOA",
    "Аргентинское песо": "ARS",
    "Австралийский доллар": "AUD",
    "Арубанский Флорин": "AWG",
    "Азербайджанский манат": "AZN",
    "Марка Боснии и Герцеговины": "BAM",
    "Барбадосский доллар": "BBD",
    "Бангладешская така": "BDT",
    "Болгарский лев": "BGN",
    "Бахрейнский динар": "BHD",
    "Бурундийский франк": "BIF",
    "Бермудский доллар": "BMD",
    "Брунейский доллар": "BND",
    "Боливийский боливиано": "BOB",
    "Бразильский реал": "BRL",
    "Багамский доллар": "BSD",
    "Бутанский Нгултрум": "BTN",
    "Ботсвана Пула": "BWP",
    "Белорусский рубль": "BYN",
    "Белизский доллар": "BZD",
    "Канадский доллар": "CAD",
    "Конголезский франк": "CDF",
    "Швейцарский франк": "CHF",
    "Чилийское песо": "CLP",
    "Китайский юань": "CNY",
    "Колумбийское песо": "COP",
    "Коста-риканский колон": "CRC",
    "Кубинское песо": "CUP",
    "Эскудо Кабо-Верде": "CVE",
    "Чешская крона": "CZK",
    "Франк Джибути": "DJF",
    "Датская крона": "DKK",
    "Доминиканское песо": "DOP",
    "Алжирский динар": "DZD",
    "Египетский фунт": "EGP",
    "Эритрейская накфа": "ERN",
    "Эфиопский быр": "ETB",
    "Евро": "EUR",
    "Доллар Фиджи": "FJD",
    "Фунт Фолклендских островов": "FKP",
    "Фарерская крона": "FOK",
    "Фунт стерлингов": "GBP",
    "Грузинский Лари": "GEL",
    "Фунт Гернси": "GGP",
    "Ганский седи": "GHS",
    "Гибралтарский фунт": "GIP",
    "Гамбийский даласи": "GMD",
    "Гвинейский франк": "GNF",
    "Гватемальский кетцаль": "GTQ",
    "Гайанский доллар": "GYD",
    "Гонконгский доллар": "HKD",
    "Гондурасская лемпира": "HNL",
    "Хорватская куна": "HRK",
    "Гаитянский гурд": "HTG",
    "Венгерский форинт": "HUF",
    "Индонезийская рупия": "IDR",
    "Новый израильский шекель": "ILS",
    "Мэнский фунт": "IMP",
    "Индийская рупия": "INR",
    "Иракский динар": "IQD",
    "Иранский риал": "IRR",
    "Исландская крона": "ISK",
    "Джерси Паунд": "JEP",
    "Ямайский доллар": "JMD",
    "Иорданский динар": "JOD",
    "Японская иена": "JPY",
    "Кенийский шиллинг": "KES",
    "Киргизский сом": "KGS",
    "Камбоджийский риель": "KHR",
    "Доллар Кирибати": "KID",
    "Коморский франк": "KMF",
    "Южнокорейская вона": "KRW",
    "Кувейтский динар": "KWD",
    "Доллар Каймановых островов": "KYD",
    "Казахстанский Тенге": "KZT",
    "Лаосский кип": "LAK",
    "Ливанский фунт": "LBP",
    "Шри-ланкийская рупия": "LKR",
    "Либерийский доллар": "LRD",
    "Лесото Лоти": "LSL",
    "Ливийский динар": "LYD",
    "Марокканский дирхам": "MAD",
    "Молдавский лей": "MDL",
    "Малагасийский ариари": "MGA",
    "Македонский денар": "MKD",
    "Бирманский кьят": "MMK",
    "Монгольский тогрог": "MNT",
    "Патака Макао": "MOP",
    "Мавританская угия": "MRU",
    "Маврикийская рупия": "MUR",
    "Мальдивская руфия": "MVR",
    "Малавийская квача": "MWK",
    "Мексиканское песо": "MXN",
    "Малазийский ринггит": "MYR",
    "Мозамбикский метикал": "MZN",
    "Намибийский доллар": "NAD",
    "Нигерийская найра": "NGN",
    "Никарагуанская Кордова": "NIO",
    "Норвежская крона": "NOK",
    "Непальская рупия": "NPR",
    "Новозеландский доллар": "NZD",
    "Оманский риал": "OMR",
    "Панамский бальбоа": "PAB",
    "Перуанский соль": "PEN",
    "Папуа-Новая Гвинея Кина": "PGK",
    "Филиппинское песо": "PHP",
    "Пакистанская рупия": "PKR",
    "Польский злотый": "PLN",
    "Парагвайский гуарани": "PYG",
    "Катарский риал": "QAR",
    "Румынский лей": "RON",
    "Сербский динар": "RSD",
    "Российский рубль": "RUB",
    "Руандийский франк": "RWF",
    "Саудовский риял": "SAR",
    "Доллар Соломоновых Островов": "SBD",
    "Сейшельская рупия": "SCR",
    "Суданский фунт": "SDG",
    "Шведская крона": "SEK",
    "Сингапурский доллар": "SGD",
    "Фунт острова Святой Елены": "SHP",
    "Сьерра-Леоне леоне": "SLE",
    "Сомалийский шиллинг": "SOS",
    "Суринамский доллар": "SRD",
    "Южносуданский фунт": "SSP",
    "Сан-Томе и Принсипи Добра": "STN",
    "Сирийский фунт": "SYP",
    "Эсватини Лилангени": "SZL",
    "Тайский бат": "THB",
    "Таджикский сомони": "TJS",
    "Туркменский манат": "TMT",
    "Тунисский динар": "TND",
    "Тонганский Паанга": "TOP",
    "Турецкая лира": "TRY",
    "Доллар Тринидада и Тобаго": "TTD",
    "Доллар Тувалу": "TVD",
    "Новый тайваньский доллар": "TWD",
    "Танзанийский шиллинг": "TZS",
    "Украинская гривна": "UAH",
    "Угандийский шиллинг": "UGX",
    "Доллар США": "USD",
    "Уругвайское песо": "UYU",
    "Узбекский сум": "UZS",
    "Венесуэльский Боливар Соберано": "VES",
    "Вьетнамский донг": "VND",
    "Вануату Вату": "VUV",
    "Самоанская тала": "WST",
    "Центральноафриканский франк КФА": "XAF",
    "Восточно-карибский доллар": "XCD",
    "Специальные права заимствования": "XDR",
    "Западноафриканский франк КФА": "XOF",
    "Франк КФП": "XPF",
    "Йеменский риал": "YER",
    "Южноафриканский рэнд": "ZAR",
    "Замбийская квача": "ZMW",
    "Зимбабвийский доллар": "ZWL"
}
list_fiat_all = list(dict_fiat_all)
list_crypta_all = list(dict_crypta_all)
list_fiat = []
list_crypta = []


# добавление нового элемента
def add_fiat():
    s = fiat_all_listbox.curselection()
    new_fiat = list_fiat_all[s[0]]
    if new_fiat not in list_fiat:
        list_fiat.append(new_fiat)
        fiat_var.set(list_fiat)
#        print(list_fiat)
#    print(selection, list1[selection[0]], dict1_all[list1[selection[0]]])
#    dict2[list1[selection[0]]] = dict1_all[list1[selection[0]]]
#    print(dict2)


# удаление выделенного элемента
def delete():
    s = fiat_listbox.curselection()
    if len(s) == 1:
        list_fiat.pop(s[0])
        fiat_var.set(list_fiat)


# очистка списка выбранных валют
def del_all():
    list_fiat.clear()
    fiat_var.set(list_fiat)


def up_step():
    s = fiat_listbox.curselection()
    if len(s) == 1:
        s = s[0]
        list_fiat[s-1:s+1] = list_fiat[s-1:s+1][::-1]
        fiat_var.set(list_fiat)
        fiat_listbox.selection_clear(0, END)
        fiat_listbox.selection_set(s-1)


def down_step():
    s = fiat_listbox.curselection()
    if len(s) == 1:
        s = s[0]
        list_fiat[s:s+2] = list_fiat[s:s+2][::-1]
        fiat_var.set(list_fiat)
        fiat_listbox.selection_clear(0, END)
        fiat_listbox.selection_set(s+1)

wind_select = Tk()
wind_select.title("METANIT.COM")
wind_select.geometry("630x250")

ttk.Button(text="Добавить", command=add_fiat).grid(row=0, column=1, padx=6, pady=6)

ttk.Button(text="Удалить", command=delete).grid(row=0, column=3, padx=5, pady=5)

ttk.Button(text="▲", command=up_step).grid(row=1, column=3, padx=5, pady=5)

ttk.Button(text="▼", command=down_step).grid(row=2, column=3, padx=5, pady=5)

ttk.Button(text="Очистить", command=del_all).grid(row=3, column=3, padx=5, pady=5)

fiat_all_var = Variable(value=list_fiat_all)
fiat_all_listbox = Listbox(listvariable=fiat_all_var, width=35)
fiat_all_listbox.grid(row=0, column=0, rowspan=4, sticky=EW, padx=5, pady=5)

fiat_var = Variable(value=list_fiat)
fiat_listbox = Listbox(listvariable=fiat_var, width=35, selectmode="single")
fiat_listbox.grid(row=0, column=2, rowspan=4, sticky=EW, padx=5, pady=5)

wind_select.mainloop()