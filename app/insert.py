from flask import Flask, render_template, request , redirect, url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
app = Flask(__name__ , template_folder="templates")
uri = "mongodb+srv://imicorp:BNCjJPAswlcwQP93@cluster0.mh1eamh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# post = [{
#   '1': [ 2 ],
#   '2': [ 1, 3 ],
#   '3': [ 2, 4 ],
#   '4': [ 3, 5 ],
#   '5': [ 4, 6 ],
#   '6': [ 5, 7 ],
#   '7': [ 6, 8 ],
#   '8': [ 7, 9 ],
#   '9': [ 8, 10 ],
#   '10': [ 9, 11 , 65 , 66 ],
#   '11': [ 10, 12 ],
#   '12': [ 11, 13 , 117 , 118 ],
#   '13': [ 12, 14 ],
#   '14': [ 13, 15 , 85 , 44 ],
#   '15': [ 14, 16 ],
#   '16': [ 15, 17 , 46 , 47 ],
#   '17': [ 16, 18 ],
#   '18': [ 17, 19 ],
#   '19': [ 18, 20 , 137 , 71 ],
#   '20': [ 19, 21 ],
#   '21': [ 20, 22 ],
#   '22': [ 21, 23 ],
#   '23': [ 22, 24 ],
#   '24': [ 23, 25 ],
#   '25': [ 24, 26 ],
#   '26': [ 25, 27 ],
#   '27': [ 26, 28 ],
#   '28': [ 27, 29 ],
#   '29': [ 28, 30 ],
#   '30': [ 29, 31 ],
#   '31': [ 30, 32 ],
#   '32': [ 31, 33 ],
#   '33': [ 32 ],
#   '34': [ 35 ],
#   '35': [ 34, 36 ],
#   '36': [ 35, 37 ],
#   '37': [ 36, 38 ],
#   '38': [ 37, 39 ],
#   '39': [ 38, 40 ],
#   '40': [ 39, 41 ],
#   '41': [ 40, 42 ],
#   '42': [ 41, 43 ],
#   '43': [ 42, 44 , 116 , 84 ],
#   '44': [ 43, 45 , 84 ],
#   '45': [ 44, 46 ],
#   '46': [ 45, 47 ],
#   '47': [ 46, 48 ],
#   '48': [ 47, 49 ],
#   '49': [ 48, 50 ],
#   '50': [ 49, 51 , 87 , 141 ],
#   '51': [ 50, 52 , 87 , 88 ],
#   '52': [ 51, 53 ],
#   '53': [ 52, 54 ],
#   '54': [ 53 , 95 ],
#   '55': [ 56 ],
#   '56': [ 55, 57 ],
#   '57': [ 56, 58 ],
#   '58': [ 57, 59 ],
#   '59': [ 58, 60 ],
#   '60': [ 59, 61 ],
#   '61': [ 60, 62 ],
#   '62': [ 61, 63 ],
#   '63': [ 62, 64 ],
#   '64': [ 63, 65 ],
#   '65': [ 64, 66 ],
#   '66': [ 65, 67 ],
#   '67': [ 66, 68 ],
#   '68': [ 67, 69 , 111 ],
#   '69': [ 68, 70 , 85 , 86 ],
#   '70': [ 69, 71 ],
#   '71': [ 70, 72 , 138 ],
#   '72': [ 71, 73 ],
#   '73': [ 72, 74 ],
#   '74': [ 73, 75 ],
#   '75': [ 74, 76 ],
#   '76': [ 75, 77 ],
#   '77': [ 76, 78 ],
#   '78': [ 77 ],
#   '79': [ 80 ],
#   '80': [ 79, 81 ],
#   '81': [ 80, 82 ],
#   '82': [ 81, 83 ],
#   '83': [ 82, 84 ],
#   '84': [ 83, 85 , 110 , 43 ],
#   '85': [ 84, 86 ],
#   '86': [ 85, 87 ],
#   '87': [ 86, 88 , 142 , 50 ],
#   '88': [ 87, 89 ],
#   '89': [ 88, 90 ],
#   '90': [ 89, 91 ],
#   '91': [ 90, 92 ],
#   '92': [ 91, 93 ],
#   '93': [ 92, 94 ],
#   '94': [ 93, 95 ],
#   '95': [ 94 , 96 , 54 ],
#   '96': [ 97 , 95 ],
#   '97': [ 96, 98 ],
#   '98': [ 97, 99 ],
#   '99': [ 98, 100 ],
#   '100': [ 99, 101 ],
#   '101': [ 100, 102 ],
#   '102': [ 101, 103 ],
#   '103': [ 102, 104 ],
#   '104': [ 103 ],
#   '105': [ 106 ],
#   '106': [ 105, 107 ],
#   '107': [ 106, 108 ],
#   '108': [ 107, 109 ],
#   '109': [ 108, 110 ],
#   '110': [ 109, 111 ],
#   '111': [ 110, 112 , 142 , 143 ],
#   '112': [ 111, 113 ],
#   '113': [ 112, 114 ],
#   '114': [ 113, 115 ],
#   '115': [ 114, 116 ],
#   '116': [ 115, 117 ],
#   '117': [ 116, 118 ],
#   '118': [ 117, 119 ],
#   '119': [ 118, 120 ],
#   '120': [ 119, 121 ],
#   '121': [ 120, 122 ],
#   '122': [ 121, 123 ],
#   '123': [ 122, 124 ],
#   '124': [ 123, 125 ],
#   '125': [ 124, 126 ],
#   '126': [ 125, 127 ],
#   '127': [ 126, 128 ],
#   '128': [ 127, 129 ],
#   '129': [ 128, 130 ],
#   '130': [ 129, 131 ],
#   '131': [ 130 ],
#   '132': [ 133 ],
#   '133': [ 132, 134 ],
#   '134': [ 133, 135 ],
#   '135': [ 134, 136 ],
#   '136': [ 135, 137 ],
#   '137': [ 136, 138 ],
#   '138': [ 137, 139 ],
#   '139': [ 138, 140 ],
#   '140': [ 139, 141 ],
#   '141': [ 140, 142 ],
#   '142': [ 141, 143 ],
#   '143': [ 142, 144 ],
#   '144': [ 143, 145 ],
#   '145': [ 144, 146 ],
#   '146': [ 145, 147 ],
#   '147': [ 146 ]
# }]





# # THIS‌ ARE‌ FOR‌ POSTING IN‌ DATABASE=====>>



# myarray = [
#   {'1': [ 2 ]},
#   {'2': [ 1, 3 ]},
#   {'3': [ 2, 4 ]},
#   {'4': [ 3, 5 ]},
#   {'5': [ 4, 6 ]},
#   {'6': [ 5, 7 ]},
#   {'7': [ 6, 8 ]},
#   {'8': [ 7, 9 ]},
#   {'9': [ 8, 10 ]},
#   {'10': [ 9, 11 , 65 , 66 ]},
#   {'11': [ 10, 12 ]},
#   {'12': [ 11, 13 , 117 , 118 ]},
#   {'13': [ 12, 14 ]},
#   {'14': [ 13, 15 , 85 , 44 ]},
#   {'15': [ 14, 16 ]},
#   {'16': [ 15, 17 , 46 , 47 ]},
#   {'17': [ 16, 18 ]},
#   {'18': [ 17, 19 ]},
#   {'19': [ 18, 20 , 137 , 71 ]},
#   {'20': [ 19, 21 ]},
#   {'21': [ 20, 22 ]},
#   {'22': [ 21, 23 ]},
#   {'23': [ 22, 24 ]},
#   {'24': [ 23, 25 ]},
#   {'25': [ 24, 26 ]},
#   {'26': [ 25, 27 ]},
#   {'27': [ 26, 28 ]},
#   {'28': [ 27, 29 ]},
#   {'29': [ 28, 30 ]},
#   {'30': [ 29, 31 ]},
#   {'31': [ 30, 32 ]},
#   {'32': [ 31, 33 ]},
#   {'33': [ 32 ]},
#   {'34': [ 35 ]},
#   {'35': [ 34, 36 ]},
#   {'36': [ 35, 37 ]},
#   {'37': [ 36, 38 ]},
#   {'38': [ 37, 39 ]},
#   {'39': [ 38, 40 ]},
#   {'40': [ 39, 41 ]},
#   {'41': [ 40, 42 ]},
#   {'42': [ 41, 43 ]},
#   {'43': [ 42, 44 , 116 , 84 ]},
#   {'44': [ 43, 45 , 84 ]},
#   {'45': [ 44, 46 ]},
#   {'46': [ 45, 47 ]},
#   {'47': [ 46, 48 ]},
#   {'48': [ 47, 49 ]},
#   {'49': [ 48, 50 ]},
#   {'50': [ 49, 51 , 87 , 141 ]},
#   {'51': [ 50, 52 , 87 , 88 ]},
#   {'52': [ 51, 53 ]},
#   {'53': [ 52, 54 ]},
#   {'54': [ 53 , 95 ]},
#   {'55': [ 56 ]},
#   {'56': [ 55, 57 ]},
#   {'57': [ 56, 58 ]},
#   {'58': [ 57, 59 ]},
#   {'59': [ 58, 60 ]},
#   {'60': [ 59, 61 ]},
#   {'61': [ 60, 62 ]},
#   {'62': [ 61, 63 ]},
#   {'63': [ 62, 64 ]},
#   {'64': [ 63, 65 ]},
#   {'65': [ 64, 66 ]},
#   {'66': [ 65, 67 ]},
#   {'67': [ 66, 68 ]},
#   {'68': [ 67, 69 , 111 ]},
#   {'69': [ 68, 70 , 85 , 86 ]},
#   {'70': [ 69, 71 ]},
#   {'71': [ 70, 72 , 138 ]},
#   {'72': [ 71, 73 ]},
#   {'73': [ 72, 74 ]},
#   {'74': [ 73, 75 ]},
#   {'75': [ 74, 76 ]},
#   {'76': [ 75, 77 ]},
#   {'77': [ 76, 78 ]},
#   {'78': [ 77 ]},
#   {'79': [ 80 ]},
#   {'80': [ 79, 81 ]},
#   {'81': [ 80, 82 ]},
#   {'82': [ 81, 83 ]},
#   {'83': [ 82, 84 ]},
#   {'84': [ 83, 85 , 110 , 43 ]},
#   {'85': [ 84, 86 ]},
#   {'86': [ 85, 87 ]},
#   {'87': [ 86, 88 , 142 , 50 ]},
#   {'88': [ 87, 89 ]},
#   {'89': [ 88, 90 ]},
#   {'90': [ 89, 91 ]},
#   {'91': [ 90, 92 ]},
#   {'92': [ 91, 93 ]},
#   {'93': [ 92, 94 ]},
#   {'94': [ 93, 95 ]},
#   {'95': [ 94 , 96 , 54 ]},
#   {'96': [ 97 , 95 ]},
#   {'97': [ 96, 98 ]},
#   {'98': [ 97, 99 ]},
#   {'99': [ 98, 100 ]},
#   {'100': [ 99, 101 ]},
#   {'101': [ 100, 102 ]},
#   {'102': [ 101, 103 ]},
#   {'103': [ 102, 104 ]},
#   {'104': [ 103 ]},
#   {'105': [ 106 ]},
#   {'106': [ 105, 107 ]},
#   {'107': [ 106, 108 ]},
#   {'108': [ 107, 109 ]},
#   {'109': [ 108, 110 ]},
#   {'110': [ 109, 111 ]},
#   {'111': [ 110, 112 , 142 , 143 ]},
#   {'112': [ 111, 113 ]},
#   {'113': [ 112, 114 ]},
#   {'114': [ 113, 115 ]},
#   {'115': [ 114, 116 ]},
#   {'116': [ 115, 117 ]},
#   {'117': [ 116, 118 ]},
#   {'118': [ 117, 119 ]},
#   {'119': [ 118, 120 ]},
#   {'120': [ 119, 121 ]},
#   {'121': [ 120, 122 ]},
#   {'122': [ 121, 123 ]},
#   {'123': [ 122, 124 ]},
#   {'124': [ 123, 125 ]},
#   {'125': [ 124, 126 ]},
#   {'126': [ 125, 127 ]},
#   {'127': [ 126, 128 ]},
#   {'128': [ 127, 129 ]},
#   {'129': [ 128, 130 ]},
#   {'130': [ 129, 131 ]},
#   {'131': [ 130 ]},
#   {'132': [ 133 ]},
#   {'133': [ 132, 134 ]},
#   {'134': [ 133, 135 ]},
#   {'135': [ 134, 136 ]},
#   {'136': [ 135, 137 ]},
#   {'137': [ 136, 138 ]},
#   {'138': [ 137, 139 ]},
#   {'139': [ 138, 140 ]},
#   {'140': [ 139, 141 ]},
#   {'141': [ 140, 142 ]},
#   {'142': [ 141, 143 ]},
#   {'143': [ 142, 144 ]},
#   {'144': [ 143, 145 ]},
#   {'145': [ 144, 146 ]},
#   {'146': [ 145, 147 ]},
#   {'147': [ 146 ]}
# ]





myguy = [{ "line": 1, "name": 'تجریش', "state": 1 },
  { "line": 1, "name": 'قیطریه', "state": 2 },
  { "line": 1, "name": 'شهید صدر', "state": 3 },
  { "line": 1, "name": 'قلهک', "state": 4 },
  { "line": 1, "name": 'دکتر شریعتی', "state": 5 },
  { "line": 1, "name": 'میرداماد', "state": 6 },
  { "line": 1, "name": 'شهید حقانی', "state": 7 },
  { "line": 1, "name": 'شهید همت', "state": 8 },
  { "line": 1, "name": 'مصلی امام خمینی', "state": 9 },
  { "line": 1, "name": 'شهید بهشتی', "state": 10 },
  { "line": 1, "name": 'شهید مفتح', "state": 11 },
  { "line": 1, "name": 'شهدای هفتم تیر', "state": 12 },
  { "line": 1, "name": 'طالقانی', "state": 13 },
  { "line": 1, "name": 'دروازه دولت', "state": 14 },
  { "line": 1, "name": 'سعدی', "state": 15 },
  { "line": 1, "name": 'امام خمینی', "state": 16 },
  { "line": 1, "name": 'پانزده خرداد', "state": 17 },
  { "line": 1, "name": 'خیام', "state": 18 },
  { "line": 1, "name": 'میدان محمدیه', "state": 19 },
  { "line": 1, "name": 'شوش', "state": 20 },
  { "line": 1, "name": 'پایانه جنوب', "state": 21 },
  { "line": 1, "name": 'شهید بخارایی', "state": 22 },
  { "line": 1, "name": 'علی آباد', "state": 23 },
  { "line": 1, "name": 'جوانمرد قصا', "state": 24 },
  { "line": 1, "name": 'شهر ری', "state": 25 },
  { "line": 1, "name": 'پالایشگاه', "state": 26 },
  { "line": 1, "name": 'شاهد - باقر شهر', "state": 27 },
  { "line": 1, "name": 'نمایشگاه آفتاب', "state": 28 },
  { "line": 1, "name": 'واوان', "state": 29 },
  { "line": 1, "name": 'فرودگاه امام خمینی', "state": 30 },
  { "line": 1, "name": 'شاهد - باقر شهر', "state": 31 },
  { "line": 1, "name": 'هرم مطهر امام خمینی', "state": 32 },
  { "line": 1, "name": 'کهریزک', "state": 33 },
  { "line": 2, "name": 'ّفرهنگسرا', "state": 34 },
  { "line": 2, "name": 'تهرانپارس', "state": 35 },
  { "line": 2, "name": 'شهید باقری', "state": 36 },
  { "line": 2, "name": 'دانشگاه علم و صنعت', "state": 37 },
  { "line": 2, "name": 'سرسبز', "state": 38 },
  { "line": 2, "name": 'جانبازان', "state": 39 },
  { "line": 2, "name": 'فدک', "state": 40 },
  { "line": 2, "name": 'سلبان', "state": 41 },
  { "line": 2, "name": 'شهید مدنی', "state": 42 },
  { "line": 2, "name": 'امام حسین', "state": 43 },
  { "line": 2, "name": 'دروازه شمیران', "state": 44 },
  { "line": 2, "name": 'بهارستان', "state": 45 },
  { "line": 2, "name": 'ملت', "state": 46 },
  { "line": 2, "name": 'حسن آباد', "state": 47 },
  { "line": 2, "name": 'دانشگاه امام علی', "state": 48 },
  { "line": 2, "name": 'میدان حر', "state": 49 },
  { "line": 2, "name": 'شهید نواب صفوی', "state": 50 },
  { "line": 2, "name": 'شادمان', "state": 51 },
  { "line": 2, "name": 'دانشگاه شریف', "state": 52 },
  { "line": 2, "name": 'طرشت', "state": 53 },
  { "line": 2, "name": 'صادقیه', "state": 54 },
  { "line": 3, "name": '‌قائم', "state": 55 },
  { "line": 3, "name": 'شهید محلاتی', "state": 56 },
  { "line": 3, "name": 'اقدسیه', "state": 57 },
  { "line": 3, "name": 'نوبنیاد', "state": 58 },
  { "line": 3, "name": 'حسین آباد', "state": 59 },
  { "line": 3, "name": 'میدان هروی', "state": 60 },
  { "line": 3, "name": 'شهید زین الدین', "state": 61 },
  { "line": 3, "name": 'خواجه ابدالله انصاری', "state": 62 },
  { "line": 3, "name": 'شهید صیاد شیرازی', "state": 63 },
  { "line": 3, "name": 'شهید قدوسی', "state": 64 },
  { "line": 3, "name": 'سهروردی', "state": 65 },
  { "line": 3, "name": 'میرزای شیرازی', "state": 66 },
  { "line": 3, "name": 'میدان جهاد', "state": 67 },
  { "line": 3, "name": 'میدان حضرت ولیعصر', "state": 68 },
  { "line": 3, "name": 'تأتر شهر', "state": 69 },
  { "line": 3, "name": 'منیریه', "state": 70 },
  { "line": 3, "name": 'مهدیه', "state": 71 },
  { "line": 3, "name": 'راه آهن', "state": 72 },
  { "line": 3, "name": 'جوادیه', "state": 73 },
  { "line": 3, "name": 'زم زم', "state": 74 },
  { "line": 3, "name": 'شهرک شریعتی', "state": 75 },
  { "line": 3, "name": 'عبدل آباد', "state": 76 },
  { "line": 3, "name": 'نعمت آباد', "state": 77 },
  { "line": 3, "name": 'آزادگان', "state": 78 },
{"line":4,"name":"شهید کلاهدوز","state":79}
,{"line":4,"name":"نیرو هوایی","state":80}
,{"line":4,"name":"نبرد","state":81}
,{"line":4,"name":"پیروزی","state":82}
,{"line":4,"name": "ابن سینا","state":83}
,{"line":4,"name":"میدان شهدا","state":84}
,{"line":4,"name":"فردوسی","state":85}
,{"line":4,"name":"میدان انقلاب","state":86}
,{"line":4,"name":"توحید","state":87}
,{"line":4,"name":"دکتر حبیب","state":88}
,{"line":4,"name":"استاد معین","state":89}
,{"line":4,"name":"میدان آزادی","state":90}
,{"line":4,"name":"بیمه","state":91}
,{"line":4,"name":"پایانه 1 و 2 فرودگاه مهرآباد","state":92}
,{"line":4,"name":"پایانه 4 و 6 فرودگاه مهرآباد","state":93}
,{"line":4,"name":"شهرک اکباتان","state":94}
,{"line":4,"name":"ارم سبز","state":95},
{ "line" :5, "name" :"ورزشگاه آزادی", "state" :96},
{ "line" :5, "name" :"چیتگر", "state" :97},
{ "line" :5, "name" :"ایران خودرو", "state" :98},
{ "line" :5, "name" :"وردآورد", "state" :99},
{ "line" :5, "name" :"گرم دره", "state" :100},
{ "line" :5, "name" :"اتمسفر", "state" :101},
{ "line" :5, "name" :"کرج", "state" :102},
{ "line" :5, "name" :"محمد شهر", "state" :103},
{ "line" :5, "name" :"گلشهر", "state" :104},
{"line":6,"name":"حرم حضرت ابدالعظیم", "state" :105},
{ "line" :6, "name" :"میدان حضرت ابدالعظیم", "state" :106},
{ "line" :6, "name" :"ابن بابویه", "state" :107},
{ "line" :6, "name" :"چشمه علی", "state" :108},
{ "line" :6, "name" :"دولت آباد", "state" :109},
{ "line" :6, "name" :"کیان شهر", "state" :110},
{ "line" :6, "name" :"بعث", "state" :111},
{ "line" :6, "name" :"شهید رضایی", "state" :112},
{ "line" :6, "name" :"میدان خراسان", "state" :113},
{ "line" :6, "name" :"شهدای هفده شهریور", "state" :114},
{ "line" :6, "name" :"امیرکبیر", "state" :115},
{ "line" :6, "name" :"سرباز", "state" :116},
{ "line" :6, "name" :"بهار شیراز", "state" :117},
{ "line" :6, "name" :"شهدای نجات اللهی", "state" :118},
{ "line" :6, "name" :"بوستان لاله", "state" :119},
{ "line" :6, "name" :"کارگر", "state" :120},
{ "line" :6, "name" :"دانشگاه تربیت مدرس", "state" :121},
{ "line" :6, "name" :"شهرک آزمایش", "state" :122},
{ "line" :6, "name" :"مرزداران", "state" :123},
{ "line" :6, "name" :"یادگار امام", "state" :124},
{ "line" :6, "name" :"شهید اشرفی اصفهانی", "state" :125},
{ "line" :6, "name" :"شهید ستاری", "state" :126},
{ "line" :6, "name" :"آیت الله کاشانی", "state" :127},
{ "line" :6, "name" :"شهر زیبا","state":128},
{ "line" :6, "name" :"شهران","state":129},
{ "line" :6, "name" :"شهدای کن","state":130},
{ "line" :6, "name" :"کوهسار","state":131},
{ "line" :7, "name" :"ورزشگاه تختی", "state" :132},
{ "line" :7, "name" :"بسیج", "state" :133},
{ "line" :7, "name" :"آهنگ", "state" :134},
{ "line" :7, "name" :"بزرگراه شهید محلاتی", "state" :135},
{ "line" :7, "name" :"میدان قیام", "state" :136},
{ "line" :7, "name" :"مولوی", "state" :137},
{ "line" :7, "name" :"هلال احمر", "state" :138},
{ "line" :7, "name" :"بریانک", "state" :139},
{ "line" :7, "name" :"کمیل", "state" :140},
{ "line" :7, "name" :"رودکی", "state" :141},
{ "line" :7, "name" :"مدافعان سلامت", "state" :142},
{ "line" :7, "name" :"بوستان گفتگو", "state" :143},
{ "line" :7, "name" :"برج میلاد تهران", "state" :144},
{ "line" :7, "name" :"میدان صنعت", "state" :145},
{ "line" :7, "name" :"شهید دادمان", "state" :146},
{ "line" :7, "name" :"میدان کتاب", "state" :147}]


db = client.test_database
posts = db.posts

post_id = posts.insert_many(myguy).inserted_ids
print(post_id)