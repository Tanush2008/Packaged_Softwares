from tkinter import *
import google_currency
from google_currency import convert
#------------------------------
#import googltrans
#print(googlettrans.LANGUAGES)
#------------------------------

#Translator function 
def translate():
    #a=currency_from()
    #b=currency_to()
    #a=float(a)
    #b=float(b)
    k = {
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "DZD": "Algerian Dinar",
    "AOA": "Angolan Kwanza",
    "ARS": "Argentine Peso",
    "AMD": "Armenian Dram",
    "AWG": "Aruban Florin",
    "AUD": "Australian Dollar",
    "AZN": "Azerbaijani Manat",
    "BSD": "Bahamian Dollar",
    "BHD": "Bahraini Dinar",
    "BBD": "Bajan dollar",
    "BDT": "Bangladeshi Taka",
    "BYR": "Belarusian Ruble",
    "BZD": "Belize Dollar",
    "BMD": "Bermudan Dollar",
    "BTN": "Bhutan currency",
    "BTC": "Bitcoin",
    "BCH": "Bitcoin Cash",
    "BOB": "Bolivian Boliviano",
    "BAM": "Bosnia-Herzegovina Convertible Mark",
    "BWP": "Botswanan Pula",
    "BRL": "Brazilian Real",
    "BND": "Brunei Dollar",
    "BGN": "Bulgarian Lev",
    "BIF": "Burundian Franc",
    "XPF": "CFP Franc",
    "KHR": "Cambodian riel",
    "CAD": "Canadian Dollar",
    "CVE": "Cape Verdean Escudo",
    "KYD": "Cayman Islands Dollar",
    "XAF": "Central African CFA franc",
    "CLP": "Chilean Peso",
    "CLF": "Chilean Unit of Account (UF)",
    "CNY": "Chinese Yuan",
    "CNH": "Chinese Yuan (offshore)",
    "COP": "Colombian Peso",
    "KMF": "Comorian franc",
    "CDF": "Congolese Franc",
    "CRC": "Costa Rican Colón",
    "HRK": "Croatian Kuna",
    "CUP": "Cuban Peso",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "DJF": "Djiboutian Franc",
    "DOP": "Dominican Peso",
    "XCD": "East Caribbean Dollar",
    "EGP": "Egyptian Pound",
    "ETH": "Ether",
    "ETB": "Ethiopian Birr",
    "EUR": "Euro",
    "FJD": "Fijian Dollar",
    "GMD": "Gambian dalasi",
    "GEL": "Georgian Lari",
    "GHC": "Ghanaian Cedi",
    "GIP": "Gibraltar Pound",
    "GTQ": "Guatemalan Quetzal",
    "GNF": "Guinean Franc",
    "GYD": "Guyanaese Dollar",
    "HTG": "Haitian Gourde",
    "HNL": "Honduran Lempira",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "ISK": "Icelandic Króna",
    "INR": "Indian Rupee",
    "IDR": "Indonesian Rupiah",
    "IRR": "Iranian Rial",
    "IQD": "Iraqi Dinar",
    "ILS": "Israeli New Shekel",
    "JMD": "Jamaican Dollar",
    "JPY": "Japanese Yen",
    "JOD": "Jordanian Dinar",
    "KZT": "Kazakhstani Tenge",
    "KES": "Kenyan Shilling",
    "KWD": "Kuwaiti Dinar",
    "KGS": "Kyrgystani Som",
    "LAK": "Laotian Kip",
    "LBP": "Lebanese pound",
    "LSL": "Lesotho loti",
    "LRD": "Liberian Dollar",
    "LYD": "Libyan Dinar",
    "LTC": "Litecoin",
    "MOP": "Macanese Pataca",
    "MKD": "Macedonian Denar",
    "MGA": "Malagasy Ariary",
    "MWK": "Malawian Kwacha",
    "MYR": "Malaysian Ringgit",
    "MVR": "Maldivian Rufiyaa",
    "MRO": "Mauritanian Ouguiya (1973–2017)",
    "MUR": "Mauritian Rupee",
    "MXN": "Mexican Peso",
    "MDL": "Moldovan Leu",
    "MAD": "Moroccan Dirham",
    "MZM": "Mozambican metical",
    "MMK": "Myanmar Kyat",
    "TWD": "NT$",
    "NAD": "Namibian dollar",
    "NPR": "Nepalese Rupee",
    "ANG": "Netherlands Antillean Guilder",
    "NZD": "New Zealand Dollar",
    "NIO": "Nicaraguan Córdoba",
    "NGN": "Nigerian Naira",
    "NOK": "Norwegian Krone",
    "OMR": "Omani Rial",
    "PKR": "Pakistani Rupee",
    "PAB": "Panamanian Balboa",
    "PGK": "Papua New Guinean Kina",
    "PYG": "Paraguayan Guarani",
    "PHP": "Philippine Piso",
    "PLN": "Poland złoty",
    "GBP": "Pound sterling",
    "QAR": "Qatari Rial",
    "ROL": "Romanian Leu",
    "RUR": "Russian Ruble",
    "RUB": "Russian Ruble",
    "RWF": "Rwandan franc",
    "SVC": "Salvadoran Colón",
    "SAR": "Saudi Riyal",
    "CSD": "Serbian Dinar",
    "SCR": "Seychellois Rupee",
    "SLL": "Sierra Leonean Leone",
    "SGD": "Singapore Dollar",
    "PEN": "Sol",
    "SBD": "Solomon Islands Dollar",
    "SOS": "Somali Shilling",
    "ZAR": "South African Rand",
    "KRW": "South Korean won",
    "VEF": "Sovereign Bolivar",
    "XDR": "Special Drawing Rights",
    "LKR": "Sri Lankan Rupee",
    "SSP": "Sudanese pound",
    "SRD": "Surinamese Dollar",
    "SZL": "Swazi Lilangeni",
    "SEK": "Swedish Krona",
    "CHF": "Swiss Franc",
    "TJS": "Tajikistani Somoni",
    "TZS": "Tanzanian Shilling",
    "THB": "Thai Baht",
    "TOP": "Tongan Paʻanga",
    "TTD": "Trinidad & Tobago Dollar",
    "TND": "Tunisian Dinar",
    "TRY": "Turkish lira",
    "TMM": "Turkmenistan manat",
    "UGX": "Ugandan Shilling",
    "UAH": "Ukrainian hryvnia",
    "AED": "United Arab Emirates Dirham",
    "USD": "United States Dollar",
    "UYU": "Uruguayan Peso",
    "UZS": "Uzbekistani Som",
    "VND": "Vietnamese dong",
    "XOF": "West African CFA franc",
    "YER": "Yemeni Rial",
    "ZMW": "Zambian Kwacha"
}
    #lc = k.keys()
    for key, value in k.items():
        #try:
            if value==a.lower():
                acode=key
            if value==b.lower():
                bcode=key
        #except UnboundLocalError:
            #print("error")
            
    translator= convert()
    translation = translator.translate(var.get(), src = acode,dest = bcode)
    var1.set(translation.amount)

#Tkinter root Window with title
root = Tk()
root.title("Money Converter")

#Creating a Frame and Grid to hold the Content
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
#mainframe.pack(pady = 100, padx = 100)
mainframe.configure(background = 'red')
#variables for dropdown list
currency_from = StringVar(root)
currency_to = StringVar(root)

#choices to show in dropdown menu
choices = { 'AED','USD','INR'}
#default selection for dropdownlists
currency_from.set('USD')
currency_to.set('INR')

#creating dropdown and arranging in the grid
currency_frommenu = OptionMenu( mainframe, currency_from, *choices)
Label(mainframe,text="Select a Country", fg = 'black', bg = "hot pink").grid(row = 0, column = 1)
currency_frommenu.grid(row = 1, column =1)

currency_to = OptionMenu( mainframe, currency_to, *choices)
Label(mainframe,text="Select a Country", fg = 'black', bg = "light blue").grid(row = 0, column = 2)
currency_to.grid(row = 1, column =2)

#Text Box to take user input
Label(mainframe, text = "Enter value", fg = 'green').grid(row=2,column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2,column=1)

#textbox to show output
#label can also be used
Label(mainframe, text = "Output", fg = 'red').grid(row=2,column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1).grid(row=2,column=3)

#creating a button to call Translator function
b=Button(mainframe,text='Convert', fg = 'black', bg = "yellow",command=translate).grid(row=8,column=1,columnspan=3)

root.mainloop()
