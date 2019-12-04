from flask import Flask, render_template, request, redirect, url_for, session, Response, make_response
import pandas as pd
import MySQLdb
import pandas.io.sql as psql
import re
import json
from wtforms import TextField, Form, SelectField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

db = MySQLdb.connect(host = "Localhost", user = "root", passwd = "Alazhar4!", db = "data_sku")
query = "select * from data_sku"

db_admin = MySQLdb.connect(host = "Localhost", user = "root", passwd = "Alazhar4!", db = "admin")
cursor = db.cursor()

df = psql.read_sql(query, con = db)

# connect_string = 'mysql://root:Alazhar4!@Localhost/data_sku'

# sql_engine = sql.create_engine(connect_string)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

list_auto = []
list_sku = df[df['Brand']!='Bundle']['SKU'].to_list()
list_nama = df[df['Brand']!='Bundle']['Nama_Produk'].to_list()
list_kode = df[df['Brand']!='Bundle']['Kode'].to_list()
list_auto = list_sku + list_nama

class SearchForm(Form):
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
    brand = SelectField('Brand',choices = [('Nutrisari', 'Nutrisari'), ('HiLo', 'HiLo'), ('L-Men', 'Men'), ('Tropicana Slim', 'Tropicana Slim'), ('WRP', 'WRP'), ('Heavenly Blush', 'Heavenly Blush'), ('Gimmick', 'Gimmick'), ('Bonus Produk', 'Bonus Produk'), ('Partnership', 'Partnership')])
    nfi = TextField(validators=[InputRequired("Please insert Price List NFI")], render_kw={"placeholder" : "Insert Price List NFI"}, id = "nfi")
    cost = TextField(validators=[InputRequired("Please insert Cost Price")], render_kw={"placeholder" : "Insert Cost Price"}, id = "cost")
    display = TextField(validators=[InputRequired("Please insert Display Price")], render_kw={"placeholder" : "Insert Display Price"}, id = "display")
    code = TextField(validators=[InputRequired("Please insert Bundle Code")], render_kw={"placeholder" : "Insert Bundle Code"}, id = "code")

class SearchSingle(Form):
    produk1 = TextField(render_kw = {"placeholder" : "Insert SKU or Product Name" }, id='produk1')

@app.route('/_autocomplete', methods = ['GET'])
def autocomplete():
    return Response(json.dumps(list_auto), mimetype='application/json')

@app.route('/_autocompletesku', methods = ['GET'])
def autocompletesku():
    return Response(json.dumps(list_sku), mimetype='application/json')

@app.route('/_autocompletekode', methods = ['GET'])
def autocompletekode():
    return Response(json.dumps(list_kode), mimetype='application/json')

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
    
    for i in list_produk: 
        if str(i) in df['SKU'].astype(str).values:
            if df[df['SKU'].astype(str) == str(i)]['Brand'].values[0] in ['Gimmick', 'Bonus Produk', 'Partnership']:
                list_gimmick.append(i)
                idx = list_produk.index(i)
                list_gimmick_qty.append(list_qty[idx])
        elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
            if df[df['Nama_Produk'].astype(str).str.lower() == str(i).lower()]['Brand'].values[0] in ['Gimmick', 'Bonus Produk', 'Partnership']:
                list_gimmick.append(i)
                idx = list_produk.index(i)
                list_gimmick_qty.append(list_qty[idx])
    for i in list_gimmick :
        idx = list_produk.index(i)
        list_produk.pop(idx)
        list_PCS.pop(idx)
        
    if all(x == list_produk[0] for x in list_produk):
        for i in list_produk:
           if str(i) in df['SKU'].astype(str).values:
               SKU_Bundle = str(df[df['SKU'].astype(str) == str(i)]['SKU'].values[0]) + "P" + str(sum(list_PCS))
           elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
               SKU_Bundle = str(df[str(i).lower() == df['Nama_Produk'].astype(str).str.lower()]['SKU'].values[0])  + "P" + str(sum(list_PCS))
    else:
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
        if len(list_gimmick)!=0:
            for i in range(len(list_gimmick)):
                if str(i) in df['SKU'].astype(str).values:
                    SKU_gim = str(df[df['SKU'].astype(str) ==  str(list_gimmick[i])]['Kode'].values[0])
                elif str(i).lower() in df['Nama_Produk'].astype(str).str.lower().values:
                    SKU_gim = str(df[str(i).lower() == df['Nama_Produk'].astype(str).str.lower()]['Kode'].values[0])
                if int(list_gimmick_qty[i]) > 1:
                    SKU_gim = str(SKU_gim) + '(' + str(list_gimmick_qty[i]) + ')'
                list_SKU_gim.append(SKU_gim)
        list_SKU_gim = sorted(list_SKU_gim, key=lambda x: int("".join([i for i in x if i.isdigit()])))
        for i in list_SKU_gim:
            SKU_Bundle = SKU_Bundle + i
        return SKU_Bundle
 

@app.route('/', methods = ['GET', 'POST'])
def main():
    return redirect(url_for('search'))

@app.route('/Search', methods = ['GET', 'POST'])
def search():
    msg = ''
    login = False
    if 'loggedin' in session:
        login = True
        if 'messages' in session:
            msg = session.pop('messages')
    form = SearchForm(request.form)
    if request.method == "POST":
        form = SearchForm(request.form) 
        result = request.form
        list_produk = []
        list_PCS = []
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
        session['list_produk'] = list_produk
        session['list_PCS'] = list_PCS
        dict_form = dict(zip(list_produk, list_PCS))
        found = False
        dict_result = {}
        index = df[df['SKU'] == '2101684190P2G1'].index.to_list()
        for i in index:
            df['PCS_Produk_2'][i] = 1
        for i in range(df.shape[0]):
            if df['Brand'][i] == 'Bundle':
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
                        print(dict_result['New_SKU'])
                        j = 1
                        while j<=7:
                            colname = 'Produk_' + str(j)
                            if df[colname][i] != '':
                                dict_result[colname] = df[colname][i]
                                dict_result['SKU_' + colname] = df['SKU_' + colname][i]
                                dict_result['PCS_' + colname] = int(float(df['PCS_' + colname][i]))
                                dict_result['Price_List_NFI_' + str(j)] = int(float(df['Price_List_NFI_' + str(j)][i]))
                                dict_result['Subtotal_' + colname] = int(float(df['Subtotal_' + colname][i]))
                            j = j+1
                        
        if found:
            return render_template('search.html', data = dict_result, form = form, login = login)
        return redirect(url_for('insert'))
    return render_template('search.html', form=form, msg = msg, login = login)


@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    list_produk = session.pop('list_produk')
    list_PCS = session.pop('list_PCS')
    sku_result = generate_SKU(list_produk, list_PCS)
    dict_result = {}
    grand_total = 0
    harga_cost = 0
    harga_display = 0
    global df
    j = 1
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
        dict_result['Harga_Cost_' + str(j)] = df['Harga_Cost'][indeks]
        dict_result['Harga_Display_' + str(j)] = df['Harga_Display'][indeks]
        grand_total = grand_total + int(float(dict_result['Subtotal_' + colname]))
        harga_cost = harga_cost + int(float(dict_result['Harga_Cost_' + str(j)]))
        harga_display = harga_display + int(float(dict_result['Harga_Display_' + str(j)]))
        j = j+1
    dict_result['SKU'] = sku_result
    dict_result['Brand'] = 'Bundle'
    dict_result['Price_List_NFI'] = grand_total
    dict_result['Harga_Cost'] = harga_cost
    dict_result['Harga_Display'] = harga_display
    dict_result = dict((k, str(v)) for k,v in dict_result.items())
    if request.method == 'POST':
        result = request.form
        if result['submit_button'] == 'cancel':
            return redirect(url_for('search'))
        for keys in result:
            nama_bundle = result['nama_bundle']
        dict_result['Nama_Produk'] = nama_bundle
        db = MySQLdb.connect(host = "Localhost", user = "root", passwd = "Alazhar4!", db = "data_sku")
        cursor = db.cursor()
        cursor.execute("INSERT INTO data_sku (SKU, Nama_Produk, Brand, Price_List_NFI, Harga_Cost, Harga_Display, Produk_1, SKU_Produk_1, PCS_Produk_1, Price_List_NFI_1, Subtotal_Produk_1,Produk_2, SKU_Produk_2, PCS_Produk_2, Price_List_NFI_2, Subtotal_Produk_2) Values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)", [dict_result['SKU'], dict_result['Nama_Produk'], dict_result['Brand'], dict_result['Price_List_NFI'], dict_result['Harga_Cost'], dict_result['Harga_Display'], dict_result['Produk_1'], dict_result['SKU_Produk_1'], dict_result['PCS_Produk_1'], dict_result['Price_List_NFI_1'], dict_result['Subtotal_Produk_1'],dict_result['Produk_2'], dict_result['SKU_Produk_2'], dict_result['PCS_Produk_2'], dict_result['Price_List_NFI_2'], dict_result['Subtotal_Produk_2']])
        db.commit()
        query = "select * from data_sku"
        df = psql.read_sql(query, con = db)
        return redirect(url_for('search'))
    session['list_produk'] = list_produk
    session['list_PCS'] = list_PCS
    return render_template('insert.html', data = dict_result)

@app.route('/add_single', methods = ['GET', 'POST'])
def add_single():
    form = AddForm(request.form)
    if 'loggedin' in session:
        form = AddForm(request.form)
        if request.method == "POST":
            db = MySQLdb.connect(host = "Localhost", user = "root", passwd = "Alazhar4!", db = "data_sku")
            cursor = db.cursor()
            result = request.form
            nama  = result['name']
            sku = result['sku']
            brand = result['brand']
            nfi = result['nfi']
            cost = result['cost']
            display = result['display']
            code = result['code']
            cursor.execute("INSERT INTO data_sku (SKU, Nama_Produk, Brand, Price_List_NFI, Harga_Cost, Harga_Display, Kode) Values (%s, %s,%s,%s,%s,%s,%s)", [sku, nama, brand, nfi, cost, display, code])
            db.commit()
            session['messages'] = 'Adding Product Successful'
            query = "select * from data_sku"
            global df
            df = psql.read_sql(query, con = db)
            global list_auto
            list_auto = []
            list_auto = list_auto + df[df['Brand']!='Bundle']['SKU'].to_list()
            list_auto = list_auto + df[df['Brand']!='Bundle']['Nama_Produk'].to_list()
            return redirect(url_for('main'))
        return render_template('add_single.html', form = form)
    return redirect(url_for('main'))

@app.route('/edit_single', methods=['GET', 'POST'])
def edit_single():
    form = SearchSingle(request.form)
    if 'edit' in session:
        if request.method == 'POST':
            result = request.form
            edit = session.pop('edit')
            name  = result['name']
            sku = result['sku']
            nfi = result['nfi']
            cost = result['cost']
            display = result['display']
            code = result['code']
            db = MySQLdb.connect(host = "Localhost", user = "root", passwd = "Alazhar4!", db = "data_sku")
            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Nama_Produk = %s, SKU = %s, Price_List_NFI = %s, Harga_Cost = %s, Harga_Display = %s, Kode = %s WHERE Nama_Produk = %s', [name, sku, nfi, cost, display, code, name])
            db.commit()
            query = "select * from data_sku"
            global df
            df = psql.read_sql(query, con = db)
            session['messages'] = 'Edit Data Successful'
            return redirect(url_for('main'))
    else :
        if request.method == 'POST':
            result = request.form
            for keys in result:
                if 'produk' in keys:
                    produk = result[keys]
            if str(produk) in df['Nama_Produk'].astype(str).values:
                indeks = df[df['Nama_Produk'] == produk].index[0]
            else :
                indeks = df[df['SKU'].astype(str) == str(produk)].index[0]
            form = AddForm(request.form)
            name = df['Nama_Produk'][indeks]
            sku = df['SKU'][indeks]
            brand = df['Brand'][indeks]
            nfi = df['Price_List_NFI'][indeks]
            cost = df['Harga_Cost'][indeks]
            display = df['Harga_Display'][indeks]
            code = df['Kode'][indeks]
            session['edit'] = True
            return render_template('edit_single.html', form = form, name = name, sku = sku, brand = brand, nfi = nfi, cost = cost, display = display, code = code)
    return render_template('edit_single.html', form = form)

@app.route('/download')
def download():
    global df
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=Master tatanama.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        db_admin = MySQLdb.connect(host = "Localhost", user = "root", passwd = "Alazhar4!", db = "admin")
        username = request.form['username']
        password = request.form['password']
        cursor_admin =  db_admin.cursor()
        cursor_admin.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password))
        admin = cursor_admin.fetchone()

        if admin:
            session['loggedin'] = True
            session['id'] = admin[1]
            session['username'] = admin[2]
            session['messages'] = 'Loggin Successfully'
            return redirect(url_for('main'))
        else :
            msg = 'Incorrect username or password'
            return render_template('login.html', msg = msg)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.debug = True
    app.run()