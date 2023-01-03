from flask import Flask, render_template, request, redirect, url_for, session, Response, make_response, send_file
import pandas as pd
import pandas.io.sql as psql
import re,json,io,MySQLdb
from wtforms import TextField, Form, SelectField, RadioField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource,Api

app = Flask(__name__)

app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
db.set_character_set('utf8')
query = "select * from data_sku"
api=Api(app)
df = psql.read_sql(query, con = db)

# connect_string = 'mysql://root:Alazhar4!@Localhost/data_sku'

# sql_engine = sql.create_engine(connect_string)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

list_hide = ['2101462301',
 '2101468',
 '2101486155',
 '2101453155',
 '2101453603',
 '2101684606',
 '2101453605',
 '2101453606',
 '2101401605',
 '2101428605',
 '2101428606',
 '2101684155',
 '2101891444',
 '1100525104',
 '1100534104',
 '1101003180',
 '1101569102',
 '1101572016',
 '1102101180',
 '1101672107',
 '2104403',
 '1101909019',
 '2102800129',
 '2105084145',
 '1101522451',
'1101909451',
'1101976451',
'1101558451',
'1101569451',
'1101907451',
'1102070451',
'1101573451',
'1101572451',
'1101978451',
'1101979451',
'1101982451',
'1101984451',
'(B)1101979451'
'1101572016',
'1101983016',
'(B)1101983016',
'(E)1101522017',
'(B)1101522017',
'1101522017',
'(B)1101983016',
'1101907019',
'1101909019',
'2305551401',
 '2306592173',
 '2101467',
 '2101401155',
 '2101468',
 '2101486155',
 '2101453603',
 '2101684606',
 '2101453605',
 '2101453606',
 '2101401605',
 '2101428605',
 '2101428606',
 '2101891444',
 '1100525104',
 '1100534104',
 '1101003180',
 '1101522451',
 '1101531451',
 '1101569102',
 '1101572016',
 '1101665104',
 '1102101190',
 '1101672318',
 '1101909451',
 '1101976451',
 '1101558451',
 '1101569451',
 '1101907451',
 '1102070451',
 '1101573451',
 '1101572451',
 '1101978451',
 '1101979451',
 '1101672107',
 '2104403',
 '1101909019',
 '2151084145',
 '2102800129',
 '2101385106',
 '2105084145',
 '(50%)2306551174',
 '(50%)2104031270',
 '(50%)1100525104',
 'E2101891443',
 '(R)1101983453',
 '(R)1101984453',
 '(S)2101551190',
 '(S)2101651190',
 '(S)2101684190',
 '(S)2102500130',
 '(S)2304558112',
 '1101982451',
 '1101569453',
 '1101909453',
 '(E)2305551401',
 '(E)1100534104',
 '(E)1102101180',
 '(E)1102101190',
 '(E)2101453605',
 '(E)1101522017',
 '(B)1102101180',
 '(B)1102101190',
 '(B)1101522017',
 '(B)2101453605',
 '71210111',
 '71210112',
 '1101983016',
 '1101984451',
 '1101522017',
 '(R)2306592173',
 '(R)1101987453',
 '(R)1101588453',
 '(R)1101534453',
 '(R)1101525453',
 '2101454447',
 '2101684155',
 '(R)1101989453',
 '(B)(R)1101989453',
 '2101551155',
 'PH38G137',
 '(R)1101927453',
 '(R)1101954453',
 '(R)1101930453',
 '71210164',
 '1101588016',
 '(R)1101573453',
 '(R)1101572453',
 '(R)1101978453',
 '(R)1101568453',
 '(R)1101580453',
 '(J)71110113',
 '(J)71110111',
 '(E)2101454447',
 '1101436453',
 '2101847036',
 '2102000135',
 '2101500148',
 '1101580453',
 '1101675318',
 '(B)1101675318'
]

list_hide_baru = ['2101453603',
 '2101684606',
 '2101453605',
 '2101453606',
 '2101401605',
 '2101428605',
 '2101428606',
 '2101891444',
 '1100525104',
 '1100534104',
 '1101003180',
 '1101531451',
 '1101569102',
 '1101665104',
 '(B)2102501125',
 '1101672318',
 '1101672107',
 '1101909019',
 '2151084145',
 '2102800129',
 '2201052106',
 '2201058106',
 '(50%)2306551174',
 '(50%)2104031270',
 '(50%)1100525104',
 '(B)2104031270',
 '(B)1100525104',
 '(B)740050175',
 '(B)740070175',
 '(B)2305551401',
 '(B)2304008151',
 '(B)71210024',
 '(B)71210025',
 '(B)71210000',
 '(B)71210001',
 '(B)71210002',
 '(B)71210007',
 '(B)71210015',
 '(B)71210017',
 '(B)71210018',
 '(B)71210020',
 'voucher-planet-sports-200.000',
 'hampers-body-shop',
 '(B)71210016',
 '(B)71210014',
 '(B)71210029',
 '(B)71210027',
 '(B)71210004',
 '(B)71210008',
 '(B)71210022',
 '(B)71210010',
 '(B)71210028',
 '(B)71210003',
 '(B)71210005',
 '(B)71210006',
 '(B)71210012',
 '(B)71210019',
 '(B)71210031',
 '(B)71210059',
 '(B)71210060',
 '(B)71210061',
 '(B)71210062',
 '(B)71210066',
 '(B)71210064',
 '(B)71210065',
 '(B)71210070',
 '(B)71210072',
 '(B)1101681318',
 '(B)1101573451',
 '(B)71210078',
 '(B)71210073',
 '(B)71210074',
 '(B)71210075',
 '(B)71210076',
 '(B)2101467',
 '(B)1101182250',
 '(B)71210079',
 '(B)2101428602',
 '(B)2303056180',
 '(B)1100534104',
 '(B)2101428180',
 '(B)71210081',
 '(B)71210082',
 '(B)71210083',
 '(B)71210084',
 '(B)71210085',
 '(B)71210086',
 '(B)71210087',
 '(B)71210088',
 '(B)71210089',
 '(B)71210090',
 '(B)71210091',
 '(B)71210093',
 '(B)2101385106',
 '(S)(B)71210013',
 '7300371',
 '7300351',
 'E2101891443',
 '2105500282',
 'EC00000038',
 'EC00000042',
 'EC00000035',
 'EC00000036',
 'EC00000039',
 'EC00000041',
 'EC00000037',
 'EC00000040',
 'EC00000043',
 'EC00000052',
 'EC00000055',
 'EC00000054',
 'EC00000056',
 'EC00000053',
 'EC00000031',
 'EC00000023',
 'EC00000034',
 'EC00000025',
 'EC00000029',
 'EC00000027',
 'EC00000026',
 'EC00000048',
 'EC00000045',
 'EC00000047',
 'EC00000046',
 'EC00000004',
 'EC00000058',
 'EC00000059',
 'EC00000057',
 'EC00000060',
 'EC00000005',
 'EC00000006',
 'EC00000051',
 'EC00000050',
 'EC00000049',
 'EC00000011',
 'EC00000010',
 'EC00000013',
 'EC00000009',
 'EC00000012',
 'EC00000017',
 'EC00000044',
 'EC00000061',
 'LL00000074',
 'LL00000077',
 'LL00000076',
 'LL00000079',
 'LL00000075',
 '(B)71210098',
 'PN29(2)N30N32G81',
 'PN4N22N23N28G81',
 'PT28G27',
 'PT17G27',
 'PT13G27',
 'PT1G27',
 '1101907019P3',
 'PT24T35T39',
 'PL8(2)G26',
 'PT8(2)G54',
 'PL7G75',
 '2101200180P3',
 '2101453190P3',
 'PL7L12T18',
 'PL3L8L12',
 'PL8P26',
 'PL6P26',
 'PT4T12',
 'PH23H28H29N22N28',
 'PH12N22N29T23',
 'PH12H29N23N29',
 'PH12H29T24',
 '(B)71210097',
 'PT3(2)G80',
 'PH10(2)G80',
 'PH27(2)G80',
 'PL6(2)G80',
 'PL13(2)G80',
 'PH9(2)G80',
 'PH16(2)G80',
 'PT28(2)G80',
 'PL8(2)G80',
 'PH5(2)G80',
 'PT6(2)G80',
 'PH17(2)G80',
 'PL1(2)G80',
 'PT4T23G27',
 'PL12(2)G80',
 'PT17(2)G80',
 '21014281P2',
 'PN36G81',
 'PT9(2)G80',
 'PT3G27',
 'PT23(2)G80',
 'PH41(5)B22',
 'PL7(2)G80',
 'PT13(2)G80',
 'PH7(2)G80',
 'PH15(2)G80',
 'PH6(2)G80',
 'PH20(2)G80',
 'PH24(2)G80',
 'PH8P31',
 'PT28(2)G29',
 'PL7(2)G26',
 'PT7(2)G29',
 'PH7(2)G29',
 'PH20(2)G29',
 'PH24(2)G29',
 'PT4T27G29',
 'PH13T4',
 'PT7(2)G80',
 'PH41(17)B22(7)',
 'PT35(2)G80',
 '(S)2101551190',
 '(S)2101651190',
 '(S)2101684190',
 '(S)2102500130',
 '(S)2304558112',
 '(S)2101684190P2',
 '(S)2101651190P2',
 '(S)2101551190P2',
 '(S)2102500130P2',
 '(S)2304558112P2',
 'PH6N50',
 'PH7N50',
 '1101569451P16',
 '1101909451P16',
 '1101522451P16',
 'PH41(12)B22(12)',
 'PN20N33(2)',
 'PB26N46',
 'PN20N33N46',
 'PN33N46',
 '(B)71210100',
 '(B)71210101',
 '(B)71210103',
 '(B)71210104',
 '(B)71210105',
 '(B)71210106',
 'PB24H43',
 'PL8G86',
 'PB25N34',
 'PB25(3)N34(3)',
 'PB25(12)N34(12)',
 '1101558451P16',
 '1101907451P16',
 '2101651180P3',
 'PN30N50G18',
 '1101572451P16',
 '1101982451P16',
 'PN20(2)N33',
 'PH12T4T24',
 '2102501125P3',
 'PL6G83',
 '2101847443P3',
 'PT1(2)G80',
 'PT5(2)G80',
 'PL5(2)G80',
 'PH4B16',
 'PN20(2)G56G79',
 '2103300125P3',
 '1101003180P2',
 '2101651190P3',
 'PL5L12',
 'PN29N33',
 '1101569451P3',
 '1101978451P3',
 '1101976451P3',
 '1101909451P3',
 '1101522451P3',
 'PH41B22',
 'PH20(2)G22',
 '1101978451P16',
 '1101675318P3',
 'PN20N33N46(2)G84',
 'PH29L13',
 'PH29L13(2)',
 'PH29N50',
 'PN20N50',
 'PN27N50',
 'PN30N50',
 'PN33N50',
 'PN19N50',
 'PH17N50',
 'PH12N50',
 'PH20N50',
 'PH22N50',
 'PH19N50',
 'PH9N50',
 'PN47N50',
 'PN20N47',
 'PH30N50',
 'PL6N50',
 'PH24N50',
 'PL9(5)B6',
 'PH31(4)H38',
 'PL4(2)G80',
 'PT28P31',
 'PT17T36T37',
 'PT8T40',
 'PT8T34',
 'PT24T28T35',
 'PT4T23',
 'PN46(4)G84',
 'PN20N46',
 'PN33(6)N46(6)',
 'PT23T40(2)',
 'PH41(9)B22(3)',
 '1101675318P1',
 'PT37(6)G76',
 '1101675318P6',
 '1101675318P12',
 '1101675318P24',
 'PL6(2)G83',
 'PL4(3)G83',
 'PL5(3)G83',
 'PL13(3)G83',
 '(B)71210107',
 '(B)71210108',
 'PL8G83',
 'PB25(12)N34(12)G91',
 '(B)71210110',
 'PH43(12)G93B24(12)',
 '1101675318P4',
 '1101531451P4',
 'PT7P55',
 '2204551186',
 '2204051148',
 '2206084355',
 'PW15W18W19W99W100',
 'PW18W19',
 'PH43(12)G47B24(12)',
 '(E)2304051151',
 '(E)2305551401',
 '(E)2101462303',
 '(E)2101551190',
 '(E)1100534104',
 '(E)1102101180',
 '(E)1102101190',
 '(E)2101551190P2',
 '(E)2101453605',
 '(E)1101522017',
 '(B)1102101180',
 '(B)2304051151',
 '(B)2101462303',
 '(B)1102101190',
 '(B)1101522017',
 '(B)2101453605',
 '(B)2104251230',
 'PT41B34',
 'PL8P19',
 'PL8P21',
 '(E)1101522017P2',
 '(E)2104251230',
 '(E)2104251230P2',
 'PT41T42',
 '71210111',
 'PE8H17',
 'PT42B34',
 '(B)71210113',
 '(B)71210114',
 '(B)71210115',
 'PH7(2)H9(4)H12(4)H15(4)G94',
 'PT1(2)T13(5)T23(5)T28(5)T37(6)T42(2)G94',
 'PL3(2)L8(2)L12(2)G94',
 'PH9(2)H12(4)L12(4)N36(2)N37(2)T42(4)G94',
 'PH7(5)H9(4)H15(5)H22(4)H24(4)H29(4)G94(2)',
 'PT5(4)T7(4)T13(6)T17(6)T23(6)T40(6)G94(2)',
 'PL3(2)L6(2)L8(4)L9(4)L12(5)G94(2)',
 'PL3(4)L6(4)L7(4)L8(4)L9(20)L12(6)G94(4)',
 'PT1(5)T2(5)T5T7(4)T13(8)T17(8)G94(5)',
 'PB32E12',
 '(B)71210116',
 '(B)71210117',
 '(B)71210118',
 '(B)71210119',
 '(B)71210120',
 '(B)71210123',
 '(B)71210124',
 'PL8L9(2)',
 'PN20N35(2)T3T22T43G105',
 '1101685318P12',
 'PB32(2)E12(2)',
 'PL6(2)G86G104',
 'PL8G83G104',
 'PT28P28',
 'PH12N22N29T24',
 'PH3H30',
 'PH8H30',
 'PH4H30',
 'PH5H30',
 'PH9H30',
 'PN36(3)G98',
 'PN16(3)G99',
 'PN37(3)G101',
 'PN39(3)G100',
 'PN18(3)G97',
 'PL6L9',
 'PH9B38',
 'PH5B38',
 'PT14T21',
 'PH19H35',
 'PB25(4)N34(8)',
 'PT8P54',
 'PT20T40',
 'PB25N34(2)G108',
 'PB25(8)N34(16)G108',
 'PH4P53',
 'PT4(2)T5T28T40(2)',
 'PH8H9H30(5)',
 'PH12(2)H19H20',
 'PT4(2)T40(4)',
 'PT23(2)T24(2)T39(2)',
 'PT6P54',
 'PT6P55',
 'PT24P33P35',
 '2101808450P1',
 'PN14(2)N18N36N37',
 'PH6H7(2)H12(2)H13H41(2)',
 '(B)2101551190',
 'PB25(4)N34(8)G108',
 'PN33N53',
 'PL11(24)L12',
 '(B)71210131',
 '(B)71210132',
 'PH6G113G114',
 'PH6G110G114',
 'PB32E12',
 'PL3(2)G49',
 'PL8(2)G83',
 '1101685318P6']

list_hide = list_hide + list_hide_baru

list_hide_baru = list(df[df['Brand'] == 'Partnership']['SKU'].unique())

list_hide = list_hide + list_hide_baru

list_hide_df = list(df[df['Active'] == 'Inactive']['Nama_Produk'].unique())

# list_hide = list_hide

list_hide_B = ['(B)' + x for x in list_hide]
list_hide_E = ['(E)' + x for x in list_hide]

list_hide = list_hide + list_hide_B + list_hide_E
list_auto = []
list_sku = list(df[(df['Brand']!='Bundle') & ~(df['SKU'].astype(str).isin(list_hide))  & ~(df['Nama_Produk'].astype(str).isin(list_hide_df))]['SKU'].unique())
list_nama = list(df[(df['Brand']!='Bundle') & ~(df['SKU'].astype(str).isin(list_hide)) & ~(df['Nama_Produk'].astype(str).isin(list_hide_df))]['Nama_Produk'].unique())
list_kode = list(df[(df['Brand']!='Bundle') & ~(df['SKU'].astype(str).isin(list_hide)) & ~(df['Nama_Produk'].astype(str).isin(list_hide_df)) & ~(df['Kode'].astype(str).isin(['x', '-'])) & (df['Kode'].notnull())]['Kode'].unique())
list_auto =  list_nama + list_sku + list_kode
list_sub = df[df['Brand']!='Bundle']['Sub_Brand'].drop_duplicates().dropna().to_list()
list_all = df['Nama_Produk'].to_list()

class restrialapinew(Resource):
    def get(self):
        # df=dbtrialapi.query.all()
        # engine = create_engine(SQLALCHEMY_DATABASE_URI)
        db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
        db.set_character_set('utf8')
        df = pd.read_sql_query("SELECT * FROM data_sku", con=db)
        df=df.to_json()
        df=json.loads(df)
        # print(df.to_dict())
        return df

api.add_resource(restrialapinew,'/apinew')

class SearchForm(Form):
    launch = RadioField('launch', validators=[InputRequired("Launching Tahap 1?")], choices=[('Yes', 'Launching Tahap 1'), ('No', 'Bukan Launching Tahap 1')], default='No', widget = None)
    produk1 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id='produk1')
    produk2 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id = "produk2")
    produk3 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id = "produk3")
    produk4 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id = "produk4")
    produk5 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id = "produk5")
    produk6 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id = "produk6")
    produk7 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id = "produk7")
    PCS1 = TextField(render_kw = {"placeholder" : "Input PCS Produk 1" }, id="PCS1")
    PCS2 = TextField(render_kw = {"placeholder" : "Input PCS Produk 2" }, id="PCS2")
    PCS3 = TextField(render_kw = {"placeholder" : "Input PCS Produk 3" }, id="PCS3")
    PCS4 = TextField(render_kw = {"placeholder" : "Input PCS Produk 4"}, id="PCS4")
    PCS5 = TextField(render_kw = {"placeholder" : "Input PCS Produk 5" }, id="PCS5")
    PCS6 = TextField(render_kw = {"placeholder" : "Input PCS Produk 6" }, id="PCS6")
    PCS7 = TextField(render_kw = {"placeholder" : "Input PCS Produk 7"}, id="PCS7")

class AddForm(Form):
    name = TextField(validators = [InputRequired("Please insert Product Name")], render_kw= {"placeholder" : "Insert Product Name"}, id = "name")
    sku = TextField(validators = [InputRequired("Please insert Product SKU")], render_kw= {"placeholder" : "Insert SKU"}, id = "sku")
    brand = SelectField(validators=[InputRequired("Please insert Brand")], id ='brand',choices = [(None, ''), ('NS', 'NS'), ('HiLo', 'HiLo'), ('L-Men', 'L-Men'), ('TS', 'TS'), ("W'dank", "W'dank"), ('WRP', 'WRP'), ('Heavenly Blush', 'Heavenly Blush'), ('Gimmick', 'Gimmick'), ('Bonus Produk', 'Bonus Produk'), ('Partnership', 'Partnership'), ('Lain Lain', 'Lain Lain')])
    nfi = TextField(validators=[InputRequired("Please insert Price List NFI")], render_kw={"placeholder" : "Insert Price List NFI"}, id = "nfi")
    cost = TextField(validators=[InputRequired("Please insert Cost Price")], render_kw={"placeholder" : "Insert Cost Price"}, id = "cost")
    display = TextField(validators=[InputRequired("Please insert Display Price")], render_kw={"placeholder" : "Insert Display Price"}, id = "display")
    organik = TextField(validators=[InputRequired("Please insert Organic Price")], render_kw={"placeholder" : "Insert Organic Price"}, id = "organik")
    code = TextField(validators=[InputRequired("Please insert Bundle Code")], render_kw={"placeholder" : "Insert Bundle Code"}, id = "code")
    parent = TextField(render_kw= {"placeholder" : "Insert Parent Name"}, id = "parent")
    # sub = TextField(validators=[InputRequired("Please insert sub")], render_kw={"placeholder" : "Insert sub"}, id = "sub")
    sub = SelectField(validators=[InputRequired("Please insert sub")], id = "sub", choices=[(None, ''),('L-MEN POWDER','L-MEN POWDER'),('L-MEN RTD','L-MEN RTD'),('NS TRADITIONAL','NS TRADITIONAL'),('PAKET NUTRISARI','PAKET NUTRISARI'),('NS MODERN','NS MODERN'),('NS RTD','NS RTD'),('PAKET WDANK','PAKET WDANK'),('TS MERAH','TS MERAH'),('TS KUNING OTHERS','TS KUNING OTHERS'),('TS KUNING - SWT POWDER','TS KUNING - SWT POWDER'),('TS BIRU','TS BIRU'),('PAKET TS','PAKET TS'),('DIABETAMIL','DIABETAMIL'),('HILO GOLD','HILO GOLD'),('HILO SCHOOL','HILO SCHOOL'),('HILO TEEN','HILO TEEN'),('HILO ACTIVE','HILO ACTIVE'),('HILO RTD','HILO RTD'),('HILO TRADITIONAL','HILO TRADITIONAL'),('PAKET HILO','PAKET HILO'),('WDANK TRADITIONAL','WDANK TRADITIONAL'),('WRP','WRP'),('HB','HB'),('OTHER','OTHER'),])
    parent_name = TextField(render_kw= {"placeholder" : "Insert Parent Name"}, id = "parent_name")
    parent_sku = TextField(render_kw= {"placeholder" : "Insert Parent Name"}, id = "parent_sku")
    berat = TextField(render_kw= {"placeholder" : "Insert Weight"}, id = "berat")
    volume = TextField(render_kw= {"placeholder" : "Insert Volume"}, id = "volume")
    nama_oracle = TextField(render_kw= {"placeholder" : "Insert Oracle Name"}, id = "nama_oracle")

class SearchSingle(Form):
    produk1 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id='produk1')

class AliasForm(Form):
    name = TextField(render_kw= {"placeholder" : "Insert Alias Name"}, id = "name")
    sku = TextField(render_kw= {"placeholder" : "Insert Alias SKU"}, id = "sku")

class AddMPForm(Form):
    name = TextField(render_kw= {"placeholder" : "Insert Bundle Name"}, id = "name")
    mp = SelectField('mp',choices = [('Blibli', 'Blibli'), ('Bukalapak', 'Bukalapak'), ('Jdid', 'Jdid'),  ('Lazada', 'Lazada'), ('Nutrimart', 'Nutrimart'), ('Shopee', 'Shopee'), ('Tokopedia', 'Tokopedia')])
    eksklusif = RadioField('eksklusif', validators=[InputRequired("Please insert exclusive status")], choices=[('Eksklusif', 'Eksklusif'), ('Not', 'Tidak Eksklusif')], default='Not', widget = None)

class AddGudangForm(Form):
    mp = SelectField('mp',choices = [('Blibli', 'Blibli'), ('Bukalapak', 'Bukalapak'), ('Jdid', 'Jdid'),  ('Lazada', 'Lazada'), ('Nutrimart', 'Nutrimart'), ('Shopee', 'Shopee'), ('Tokopedia', 'Tokopedia')])
    name = TextField(render_kw= {"placeholder" : "Insert Alias Name"}, id = "name")
    sku = TextField(render_kw= {"placeholder" : "Insert Alias SKU"}, id = "sku")



@app.route('/_autocomplete', methods = ['GET', 'POST'])
def autocomplete():
    return Response(json.dumps(list_auto), mimetype='application/json')

@app.route('/_autocompletesku', methods = ['GET', 'POST'])
def autocompletesku():
    return Response(json.dumps(list_sku), mimetype='application/json')

@app.route('/_autocompletekode', methods = ['GET', 'POST'])
def autocompletekode():
    return Response(json.dumps(list_kode), mimetype='application/json')

@app.route('/_autocompletesub', methods = ['GET', 'POST'])
def autocompletesub():
    return Response(json.dumps(list_sub), mimetype='application/json')

@app.route('/_autocompleteall', methods = ['GET', 'POST'])
def autocompleteall():
    return Response(json.dumps(list_all), mimetype='application/json')

def sorted_nicely( l ):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

def generate_SKU(list_produk, list_PCS):
    SKU_Bundle = ""
    list_SKU = []
    list_gimmick = []
    list_gimmick_qty = []
    list_SKU_gim = []

    global df

    if all(x == list_produk[0] for x in list_produk):
        for i in list_produk:
           if str(i) in df['SKU'].astype(str).values:
               SKU_Bundle = str(df[df['SKU'].astype(str) == str(i)]['SKU'].values[0]) + "P" + str(list_PCS[0])
           elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
               SKU_Bundle = str(df[str(i).lower() == df['Nama_Produk'].astype(str).str.lower()]['SKU'].values[0])  + "P" + str(list_PCS[0])
        return SKU_Bundle

    for i in list_produk:
        if str(i) in df['SKU'].astype(str).values:
            if df[df['SKU'].astype(str) == str(i)]['Brand'].values[0] in ['Gimmick', 'Bonus Produk', 'Partnership']:
                list_gimmick.append(i)
                idx = list_produk.index(i)
                list_gimmick_qty.append(list_PCS[idx])
        elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
            if df[df['Nama_Produk'].astype(str).str.lower() == str(i).lower()]['Brand'].values[0] in ['Gimmick', 'Bonus Produk', 'Partnership']:
                list_gimmick.append(i)
                idx = list_produk.index(i)
                list_gimmick_qty.append(list_PCS[idx])

    for i in list_gimmick :
        idx = list_produk.index(i)
        list_produk.pop(idx)
        list_PCS.pop(idx)

    for i in list_produk:
        if str(i) in df['SKU'].astype(str).values:
            SKU_Sing = str(df[df['SKU'].astype(str) == str(i)]['Kode'].values[0])
        elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
            SKU_Sing = str(df[str(i).lower() == df['Nama_Produk'].astype(str).str.lower()]['Kode'].values[0])
        list_SKU.append(SKU_Sing)
    dict_list = dict(zip(list_SKU, list_PCS))
    list_SKU = sorted_nicely(list_SKU)
    list_PCS = []
    for i in list_SKU:
        list_PCS.append(dict_list.get(i))
    for i in range(len(list_SKU)):
        if int(list_PCS[i]) > 1:
            list_SKU[i] = str(list_SKU[i]) + '(' + str(int(list_PCS[i])) + ')'
    SKU_Bundle = 'P'
    for i in list_SKU:
        SKU_Bundle = SKU_Bundle + i
    if len(list_produk) == 0:
        SKU_Bundle = 'P'
    if len(list_gimmick)!=0:
        for i in range(len(list_gimmick)):
            SKU_gim = ''
            if str(list_gimmick[i]) in df['SKU'].astype(str).values:
                SKU_gim = str(df[df['SKU'].astype(str) ==  str(list_gimmick[i])]['Kode'].values[0])
            elif str(list_gimmick[i]).lower() in df['Nama_Produk'].astype(str).str.lower().values:
                SKU_gim = str(df[str(list_gimmick[i]).lower() == df['Nama_Produk'].astype(str).str.lower()]['Kode'].values[0])
            if SKU_gim != '':
                if int(list_gimmick_qty[i]) > 1:
                    SKU_gim = str(SKU_gim) + '(' + str(list_gimmick_qty[i]) + ')'
                list_SKU_gim.append(SKU_gim)
    list_SKU_gim = sorted(list_SKU_gim, key=lambda x: int("".join([i for i in x if i.isdigit()])))
    for i in list_SKU_gim:
        SKU_Bundle = SKU_Bundle + i
    return SKU_Bundle

def updatesku():
    global df
    df_old = pd.read_excel(r'/home/tatanama/mastertatanama/data_SKU.xlsx', index = False)
    df_old = df_old.drop_duplicates(['SKU'])
    bundle = df[df['Brand'] == 'Bundle'].copy()
    df = df[df['Brand'] != 'Bundle']

    df = df.append(bundle, ignore_index = True, sort = False)
    df = df.reset_index(drop = True)

    list_alias = [x for x in df.columns if 'Alias' in x]
    list_organic = [x for x in df.columns if 'Organik' in x]
    not_alias = [x for x in df.columns if x not in list_alias and x not in list_organic]

    df_old.columns = [x.replace(' ', '_') for x in df_old.columns]
    list_url = [x for x in df_old.columns if 'URL' in str(x) and '1' not in str(x)]
    url_col = df_old[['SKU'] + list_url].copy()
    df_old = df_old[~df_old['SKU'].astype(str).isin(df['SKU'].astype(str))]
    df_old = df_old.append(df, ignore_index = True, sort = False)
    list_alias = [x for x in df_old.columns if 'Alias' in x]
    list_organic = [x for x in df_old.columns if 'Organik' in x]
    not_alias = [x for x in df_old.columns if x not in list_alias and x not in list_organic and x not in list_url]
    bundle = df_old[df_old['Brand'] == 'Bundle'].copy()
    df_old = df_old[df_old['Brand'] != 'Bundle']
    df_old = df_old.append(bundle, ignore_index = True, sort = False)
    df_old['SKU'] = df_old['SKU'].astype(str)
    url_col['SKU'] = url_col['SKU'].astype(str)
    temp = df_old.merge(url_col.drop_duplicates(['SKU']), how = 'left', on = 'SKU').set_index(df_old.index)
    for i in list_url:
        df_old[i] = df_old[i].fillna(temp[i + '_y'])
    list_used = not_alias[:not_alias.index('Harga_Cost_7')+1]
    list_notused = not_alias[not_alias.index('Harga_Cost_7')+1:]
    df_old = df_old.applymap(lambda x: pd.to_numeric(x, errors='ignore'))
    df_old[list_used].set_index(df_old.index).join([df_old[list_url].set_index(df_old.index), df_old[list_notused].set_index(df_old.index), df_old[list_alias].set_index(df_old.index)]).to_excel(r'/home/tatanama/mastertatanama/Master tatanama.xlsx', index = False)


@app.route('/', methods = ['GET', 'POST'])
def main():
    if 'user' in session:
        return redirect(url_for('search'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        if username == 'ecommerce' and password == 'ecommerce':
            session['user'] = True
            session['messages'] = 'Loggin Successfully'
            return redirect(url_for('search'))
        else :
            msg = 'Incorrect username or password'
            return render_template('home.html', msg = msg)
    return render_template('home.html')

@app.route('/Search', methods = ['GET', 'POST'])
def search():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    msg = ''
    global df
    df['Berat'] = pd.to_numeric(df['Berat'], errors = 'coerce').fillna(0)
    df['Volume'] = pd.to_numeric(df['Volume'], errors = 'coerce').fillna(0)
    df['Harga_Organik'] = pd.to_numeric(df['Harga_Organik'], errors = 'coerce').fillna(0)


    for i in range(1,8):
        df['Berat_' + str(i)] = pd.to_numeric(df['Berat_' + str(i)], errors = 'coerce').fillna(0)
        df['Volume_' + str(i)] = pd.to_numeric(df['Volume_' + str(i)], errors = 'coerce').fillna(0)
        df['Harga_Organik_' + str(i)] = pd.to_numeric(df['Harga_Organik_' + str(i)], errors = 'coerce').fillna(0)
    login = False
    if 'loggedin' in session:
        login = True
        if 'messages' in session:
            msg = session.pop('messages')
    if 'messages' in session:
       msg = session.pop('messages')
       updatesku()
    form = SearchForm(request.form)
    if request.method == "POST":
        form = SearchForm(request.form)
        result = request.form
        list_produk = []
        list_PCS = []
        # launch = result['launch']
        launch = "No"
        for keys in result:
            if 'produk' in keys:
                if str(result[keys]) != '':
                    list_produk.append(result[keys])
            elif 'PCS' in keys:
                if str(result[keys]) != '':
                    list_PCS.append(result[keys])
        if len(list_produk) == 0 or len(list_PCS) == 0:
            return render_template('search.html', form=form)
        list_PCS = [int(float(x)) for x in list_PCS]
        for i in list_produk:
            if i in df['SKU'].values:
                nama_produk = df[df['SKU'] == i]['Nama_Produk'].values[0]
                list_produk = [nama_produk if x == i else x for x in list_produk]
            elif i in df['Kode'].values:
                sku = df[df['Kode'] == i]['SKU'].values[0]
                nama_produk = df[df['SKU'] == sku]['Nama_Produk'].values[0]
                list_produk = [nama_produk if x == i else x for x in list_produk]
        # if launch == 'Yes':
        #     list_sku = []
        #     for i in list_produk:
        #         sku = df[df['Nama_Produk'] == i]['SKU'].values[0]
        #         list_sku.append(sku)
        #     table = pd.DataFrame({'list_sku' : list_sku, 'list_produk' : list_produk, 'list_PCS' : list_PCS})
        #     print(table)
        #     indeks = table[table['list_sku'].astype(str).str.contains('B')].index.to_list()
        #     for i in indeks:
        #         table['list_sku'][i] = table['list_sku'][i].replace('(B)', '')
        #         sku = table['list_sku'][i]
        #         nama_produk = df[df['SKU'] == sku]['Nama_Produk'].values[0]
        #         table['list_produk'][i] = nama_produk
        #     table = table.groupby(['list_sku', 'list_produk'])['list_PCS'].sum().reset_index()
        #     list_produk_launch = table['list_produk'].to_list()
        #     list_PCS_launch = table['list_PCS'].to_list()
        #     session['list_produk_launch'] = list_produk_launch
        #     session['list_PCS_launch'] = list_PCS_launch

        session['list_produk'] = list_produk
        session['list_PCS'] = list_PCS
        session['launch'] = launch
        list_produk_ori = list_produk.copy()
        list_PCS_ori = list_PCS.copy()
        dict_form = dict(zip(list_produk, list_PCS))
        found = False
        eksklusif = False
        dict_result = {}
        print(list_produk)
        if launch == 'Yes':
            sku_result = generate_SKU(list_produk, list_PCS)
            list_produk = list_produk_ori.copy()
            list_PCS = list_PCS_ori.copy()
            sku_result = sku_result.replace('P', 'C')
            if str(sku_result) in df['SKU'].astype(str).values:
                found = True
                i = df[df['SKU'].astype(str) == sku_result].index[0]
                dict_result['Nama_Produk'] = df['Nama_Produk'][i]
                dict_result['SKU'] = df['SKU'][i]
                dict_result['New_SKU'] = df['SKU_Generate'][i]
                dict_result['Price_List_NFI'] = int(float(df['Price_List_NFI'][i]))
                dict_result['Harga_Cost'] = int(float(df['Harga_Cost'][i]))
                dict_result['Harga_Display'] = int(float(df['Harga_Display'][i]))
                dict_result['Berat'] = float(df['Berat'][i])
                dict_result['Volume'] = float(df['Volume'][i])

                dict_result['MP_Eksklusif'] = df['MP_Eksklusif'][i]
                dict_result['MP_Tokopedia'] = df['MP_Tokopedia'][i]
                dict_result['MP_Shopee'] = df['MP_Shopee'][i]
                dict_result['MP_Lazada'] = df['MP_Lazada'][i]
                dict_result['MP_Blibli'] = df['MP_Blibli'][i]
                dict_result['MP_Jdid'] = df['MP_Jdid'][i]
                dict_result['MP_Bukalapak'] = df['MP_Bukalapak'][i]
                dict_result['MP_Nutrimart'] = df['MP_Nutrimart'][i]
                j = 1
                while j<=7:
                    colname = 'Produk_' + str(j)
                    if df[colname][i] != '' and df[colname][i] != None:
                        dict_result[colname] = df[colname][i]
                        dict_result['SKU_' + colname] = df['SKU_' + colname][i]
                        dict_result['PCS_' + colname] = int(float(df['PCS_' + colname][i]))
                        dict_result['Price_List_NFI_' + str(j)] = int(float(df['Price_List_NFI_' + str(j)][i]))
                        dict_result['Subtotal_' + colname] = int(float(df['Subtotal_' + colname][i]))
                        dict_result['Berat_' + str(j)] = float(df['Berat_' + str(j)][i])
                        dict_result['Volume_' + str(j)] = float(df['Volume_' + str(j)][i])
                    j = j+1
            else :
                    pass
        else :
            for i in range(df.shape[0]):
                if (df['Brand'][i] == 'Bundle') and ('C' not in df['SKU'][i]):
                    sql_produk = []
                    sql_sku = []
                    sql_pcs = []
                    if not found:
                        j = 1
                        colname = 'Produk_'
                        while j<=7:
                            if str(df[colname+str(j)][i]) != '':
                                if str(df[colname+str(j)][i]) != ' ':
                                    sql_produk.append(df[colname+str(j)][i])
                                    sql_sku.append(df['SKU_' + colname + str(j)][i])
                                    sql_pcs.append(df['PCS_'+colname+str(j)][i])
                            j = j+1
                        sql_pcs = [int(float(x)) for x in sql_pcs]
                        dict_produk = dict(zip(sql_produk, sql_pcs))
                        dict_sku = dict(zip(sql_sku, sql_pcs))
                        if dict_form == dict_produk or dict_sku == dict_form:
                            found = True
                            dict_result['Nama_Produk'] = df['Nama_Produk'][i]
                            dict_result['SKU'] = df['SKU'][i]
                            dict_result['New_SKU'] = df['SKU_Generate'][i]
                            dict_result['Price_List_NFI'] = int(float(df['Price_List_NFI'][i]))
                            dict_result['Harga_Cost'] = int(float(df['Harga_Cost'][i]))
                            dict_result['Harga_Display'] = int(float(df['Harga_Display'][i]))
                            dict_result['Berat'] = float(df['Berat'][i])
                            dict_result['Volume'] = float(df['Volume'][i])
                            dict_result['MP_Eksklusif'] = df['MP_Eksklusif'][i]
                            dict_result['MP_Tokopedia'] = df['MP_Tokopedia'][i]
                            dict_result['MP_Shopee'] = df['MP_Shopee'][i]
                            dict_result['MP_Lazada'] = df['MP_Lazada'][i]
                            dict_result['MP_Blibli'] = df['MP_Blibli'][i]
                            dict_result['MP_Jdid'] = df['MP_Jdid'][i]
                            dict_result['MP_Bukalapak'] = df['MP_Bukalapak'][i]
                            dict_result['MP_Nutrimart'] = df['MP_Nutrimart'][i]
                            j = 1
                            while j<=7:
                                colname = 'Produk_' + str(j)
                                if df[colname][i] != '':
                                    dict_result[colname] = df[colname][i]
                                    dict_result['SKU_' + colname] = df['SKU_' + colname][i]
                                    dict_result['PCS_' + colname] = int(float(df['PCS_' + colname][i]))
                                    dict_result['Price_List_NFI_' + str(j)] = int(float(df['Price_List_NFI_' + str(j)][i]))
                                    dict_result['Subtotal_' + colname] = int(float(df['Subtotal_' + colname][i]))
                                    dict_result['Berat_' + str(j)] = float(df['Berat_' + str(j)][i])
                                    dict_result['Volume_' + str(j)] = float(df['Volume_' + str(j)][i])
                                j = j+1
                else :
                    pass

        session['list_produk'] = list_produk
        session['list_PCS'] = list_PCS
        session['launch'] = launch

        if found:
            if dict_result['MP_Eksklusif'] != None:
                msg = 'Bundle ekslusif di ' + dict_result['MP_Eksklusif']
                return render_template('search.html', data = dict_result, form = form, login = login, msg = msg)
            else :
                session['dict_result_search'] = dict_result
                return redirect(url_for('add_MP'))
        return redirect(url_for('insert'))
    return render_template('search.html', form=form, msg = msg, login = login)

@app.route('/add_MP', methods = ['GET', 'POST'])
def add_MP():

    global df
    login = False
    if 'loggedin' in session:
        login = True
    dict_result_search = session.pop('dict_result_search')
    session['dict_result_search'] = dict_result_search
    list_MP = []
    for keys in dict_result_search:
        if 'MP_' in keys:
            if dict_result_search[keys] != '':
                if dict_result_search[keys] != None:
                    list_MP.append(keys.replace('MP_', ''))
    form = AddMPForm()
    if request.method == 'POST':
        result = request.form
        if result['submit_button'] == 'cancel':
            return redirect(url_for('search'))
        for keys in result:
            marketplace = result['mp']
        db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
        cursor = db.cursor()
        sql_arg = 'UPDATE data_sku SET MP_' + marketplace + ' = %s WHERE SKU = %s'
        cursor.execute(sql_arg, ['Yes', dict_result_search['SKU']])
        db.commit()
        query = "select * from data_sku"
        df = psql.read_sql(query, con = db)
        session['messages'] = 'Bundle Upload Successfully'
        return redirect(url_for('search'))
    if len(list_MP) == 0:
        return render_template('add_mp.html', data = dict_result_search, login = login, form = form)
    else :
        return render_template('add_mp.html', data = dict_result_search, login = login, form = form, list_MP = list_MP)


@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    global df
    login = False
    if 'loggedin' in session:
        login = True
    list_produk = session.pop('list_produk')
    list_produk_ori = list_produk.copy()
    list_PCS = session.pop('list_PCS')
    list_PCS_ori = list_PCS.copy()
    launch = session.pop('launch')
    session['launch'] = launch
    # if launch == 'Yes':
    #     list_produk_launch = session.pop('list_produk_launch')
    #     list_PCS_launch = session.pop('list_PCS_launch')
    #     session['list_produk_launch'] = list_produk_launch
    #     session['list_PCS_launch'] = list_PCS_launch
    sku_result = generate_SKU(list_produk, list_PCS)
    list_produk = list_produk_ori.copy()
    list_PCS = list_PCS_ori.copy()
    print(list_produk)
    print('sku_result : ', sku_result)

    if launch == 'Yes':
        # sku_result = generate_SKU(list_produk_launch, list_PCS_launch)
        sku_result = sku_result.replace('P', 'C')
        print('sku_result launch: ', sku_result)
    # else :
        # sku_result = generate_SKU(list_produk, list_PCS)
    dict_result = {}
    grand_total = 0
    harga_cost = 0
    harga_display = 0
    harga_organik = 0
    total_berat = 0
    total_volume = 0
    j = 1
    list_produk = list_produk_ori.copy()
    list_PCS = list_PCS_ori.copy()
    form = AddMPForm()
    session['list_produk'] = list_produk_ori
    session['list_PCS'] = list_PCS_ori
    df['Harga_Display'] = pd.to_numeric(df['Harga_Display'], errors = 'coerce').fillna(0)
    df['Harga_Cost'] = pd.to_numeric(df['Harga_Cost'], errors = 'coerce').fillna(0)
    df['Berat'] = pd.to_numeric(df['Berat'], errors = 'coerce').fillna(0)
    df['Volume'] = pd.to_numeric(df['Volume'], errors = 'coerce').fillna(0)
    for i in list_produk:
        if str(i) in df['SKU'].astype(str).values:
            indeks = df.loc[str(i) == df['SKU'].astype(str)].index[0]
        elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
            indeks = df.loc[str(i).lower() == df['Nama_Produk'].astype(str).str.lower()].index[0]
        colname = 'Produk_' + str(j)
        dict_result[colname] = df['Nama_Produk'][indeks]
        dict_result['SKU_' + colname] = df['SKU'][indeks]
        dict_result['PCS_' + colname] = list_PCS[j-1]
        dict_result['Price_List_NFI_' + str(j)] = df['Price_List_NFI'][indeks]
        dict_result['Subtotal_' + colname] = int(float(df['Price_List_NFI'][indeks])) * int(float(list_PCS[j-1]))
        dict_result['Harga_Cost_' + str(j)] = int(float(df['Harga_Cost'][indeks])) * int(float(list_PCS[j-1]))
        dict_result['Harga_Display_' + str(j)] = int(float(df['Harga_Display'][indeks])) * int(float(list_PCS[j-1]))
        dict_result['Harga_Organik_' + str(j)] = int(float(df['Harga_Organik'][indeks])) * int(float(list_PCS[j-1]))
        dict_result['Berat_' + str(j)] = float(df['Berat'][indeks]) * int(float(list_PCS[j-1]))
        dict_result['Volume_' + str(j)] = float(df['Volume'][indeks]) * int(float(list_PCS[j-1]))
        grand_total = grand_total + int(float(dict_result['Subtotal_' + colname]))
        harga_cost = harga_cost + int(float(dict_result['Harga_Cost_' + str(j)]))
        harga_display = harga_display + int(float(dict_result['Harga_Display_' + str(j)]))
        harga_organik = harga_organik + int(float(dict_result['Harga_Organik_' + str(j)]))
        total_berat = total_berat + float(dict_result['Berat_' + str(j)])
        total_volume = total_volume + float(dict_result['Volume_' + str(j)])
        j = j+1

    for i in range(j, 8):
        colname = 'Produk_' + str(i)
        dict_result[colname] = ''
        dict_result['SKU_' + colname] = ''
        dict_result['PCS_' + colname] = ''
        dict_result['Price_List_NFI_' + str(i)] = ''
        dict_result['Subtotal_' + colname] = ''
        dict_result['Harga_Cost_' + str(i)] = ''
        dict_result['Harga_Display_' + str(i)] = ''
        dict_result['Harga_Organik_' + str(i)] = ''
        dict_result['Berat_' + str(i)] = ''
        dict_result['Volume_' + str(i)] = ''

    dict_result['SKU'] = sku_result
    dict_result['Brand'] = 'Bundle'
    dict_result['Price_List_NFI'] = grand_total
    dict_result['Harga_Cost'] = harga_cost
    dict_result['Harga_Display'] = harga_display
    dict_result['Harga_Organik'] = harga_organik
    dict_result['Berat'] = total_berat
    dict_result['Volume'] = total_volume
    dict_result = dict((k, str(v)) for k,v in dict_result.items())

    if request.method == 'POST':
        print('Harga Display : ')
        print(harga_display)
        print('Harga Cost : ')
        print(harga_display)
        result = request.form
        if result['submit_button'] == 'cancel':
            return redirect(url_for('search'))
        nama_bundle = result['name']
        marketplace = result['mp']
        eksklusif = result['eksklusif']
        dict_result['Nama_Produk'] = nama_bundle
        sql_arg = "INSERT INTO data_sku (SKU, Nama_Produk, Brand, Price_List_NFI, Harga_Cost, Harga_Display, Harga_Organik, Berat, Volume, Produk_1, SKU_Produk_1, PCS_Produk_1, Price_List_NFI_1, Subtotal_Produk_1, Harga_Cost_1, Harga_Display_1, Harga_Organik_1, Berat_1, Volume_1, Produk_2, SKU_Produk_2, PCS_Produk_2, Price_List_NFI_2, Subtotal_Produk_2, Harga_Cost_2, Harga_Display_2, Harga_Organik_2, Berat_2, Volume_2,Produk_3, SKU_Produk_3, PCS_Produk_3, Price_List_NFI_3, Subtotal_Produk_3, Harga_Cost_3, Harga_Display_3, Harga_Organik_3,Berat_3, Volume_3, Produk_4, SKU_Produk_4, PCS_Produk_4, Price_List_NFI_4, Subtotal_Produk_4, Harga_Cost_4, Harga_Display_4, Harga_Organik_4,Berat_4, Volume_4, Produk_5, SKU_Produk_5, PCS_Produk_5, Price_List_NFI_5, Subtotal_Produk_5, Harga_Cost_5, Harga_Display_5, Harga_Organik_5,Berat_5, Volume_5, Produk_6, SKU_Produk_6, PCS_Produk_6, Price_List_NFI_6, Subtotal_Produk_6, Harga_Cost_6, Harga_Display_6, Harga_Organik_6, Berat_6, Volume_6,Produk_7, SKU_Produk_7, PCS_Produk_7, Price_List_NFI_7, Subtotal_Produk_7, Harga_Cost_7, Harga_Display_7, Harga_Organik_7,Berat_7, Volume_7, SKU_Generate"
        list_sql_arg = [dict_result['SKU'], dict_result['Nama_Produk'], dict_result['Brand'], dict_result['Price_List_NFI'], dict_result['Harga_Cost'], dict_result['Harga_Display'], dict_result['Harga_Organik'],dict_result['Berat'],dict_result['Volume'], dict_result['Produk_1'], dict_result['SKU_Produk_1'], dict_result['PCS_Produk_1'], dict_result['Price_List_NFI_1'], dict_result['Subtotal_Produk_1'], dict_result['Harga_Cost_1'], dict_result['Harga_Display_1'], dict_result['Harga_Organik_1'], dict_result['Berat_1'], dict_result['Volume_1'], dict_result['Produk_2'], dict_result['SKU_Produk_2'], dict_result['PCS_Produk_2'], dict_result['Price_List_NFI_2'], dict_result['Subtotal_Produk_2'], dict_result['Harga_Cost_2'], dict_result['Harga_Display_2'], dict_result['Harga_Organik_2'], dict_result['Berat_2'], dict_result['Volume_2'],dict_result['Produk_3'], dict_result['SKU_Produk_3'], dict_result['PCS_Produk_3'], dict_result['Price_List_NFI_3'], dict_result['Subtotal_Produk_3'], dict_result['Harga_Cost_3'], dict_result['Harga_Display_3'], dict_result['Harga_Organik_3'], dict_result['Berat_3'], dict_result['Volume_3'], dict_result['Produk_4'], dict_result['SKU_Produk_4'], dict_result['PCS_Produk_4'], dict_result['Price_List_NFI_4'], dict_result['Subtotal_Produk_4'], dict_result['Harga_Cost_4'], dict_result['Harga_Display_4'], dict_result['Harga_Organik_4'], dict_result['Berat_4'], dict_result['Volume_4'], dict_result['Produk_5'], dict_result['SKU_Produk_5'], dict_result['PCS_Produk_5'], dict_result['Price_List_NFI_5'], dict_result['Subtotal_Produk_5'], dict_result['Harga_Cost_5'], dict_result['Harga_Display_5'], dict_result['Harga_Organik_5'], dict_result['Berat_5'], dict_result['Volume_5'], dict_result['Produk_6'], dict_result['SKU_Produk_6'], dict_result['PCS_Produk_6'], dict_result['Price_List_NFI_6'], dict_result['Subtotal_Produk_6'], dict_result['Harga_Cost_6'], dict_result['Harga_Display_6'], dict_result['Harga_Organik_6'], dict_result['Berat_6'], dict_result['Volume_6'], dict_result['Produk_7'], dict_result['SKU_Produk_7'], dict_result['PCS_Produk_7'], dict_result['Price_List_NFI_7'], dict_result['Subtotal_Produk_7'], dict_result['Harga_Cost_7'], dict_result['Harga_Display_7'], dict_result['Harga_Organik_7'], dict_result['Berat_7'], dict_result['Volume_7'], dict_result['SKU']]
        if eksklusif == 'Eksklusif':
            sql_arg = sql_arg + ', MP_' + marketplace + ', MP_Eksklusif'
            sql_arg = sql_arg + ') Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s, %s,%s,%s,%s)'
            list_sql_arg.append('Yes')
            list_sql_arg.append(marketplace)
        else :
            sql_arg = sql_arg + ', MP_' + marketplace
            sql_arg = sql_arg + ') Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s)'
            list_sql_arg.append('Yes')
        db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
        cursor = db.cursor()
        cursor.execute(sql_arg, list_sql_arg)
        db.commit()
        query = "select * from data_sku"
        df = psql.read_sql(query, con = db)
        global list_all
        list_all = df['Nama_Produk'].to_list()
        session['messages'] = 'Bundle Uploadaded Successfully'
        return redirect(url_for('search'))
    return render_template('insert.html', data = dict_result, login = login, form = form)

@app.route('/add_single', methods = ['GET', 'POST'])
def add_single():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    form = AddForm(request.form)
    if 'loggedin' in session:
        form = AddForm(request.form)
        if request.method == "POST":
            db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
            cursor = db.cursor()
            result = request.form
            nama  = result['name']
            sku = result['sku']
            brand = result['brand']
            nfi = result['nfi']
            cost = result['cost']
            display = result['display']
            code = result['code']
            organik = result['organik']
            parent = result['parent']
            subbrand = result['sub']
            berat = result['berat']
            volume = result['volume']
            nama_oracle = result['nama_oracle']
            cursor.execute("INSERT INTO data_sku (SKU, Nama_Produk, Brand, Price_List_NFI, Harga_Cost, Harga_Display, Kode, Harga_Organik, Parent_Item, Sub_Brand, Nama_Oracle, Berat, Volume) Values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [sku, nama, brand, nfi, cost, display, code, organik, parent, subbrand, nama_oracle, berat, volume])
            db.commit()
            session['messages'] = 'Adding Product Successful'
            query = "select * from data_sku"
            global df
            df = psql.read_sql(query, con = db)
            global list_auto
            list_auto = []
            list_auto = list_auto + df[df['Brand']!='Bundle']['SKU'].to_list()
            list_auto = list_auto + df[df['Brand']!='Bundle']['Nama_Produk'].to_list()
            return redirect(url_for('search'))
        return render_template('add_single.html', form = form)
    return redirect(url_for('main'))

@app.route('/edit_single', methods=['GET', 'POST'])
def edit_single():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    form = SearchSingle(request.form)
    global df
    if request.method == 'POST':
        result = request.form
        for keys in result:
            if 'produk' in keys:
                produk = result[keys]
        if str(produk) in df['Nama_Produk'].astype(str).values:
            indeks = df[df['Nama_Produk'] == produk].index[0]
        elif str(produk) in df['Kode'].values:
            indeks = df[df['Kode'] == produk].index[0]
        else :
            indeks = df[df['SKU'].astype(str) == str(produk)].index[0]
        parent_name = df['Parent_Item'][indeks]
        parent_sku = df['Parent_SKU'][indeks]
        name = df['Nama_Produk'][indeks]
        sku = df['SKU'][indeks]
        brand = df['Brand'][indeks]
        nfi = df['Price_List_NFI'][indeks]
        cost = df['Harga_Cost'][indeks]
        display = df['Harga_Display'][indeks]
        code = df['Kode'][indeks]
        organik = df['Harga_Organik'][indeks]
        nama_oracle = df['Nama_Oracle'][indeks]
        berat = df['Berat'][indeks]
        volume = df['Volume'][indeks]
        dict_result = {'Parent Name' : parent_name, 'Parent SKU' : parent_sku, 'Name' : name, 'SKU':sku, 'Brand':brand, 'NFI' : nfi, 'Cost' : cost, 'Display' : display, 'Organik' : organik, 'Code' : code, 'Nama_Oracle' : nama_oracle, 'Berat' : berat, 'Volume':volume}
        session['dict_result_edit'] = dict_result
        return redirect(url_for('insert_edit_single'))
    return render_template('edit_single.html', form = form)

@app.route('/insert_edit_single', methods=['GET', 'POST'])
def insert_edit_single():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    global df
    dict_result = session.pop('dict_result_edit')
    session['dict_result_edit'] = dict_result
    form = AddForm(request.form, brand = dict_result['Brand'])
    if request.method == 'POST':
        result = request.form
        name  = result['name']
        sku = result['sku']
        nfi = int(result['nfi'])
        cost = int(result['cost'])
        display = int(result['display'])
        organik = result['organik']
        code = result['code']
        brand = result['brand']
        nama_oracle = result['nama_oracle']
        berat = result['berat']
        volume = result['volume']
        db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
        cursor = db.cursor()
        print(dict_result['Name'])
        if dict_result['Name'] == name:
            cursor.execute('UPDATE data_sku SET Nama_Produk = %s, SKU = %s, Price_List_NFI = %s, Harga_Cost = %s, Harga_Display = %s, Kode = %s, Harga_Organik = %s, Brand = %s, Nama_Oracle = %s, Berat = %s, Volume = %s WHERE Nama_Produk = %s', [name, sku, nfi, cost, display, code, organik, brand, nama_oracle, berat, volume, name])
            db.commit()
            cursor.execute('UPDATE data_sku SET Produk_1 = %s, SKU_Produk_1 = %s, Price_List_NFI_1 = %s, Harga_Cost_1 = %s, Harga_Display_1 = %s, Harga_Organik_1 = %s, Berat_1 = %s, Volume_1 = %s WHERE Produk_1 = %s', [name, sku, nfi, cost, display, organik, berat, volume, name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_1 = CAST(Price_List_NFI_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_1 = CAST(Harga_Cost_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_1 = CAST(Harga_Display_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [name])
            db.commit()
            cursor.execute('UPDATE data_sku SET Berat_1 = Berat_1 * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_1 = Volume_1 * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_2 = %s, SKU_Produk_2 = %s, Price_List_NFI_2 = %s, Harga_Cost_2 = %s, Harga_Display_2 = %s, Harga_Organik_2 = %s, Berat_2 = %s, Volume_2 = %s WHERE Produk_2 = %s', [name, sku, nfi, cost, display, organik,berat, volume, name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_2 = CAST(Price_List_NFI_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_2 = CAST(Harga_Cost_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_2 = CAST(Harga_Display_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_2 = Berat_2 * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_2 = Volume_2 * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_3 = %s, SKU_Produk_3 = %s, Price_List_NFI_3 = %s, Harga_Cost_3 = %s, Harga_Display_3 = %s, Harga_Organik_3 = %s, Berat_3 = %s, Volume_3 = %s WHERE Produk_3 = %s', [name, sku, nfi, cost, display, organik,berat, volume, name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_3 = CAST(Price_List_NFI_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_3 = CAST(Harga_Cost_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_3 = CAST(Harga_Display_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_3 = Berat_3 * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_3 = Volume_3 * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_4 = %s, SKU_Produk_4 = %s, Price_List_NFI_4 = %s, Harga_Cost_4 = %s, Harga_Display_4 = %s, Harga_Organik_4 = %s, Berat_4 = %s, Volume_4 = %s WHERE Produk_4 = %s', [name, sku, nfi, cost, display, organik, berat, volume,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_4 = CAST(Price_List_NFI_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_4 = CAST(Harga_Cost_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_4 = CAST(Harga_Display_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_4 = Berat_4 * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_4 = Volume_4 * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_5 = %s, SKU_Produk_5 = %s, Price_List_NFI_5 = %s, Harga_Cost_5 = %s, Harga_Display_5 = %s, Harga_Organik_5 = %s, Berat_5 = %s, Volume_5 = %s WHERE Produk_5 = %s', [name, sku, nfi, cost, display, organik, berat, volume,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_5 = CAST(Price_List_NFI_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_5 = CAST(Harga_Cost_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_5 = CAST(Harga_Display_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_5 = Berat_5 * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_5 = Volume_5 * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_6 = %s, SKU_Produk_6 = %s, Price_List_NFI_6 = %s, Harga_Cost_6 = %s, Harga_Display_6 = %s, Harga_Organik_6 = %s, Berat_6 = %s, Volume_6 = %s WHERE Produk_6 = %s', [name, sku, nfi, cost, display, organik,berat, volume, name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_6 = CAST(Price_List_NFI_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_6 = CAST(Harga_Cost_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_6 = CAST(Harga_Display_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_6 = Berat_6 * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_6 = Volume_6 * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_7 = %s, SKU_Produk_7 = %s, Price_List_NFI_7 = %s, Harga_Cost_7 = %s, Harga_Display_7 = %s, Harga_Organik_7 = %s, Berat_7 = %s, Volume_7 = %s WHERE Produk_7 = %s', [name, sku, nfi, cost, display, organik,berat, volume, name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_7 = CAST(Price_List_NFI_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Price_List_NFI = Subtotal_Produk_1 + Subtotal_Produk_2 + Subtotal_Produk_3 + Subtotal_Produk_4 + Subtotal_Produk_5 + Subtotal_Produk_6 + Subtotal_Produk_7 Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_7 = CAST(Harga_Cost_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_7 = CAST(Harga_Display_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_7 = Berat_7 * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_7 = Volume_7 * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [name])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost = Harga_Cost_1 + Harga_Cost_2  + Harga_Cost_3 + Harga_Cost_4  + Harga_Cost_5 + Harga_Cost_6  + Harga_Cost_7  Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display = Harga_Display_1  + Harga_Display_2  + Harga_Display_3  + Harga_Display_4  + Harga_Display_5  + Harga_Display_6+ Harga_Display_7 Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor.execute('UPDATE data_sku SET Berat = Berat_1 + Berat_2  + Berat_3 + Berat_4  + Berat_5 + Berat_6  + Berat_7  Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume = Volume_1  + Volume_2  + Volume_3  + Volume_4  + Volume_5  + Volume_6+ Volume_7 Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()

        else :
            db.set_character_set('utf8')

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Nama_Produk = %s, SKU = %s, Price_List_NFI = %s, Harga_Cost = %s, Harga_Display = %s, Kode = %s, Harga_Organik = %s, Brand = %s, Nama_Oracle = %s, Berat = %s, Volume = %s WHERE Nama_Produk = %s', [name, sku, nfi, cost, display, code, organik, brand, nama_oracle, berat, volume, dict_result['Name']])
            db.commit()
            cursor.execute('UPDATE data_sku SET Produk_1 = %s, SKU_Produk_1 = %s, Price_List_NFI_1 = %s, Harga_Cost_1 = %s, Harga_Display_1 = %s, Harga_Organik_1 = %s, Berat_1 = %s, Volume_1 = %s WHERE Produk_1 = %s', [name, sku, nfi, cost, display, organik, berat, volume, dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_1 = CAST(Price_List_NFI_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_1 = CAST(Harga_Cost_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_1 = CAST(Harga_Display_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [dict_result['Name']])
            db.commit()
            cursor.execute('UPDATE data_sku SET Berat_1 = Berat_1 * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_1 = Volume_1 * CAST(PCS_Produk_1 AS UNSIGNED) WHERE Produk_1 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_2 = %s, SKU_Produk_2 = %s, Price_List_NFI_2 = %s, Harga_Cost_2 = %s, Harga_Display_2 = %s, Harga_Organik_2 = %s, Berat_2 = %s, Volume_2 = %s WHERE Produk_2 = %s', [name, sku, nfi, cost, display, organik,berat, volume, dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_2 = CAST(Price_List_NFI_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_2 = CAST(Harga_Cost_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_2 = CAST(Harga_Display_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_2 = Berat_2 * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_2 = Volume_2 * CAST(PCS_Produk_2 AS UNSIGNED) WHERE Produk_2 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_3 = %s, SKU_Produk_3 = %s, Price_List_NFI_3 = %s, Harga_Cost_3 = %s, Harga_Display_3 = %s, Harga_Organik_3 = %s, Berat_3 = %s, Volume_3 = %s WHERE Produk_3 = %s', [name, sku, nfi, cost, display, organik,berat, volume, dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_3 = CAST(Price_List_NFI_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_3 = CAST(Harga_Cost_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_3 = CAST(Harga_Display_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_3 = Berat_3 * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_3 = Volume_3 * CAST(PCS_Produk_3 AS UNSIGNED) WHERE Produk_3 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_4 = %s, SKU_Produk_4 = %s, Price_List_NFI_4 = %s, Harga_Cost_4 = %s, Harga_Display_4 = %s, Harga_Organik_4 = %s, Berat_4 = %s, Volume_4 = %s WHERE Produk_4 = %s', [name, sku, nfi, cost, display, organik, berat, volume,dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_4 = CAST(Price_List_NFI_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_4 = CAST(Harga_Cost_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_4 = CAST(Harga_Display_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_4 = Berat_4 * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_4 = Volume_4 * CAST(PCS_Produk_4 AS UNSIGNED) WHERE Produk_4 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_5 = %s, SKU_Produk_5 = %s, Price_List_NFI_5 = %s, Harga_Cost_5 = %s, Harga_Display_5 = %s, Harga_Organik_5 = %s, Berat_5 = %s, Volume_5 = %s WHERE Produk_5 = %s', [name, sku, nfi, cost, display, organik, berat, volume,dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_5 = CAST(Price_List_NFI_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_5 = CAST(Harga_Cost_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_5 = CAST(Harga_Display_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_5 = Berat_5 * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_5 = Volume_5 * CAST(PCS_Produk_5 AS UNSIGNED) WHERE Produk_5 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_6 = %s, SKU_Produk_6 = %s, Price_List_NFI_6 = %s, Harga_Cost_6 = %s, Harga_Display_6 = %s, Harga_Organik_6 = %s, Berat_6 = %s, Volume_6 = %s WHERE Produk_6 = %s', [name, sku, nfi, cost, display, organik,berat, volume, dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_6 = CAST(Price_List_NFI_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_6 = CAST(Harga_Cost_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_6 = CAST(Harga_Display_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_6 = Berat_6 * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_6 = Volume_6 * CAST(PCS_Produk_6 AS UNSIGNED) WHERE Produk_6 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Produk_7 = %s, SKU_Produk_7 = %s, Price_List_NFI_7 = %s, Harga_Cost_7 = %s, Harga_Display_7 = %s, Harga_Organik_7 = %s, Berat_7 = %s, Volume_7 = %s WHERE Produk_7 = %s', [name, sku, nfi, cost, display, organik,berat, volume, dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Subtotal_Produk_7 = CAST(Price_List_NFI_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Price_List_NFI = Subtotal_Produk_1 + Subtotal_Produk_2 + Subtotal_Produk_3 + Subtotal_Produk_4 + Subtotal_Produk_5 + Subtotal_Produk_6 + Subtotal_Produk_7 Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost_7 = CAST(Harga_Cost_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_7 = CAST(Harga_Display_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Berat_7 = Berat_7 * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [dict_result['Name']])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume_7 = Volume_7 * CAST(PCS_Produk_7 AS UNSIGNED) WHERE Produk_7 = %s', [dict_result['Name']])
            db.commit()

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Cost = Harga_Cost_1 + Harga_Cost_2  + Harga_Cost_3 + Harga_Cost_4  + Harga_Cost_5 + Harga_Cost_6  + Harga_Cost_7  Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display = Harga_Display_1  + Harga_Display_2  + Harga_Display_3  + Harga_Display_4  + Harga_Display_5  + Harga_Display_6+ Harga_Display_7 Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor.execute('UPDATE data_sku SET Berat = Berat_1 + Berat_2  + Berat_3 + Berat_4  + Berat_5 + Berat_6  + Berat_7  Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Volume = Volume_1  + Volume_2  + Volume_3  + Volume_4  + Volume_5  + Volume_6+ Volume_7 Where Brand = %s and (Produk_1 = %s or Produk_2 = %s or Produk_3 = %s or Produk_4 = %s or Produk_5 = %s or Produk_6 = %s or Produk_7 = %s)', ['Bundle',name,name,name,name,name,name,name])
            db.commit()


        df = psql.read_sql(query, con = db)
        if code != dict_result['Code']:
            list_col_pcs = [x for x in df.columns if 'PCS_Produk_' in x]
            indeks = df[df['Brand'] == 'Bundle'].index.to_list()
            for i in indeks:
                list_produk = []
                list_pcs = []
                for j in list_col_pcs:
                    if str(df[j.replace('PCS_', '')][i]).lower() == str(name).lower():
                        for k in list_col_pcs:
                            if str(df[k.replace('PCS_', '')][i]) != '':
                                if str(df[k.replace('PCS_', '')][i]) != ' ':
                                    list_produk.append(df[k.replace('PCS_', '')][i])
                                    list_pcs.append(df[k][i])
                        sku_baru = generate_SKU(list_produk, list_pcs)
                        nama_bundle = df['Nama_Produk'][i]
                        cursor.execute('UPDATE data_sku SET SKU = %s Where Nama_Produk = %s', [sku_baru, nama_bundle])
                        print(nama_bundle)
                        db.commit()

        session['messages'] = 'Edit Data Successful'
        df = psql.read_sql(query, con = db)
        global list_auto
        list_auto = []
        list_auto = list_auto + df[df['Brand']!='Bundle']['SKU'].to_list()
        list_auto = list_auto + df[df['Brand']!='Bundle']['Nama_Produk'].to_list()
        global list_all
        list_all = df['Nama_Produk'].to_list()
        return redirect(url_for('search'))
    return render_template('edit_single.html', form = form, parent_name = dict_result['Parent Name'], parent_sku = dict_result['Parent SKU'], name = dict_result['Name'], sku = dict_result['SKU'], nfi = dict_result['NFI'], cost = dict_result['Cost'], display = dict_result['Display'], code = dict_result['Code'], organik = dict_result['Organik'], brand = dict_result['Brand'], berat = dict_result['Berat'], volume = dict_result['Volume'], nama_oracle = dict_result['Nama_Oracle'])


@app.route('/add_alias', methods=['GET', 'POST'])
def add_alias():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    login = False
    if 'loggedin' in session:
        login = True
    form = SearchSingle(request.form)
    global df
    if request.method == 'POST':
        result = request.form
        for keys in result:
            if 'produk' in keys:
                produk = result[keys]
        if str(produk) in df['Nama_Produk'].astype(str).values:
            indeks = df[df['Nama_Produk'] == produk].index[0]
            session['indeks'] = int(indeks)
        else :
            indeks = df[df['SKU'].astype(str) == str(produk)].index[0]
            session['indeks'] = int(indeks)
        dict_result = {}
        alias_nama = [x for x in df.columns if 'Alias_Nama' in x]
        for i in alias_nama:
            dict_result[i] = df[i][indeks]
            dict_result[i.replace('Nama', 'SKU')] = df[i.replace('Nama', 'SKU')][indeks]
        session['dict_result_alias'] = dict_result
        return redirect(url_for('insert_alias'))
    return render_template('edit_alias.html', form = form, login = login)

@app.route('/insert_alias', methods=['GET', 'POST'])
def insert_alias():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    login = False
    if 'loggedin' in session:
        login = True
    global df
    indeks = session.pop('indeks')
    session['indeks'] = indeks
    dict_result = session.pop('dict_result_alias')
    session['dict_result_alias'] = dict_result
    form = AliasForm(request.form)
    if request.method == 'POST':
        result = request.form
        name  = result['name']
        sku = result['sku']
        db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
        cursor = db.cursor()
        null_col = False
        alias_name = [x for x in df.columns if 'Alias_Nama' in x]
        for i in alias_name:
            if not null_col:
                if str(df[i][indeks]) == '' or str(df[i][indeks]) == 'nan' or df[i][indeks] == None:
                    null_col = True
                    null_name = i
                    null_sku = i.replace('Nama', 'SKU')
        if null_col :
            nama_single = df['Nama_Produk'][indeks]
            sql_arg = 'UPDATE data_sku SET ' + null_name + ' = %s, ' + null_sku + ' = %s WHERE Nama_Produk = %s'
            cursor.execute(sql_arg, [name, sku, nama_single])
            db.commit()
        else :
            nama_single = df['Nama_Produk'][indeks]
            null_name = 'Alias_Nama_' + str(len(alias_name) + 1)
            null_sku = null_name.replace('Nama', 'SKU')
            sql_arg = 'ALTER TABLE data_sku ADD ' + null_name + ' VARCHAR (255), ADD ' + null_sku + ' VARCHAR (255)'
            cursor.execute(sql_arg)
            db.commit()
            sql_arg = 'UPDATE data_sku SET ' + null_name + ' = %s, ' + null_sku + ' = %s WHERE Nama_Produk = %s'
            cursor.execute(sql_arg, [name, sku, nama_single])
            db.commit()
        query = "select * from data_sku"
        df = psql.read_sql(query, con = db)
        session['messages'] = 'Edit Alias Data Successful'
        return redirect(url_for('search'))
    return render_template('edit_alias.html', login = login, form = form, data = dict_result, kond = True, len = len(dict_result) + 1, name = df['Nama_Produk'][indeks], sku = df['SKU'][indeks])

@app.route('/download')
def download():
    updatesku()
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    global df
    db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
    query = "select * from data_sku"
    df = psql.read_sql(query, con = db)
    # df_old = pd.read_excel(r'/home/tatanama/mastertatanama/data_SKU.xlsx', index = False)
    # df_old = df_old.drop_duplicates(['SKU'])
    # bundle = df[df['Brand'] == 'Bundle'].copy()
    # bundle = bundle.reset_index(drop = True)
    # df = df[df['Brand'] != 'Bundle']

    # for i in range(idx, idx+1):
    #     price_list_nfi = 0
    #     harga_cost = 0
    #     harga_display = 0
    #     harga_organik = 0
    #     dict_result = {}
    #     print(bundle['SKU'][i])
    #     for j in range(1,8):
    #         colname = 'Produk_' + str(j)
    #         if bundle['SKU_' + colname][i] != None and str(bundle['SKU_' + colname][i]) != '':
    #             print(str(bundle['SKU_' + colname][i]))
    #             indeks = df[str(bundle['SKU_' + colname][i]) == df['SKU'].astype(str)].index[0]
    #             dict_result['Price_List_NFI_' + str(j)] = df['Price_List_NFI'][indeks]
    #             dict_result['Subtotal_' + colname] = int(float(df['Price_List_NFI'][indeks])) * int(float(bundle['PCS_' + colname][i]))
    #             print(int(float(df['Harga_Cost'][indeks])))
    #             print(int(float(bundle['PCS_' + colname][i])))
    #             dict_result['Harga_Cost_' + str(j)] = int(float(df['Harga_Cost'][indeks])) * int(float(bundle['PCS_' + colname][i]))
    #             print(dict_result['Harga_Cost_' + str(j)])
    #             if df['Harga_Display'][indeks] == 'x':
    #                 dict_result['Harga_Display_' + str(j)] = 0
    #             else :
    #                 dict_result['Harga_Display_' + str(j)] = int(float(df['Harga_Display'][indeks])) * int(float(bundle['PCS_' + colname][i]))
    #             dict_result['Harga_Organik_' + str(j)] = int(float(df['Harga_Organik'][indeks])) * int(float(bundle['PCS_' + colname][i]))
    #             price_list_nfi = price_list_nfi + int(float(dict_result['Subtotal_' + colname]))
    #             harga_cost = harga_cost + int(float(dict_result['Harga_Cost_' + str(j)]))
    #             harga_display = harga_display + int(float(dict_result['Harga_Display_' + str(j)]))
    #             harga_organik = harga_organik + int(float(dict_result['Harga_Organik_' + str(j)]))
    #         else :
    #             dict_result['Price_List_NFI_' + str(j)] = 0
    #             dict_result['Subtotal_' + colname] = 0
    #             dict_result['Harga_Cost_' + str(j)] = 0
    #             dict_result['Harga_Display_' + str(j)] = 0
    #             dict_result['Harga_Organik_' + str(j)] = 0
    #     cursor = db.cursor()
    #     cursor.execute('Update data_sku set Price_List_NFI = %s, Harga_Cost = %s, Harga_Display = %s, Harga_Organik = %s, Price_List_NFI_1 = %s, Harga_Cost_1 = %s, Harga_Display_1 = %s, Harga_Organik_1 = %s, Price_List_NFI_2 = %s, Harga_Cost_2 = %s, Harga_Display_2 = %s, Harga_Organik_2 = %s, Price_List_NFI_3 = %s, Harga_Cost_3 = %s, Harga_Display_3 = %s, Harga_Organik_3 = %s, Price_List_NFI_4 = %s, Harga_Cost_4 = %s, Harga_Display_4 = %s, Harga_Organik_4 = %s, Price_List_NFI_5 = %s, Harga_Cost_5 = %s, Harga_Display_5 = %s, Harga_Organik_5 = %s, Price_List_NFI_6 = %s, Harga_Cost_6 = %s, Harga_Display_6 = %s, Harga_Organik_6 = %s, Price_List_NFI_7 = %s, Harga_Cost_7 = %s, Harga_Display_7 = %s, Harga_Organik_7 = %s, Subtotal_Produk_1 = %s, Subtotal_Produk_2 = %s, Subtotal_Produk_3 = %s, Subtotal_Produk_4 = %s, Subtotal_Produk_5 = %s, Subtotal_Produk_6 = %s, Subtotal_Produk_7 = %s Where SKU = %s', [price_list_nfi, harga_cost, harga_display, harga_organik, dict_result['Price_List_NFI_1'], dict_result['Harga_Cost_1'], dict_result['Harga_Display_1'], dict_result['Harga_Organik_1'],dict_result['Price_List_NFI_2'], dict_result['Harga_Cost_2'], dict_result['Harga_Display_2'], dict_result['Harga_Organik_2'],dict_result['Price_List_NFI_3'], dict_result['Harga_Cost_3'], dict_result['Harga_Display_3'], dict_result['Harga_Organik_3'],dict_result['Price_List_NFI_4'], dict_result['Harga_Cost_4'], dict_result['Harga_Display_4'], dict_result['Harga_Organik_4'],dict_result['Price_List_NFI_5'], dict_result['Harga_Cost_5'], dict_result['Harga_Display_5'], dict_result['Harga_Organik_5'],dict_result['Price_List_NFI_6'], dict_result['Harga_Cost_6'], dict_result['Harga_Display_6'], dict_result['Harga_Organik_6'],dict_result['Price_List_NFI_7'], dict_result['Harga_Cost_7'], dict_result['Harga_Display_7'], dict_result['Harga_Organik_7'], dict_result['Subtotal_Produk_1'], dict_result['Subtotal_Produk_2'],dict_result['Subtotal_Produk_3'],dict_result['Subtotal_Produk_4'],dict_result['Subtotal_Produk_5'],dict_result['Subtotal_Produk_6'],dict_result['Subtotal_Produk_7'], bundle['SKU'][i]])
    #     db.commit()

    # df['SKU'] = df['SKU'].astype(str)
    # df_old['SKU'] = df_old['SKU'].astype(str)

    # temp = df.merge(df_old[['SKU', 'Harga Cost', 'Harga Display']], how = 'left', on ='SKU').set_index(df.index)
    # df['Harga_Cost'] = temp['Harga Cost']
    # df['Harga_Display'] = temp['Harga Display']
    # df['Harga_Cost'] = df['Harga_Cost'].fillna('0')
    # df['Harga_Display'] = df['Harga_Display'].fillna('0')

    # for i in df.index:
    #     cursor.execute('UPDATE data_sku SET Harga_Cost = %s, Harga_Display = %s WHERE SKU = %s', [df['Harga_Cost'][i], df['Harga_Display'][i], df['SKU'][i]])
    #     db.commit()
    # df = df.append(bundle, ignore_index = True, sort = False)
    # df = df.reset_index(drop = True)
    # indeks = df[df['SKU'].astype(str) == '2101468P2'].index[0]


    # indeks = df[df['Brand'] == 'Bundle'].index.to_list()
    # for i in indeks:
    #     cursor = db.cursor()
    #     idx1 = df[df['SKU'].astype(str) == str(df['SKU_Produk_1'][i])].index.to_list()
    #     if len(idx1)>0:
    #         if df['Harga_Cost'][idx1[0]] == 'x':
    #             df['Harga_Cost_1'][i] = 0
    #         else :
    #             df['Harga_Cost_1'][i] = int(float(df['Harga_Cost'][idx1[0]])) * int(df['PCS_Produk_1'][i])
    #         if df['Harga_Display'][idx1[0]] == 'x':
    #             df['Harga_Display_1'][i] = 0
    #         else :
    #             df['Harga_Display_1'][i] = int(df['Harga_Display'][idx1[0]]) * int(df['PCS_Produk_1'][i])
    #     idx2 = df[df['SKU'].astype(str) == str(df['SKU_Produk_2'][i])].index.to_list()
    #     if len(idx2)>0:
    #         df['Harga_Cost_2'][i] = int(df['Harga_Cost'][idx2[0]]) * int(df['PCS_Produk_2'][i])
    #         df['Harga_Display_2'][i] = int(df['Harga_Display'][idx2[0]]) * int(df['PCS_Produk_2'][i])
    #     else :
    #         df['Harga_Cost_2'][i] = 0
    #         df['Harga_Display_2'][i] = 0
    #     df['Harga_Cost'][i] = int(float(df['Harga_Cost_1'][i])) + int(float(df['Harga_Cost_2'][i]))
    #     df['Harga_Display'][i] = int(df['Harga_Display_1'][i]) + int(df['Harga_Display_2'][i])
    #     cursor.execute('UPDATE data_sku SET Harga_Cost = %s, Harga_Display = %s, Harga_Display_1 = %s, Harga_Cost_1 = %s, Harga_Display_2 = %s, Harga_Cost_2 = %s WHERE SKU = %s', [df['Harga_Cost'][i], df['Harga_Display'][i], df['Harga_Cost_1'][i], df['Harga_Display_1'][i], df['Harga_Cost_2'][i], df['Harga_Display_2'][i],df['SKU'][i]])
    #     db.commit()

    pd.DataFrame(list_auto).to_excel('List Auto.xlsx', index = False)
    pd.DataFrame(list_all).to_excel('List All.xlsx', index = False)
    df_printed = df[df['Brand'] != 'Partnership']
    if 'Active' not in df_printed.columns:
        df_printed['Active'] = 'Active'
        indeks = df_printed[df_printed['SKU'].isin(list_hide)].index.to_list()
        df_printed['Active'][indeks] = 'Inactive'

    list_alias = [x for x in df_printed.columns if 'Alias' in x]
    list_organic = [x for x in df_printed.columns if 'Organik' in x]
    not_alias = [x for x in df_printed.columns if x not in list_alias and x not in list_organic]

    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df_printed[not_alias].join(df_printed[list_alias]).to_excel(writer, 'Master tatanama', index = False)
    writer.save()
    resp = make_response(output.getvalue())
    resp.headers["Content-Disposition"] = "attachment; filename=Master tatanama.xlsx"
    resp.headers["Content-Type"] = "text/xlsx"

    # df_old.columns = [x.replace(' ', '_') for x in df_old.columns]
    # list_url = [x for x in df_old.columns if 'URL' in str(x) and '1' not in str(x)]
    # url_col = df_old[['SKU'] + list_url].copy()
    # df_old = df_old[~df_old['SKU'].astype(str).isin(df['SKU'].astype(str))]
    # df_old = df_old.append(df, ignore_index = True, sort = False)
    # list_alias = [x for x in df_old.columns if 'Alias' in x]
    # list_organic = [x for x in df_old.columns if 'Organik' in x]
    # not_alias = [x for x in df_old.columns if x not in list_alias and x not in list_organic and x not in list_url]
    # bundle = df_old[df_old['Brand'] == 'Bundle'].copy()
    # df_old = df_old[df_old['Brand'] != 'Bundle']
    # df_old = df_old.append(bundle, ignore_index = True, sort = False)
    # df_old['SKU'] = df_old['SKU'].astype(str)
    # url_col['SKU'] = url_col['SKU'].astype(str)
    # temp = df_old.merge(url_col.drop_duplicates(['SKU']), how = 'left', on = 'SKU').set_index(df_old.index)
    # for i in list_url:
    #     df_old[i] = df_old[i].fillna(temp[i + '_y'])
    # list_used = not_alias[:not_alias.index('Harga_Cost_7')+1]
    # list_notused = not_alias[not_alias.index('Harga_Cost_7')+1:]
    # df_old = df_old.applymap(lambda x: pd.to_numeric(x, errors='ignore'))
    # df_old[list_used].set_index(df_old.index).join([df_old[list_url].set_index(df_old.index), df_old[list_notused].set_index(df_old.index), df_old[list_alias].set_index(df_old.index)]).to_excel(r'/home/tatanama/mastertatanama/Master tatanama.xlsx', index = False)

    return resp

@app.route('/login', methods = ['GET', 'POST'])
def login():
    user_session = False
    if 'user' not in session:
        return redirect(url_for('main'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        if username == 'nutrifood' and password == 'nutrifood':
            session['loggedin'] = True
            session['messages'] = 'Loggin Successfully'
            return redirect(url_for('search'))
        else :
            msg = 'Incorrect username or password'
            return render_template('login.html', msg = msg)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    if 'user' not in session:
        return redirect(url_for('main'))
    else :
        return redirect(url_for('search'))

@app.route('/janjianharga')
def janjianharga():
    return render_template('janjianharga.html')


# @app.route('/add_alias_gudang')
# def add_alias_gudang() :
#     user_session = False
#     if 'user' not in session:
#         return redirect(url_for('main'))
#     login = False
#     if 'loggedin' in session:
#         login = True
#     form = SearchSingle(request.form)
#     global df
#     if request.method == 'POST':
#         result = request.form
#         for keys in result:
#             if 'produk' in keys:
#                 produk = result[keys]
#         if str(produk) in df['Nama_Produk'].astype(str).values:
#             indeks = df[df['Nama_Produk'] == produk].index[0]
#             session['indeks'] = int(indeks)
#         else :
#             indeks = df[df['SKU'].astype(str) == str(produk)].index[0]
#             session['indeks'] = int(indeks)
#         dict_result = {}
#         alias_gudang = [x for x in df.columns if 'Alias_Nama_Gudang' in x]
#         for i in alias_gudang:
#             dict_result[i] = df[i][indeks]
#             dict_result[i.replace('Nama', 'SKU')] = df[i.replace('Nama', 'SKU')][indeks]
#         session['dict_result_alias_gudang'] = dict_result
#         return redirect(url_for('insert_alias_gudang'))
#     return render_template('add_alias_gudang.html', form = form, login = login)


# @app.route('/insert_alias_gudang')
# def insert_alias_gudang() :
#     user_session = False
#     if 'user' not in session:
#         return redirect(url_for('main'))
#     login = False
#     if 'loggedin' in session:
#         login = True
#     global df
#     indeks = session.pop('indeks')
#     session['indeks'] = indeks
#     dict_result = session.pop('dict_result_alias_gudang')
#     session['dict_result_alias_gudang'] = dict_result
#     form = AddGudangForm(request.form)
#     if request.method == 'POST':
#         result = request.form
#         name  = result['name']
#         sku = result['sku']
#         mp = result['mp']
#         db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
#         cursor = db.cursor()
#         null_col = False
#         alias_name = [x for x in df.columns if 'Alias_Nama_Gudang' in x]
#         alias_name = [x for x in alias_name if mp in x]
#         for i in alias_name:
#             if not null_col:
#                 if str(df[i][indeks]) == '' or str(df[i][indeks]) == 'nan' or df[i][indeks] == None:
#                     null_col = True
#                     null_name = i
#                     null_sku = i.replace('Nama', 'SKU')
#         if null_col :
#             nama_single = df['Nama_Produk'][indeks]
#             sql_arg = 'UPDATE data_sku SET ' + null_name + ' = %s, ' + null_sku + ' = %s WHERE Nama_Produk = %s'
#             cursor.execute(sql_arg, [name, sku, nama_single])
#             db.commit()
#         else :
#             nama_single = df['Nama_Produk'][indeks]
#             null_name = 'Alias_Nama_Gudang_' + str(mp) + '_' + str(len(alias_name) + 1)
#             null_sku = null_name.replace('Nama', 'SKU')
#             sql_arg = 'ALTER TABLE data_sku ADD ' + null_name + ' VARCHAR (255), ADD ' + null_sku + ' VARCHAR (255)'
#             cursor.execute(sql_arg)
#             db.commit()
#             sql_arg = 'UPDATE data_sku SET ' + null_name + ' = %s, ' + null_sku + ' = %s WHERE Nama_Produk = %s'
#             cursor.execute(sql_arg, [name, sku, nama_single])
#             db.commit()
#         query = "select * from data_sku"
#         df = psql.read_sql(query, con = db)
#         session['messages'] = 'Edit Alias Gudang Data Successful'
#         return redirect(url_for('search'))
#     return render_template('edit_alias_gudang.html', login = login, form = form, data = dict_result, kond = True, len = len(dict_result) + 1, name = df['Nama_Produk'][indeks], sku = df['SKU'][indeks])

if __name__ == "__main__":
    app.debug = True
    app.run(ssl_context='adhoc')