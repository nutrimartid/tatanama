import pandas as pd
import numpy as np
import MySQLdb
import pandas.io.sql as psql

data_SKU = pd.read_excel(r'Template Ganti Display 20221128.xlsx')
print('Read data SKU')
# data_SKU = data_SKU[data_SKU['SKU'].notnull()]
# data_SKU = data_SKU[data_SKU['Harga_Display_rev'].notnull()]
# data_SKU = data_SKU.reset_index(drop = True)
db = MySQLdb.connect(host = "tatanama.mysql.pythonanywhere-services.com", user = "tatanama", passwd = "satuduatiga", db = "tatanama$data_sku")
db.set_character_set('utf8')
query = "select * from data_sku"
cursor = db.cursor()
df = psql.read_sql(query, con = db)

# cursor.execute('Start Transaction')

# indeks = df[df['Nama_Produk'].astype(str).str.contains('Khusus Homdel', case = False)].index.to_list()
# print(indeks)
# for i in indeks:
#     print(i)
#     if str(df['SKU'][i]) != '2309005300':
#         if str(df['SKU'][i]) in df['SKU'].astype(str).values:
#             if 'Khusus Homdel-' in str(df['Nama_Produk'][i]):
#                 name = str(df['Nama_Produk'][i]).replace('Khusus Homdel-', '').strip()
#             else :
#                 name = str(df['Nama_Produk'][i]).replace('Khusus Homdel - ', '').strip()
#             old_name = str(df['Nama_Produk'][i])
#             sku = df['SKU'][i]
#             print(old_name)
#             print(name)
#             cursor = db.cursor()
#             cursor.execute('UPDATE data_sku SET Nama_Produk = %s WHERE SKU = %s', [name, sku])

# cursor.execute('commit')
# db.commit()

# data_SKU = data_SKU[~data_SKU['KATEGORI '].astype(str).str.contains('Traditional', case = False)]
# data_SKU = data_SKU.reset_index(drop = True)
data_SKU = data_SKU.rename(columns = {
    'SKU' : 'SKU',
    # 'PL baru' : 'New_Price_List_NFI',
    # 'Harga Cost Baru' : 'Harga_Cost_rev'
    'Propose New Harga Display' : 'Harga_Display_rev'
})

data_SKU = data_SKU[data_SKU['SKU'].notnull()]
df['SKU'] = df['SKU'].astype(str)
data_SKU['SKU'] = data_SKU['SKU'].astype(str).str.replace('.0', '', regex = False)

# for i in range(df.shape[0]):
#     if str(df['SKU'][i]) in data_SKU['SKU'].astype(str).values:
#         id = df['ID'][i]
#         nama_produk = data_SKU[data_SKU['SKU'].astype(str) == str(df['SKU'][i])]['Nama_Produk'].values[0]
#         print(id)
#         print(nama_produk)
#         cursor.execute('Update data_sku set Nama_Produk = %s where ID = %s', [str(nama_produk), str(id)])
#         db.commit()

# data_SKU['PL_Baru After PPN / Unit'] = data_SKU['PL_Baru After PPN / Unit'].fillna(data_SKU['Price_List_NFI'])
# data_SKU['Harga_Display_rev'] = data_SKU['Harga_Display_rev'].replace(0, np.nan)
# data_SKU['Harga_Cost_rev'] = data_SKU['Harga_Cost_rev'].replace(0, np.nan)

# data_SKU['New_Price_List_NFI'] = data_SKU['New_Price_List_NFI'].replace(0, np.nan) * 1.1

# data_SKU['Harga_Display_Baru'] = data_SKU['Harga_Display_Baru'].fillna(data_SKU['Harga_Display'])
# print(data_SKU)
cursor.execute('Start Transaction')
print(len(data_SKU))


for i in range(data_SKU.shape[0]):
    ### kalau harga display aja
    if str(data_SKU['Harga_Display_rev'][i]) != 'nan':
        if str(data_SKU['SKU'][i]) in df['SKU'].astype(str).values:
            # print('C')
            sku = str(data_SKU['SKU'][i])
            display = str(int(float(data_SKU['Harga_Display_rev'][i])))


            cursor.execute('UPDATE data_sku SET Harga_Display = %s WHERE SKU = %s', [display, sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_1 = %s WHERE SKU_Produk_1 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_1 = CAST(Harga_Display_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE SKU_Produk_1 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_2 = %s WHERE SKU_Produk_2 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_2 = CAST(Harga_Display_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE SKU_Produk_2 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_3 = %s WHERE SKU_Produk_3 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_3 = CAST(Harga_Display_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE SKU_Produk_3 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_4 = %s WHERE SKU_Produk_4 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_4 = CAST(Harga_Display_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE SKU_Produk_4 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_5 = %s WHERE SKU_Produk_5 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_5 = CAST(Harga_Display_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE SKU_Produk_5 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_6 = %s WHERE SKU_Produk_6 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_6 = CAST(Harga_Display_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE SKU_Produk_6 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_7 = %s WHERE SKU_Produk_7 = %s', [display,sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display_7 = CAST(Harga_Display_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE SKU_Produk_7 = %s', [sku])

            cursor = db.cursor()
            cursor.execute('UPDATE data_sku SET Harga_Display = Harga_Display_1  + Harga_Display_2  + Harga_Display_3  + Harga_Display_4  + Harga_Display_5  + Harga_Display_6+ Harga_Display_7 Where Brand = %s and (SKU_Produk_1 = %s or SKU_Produk_2 = %s or SKU_Produk_3 = %s or SKU_Produk_4 = %s or SKU_Produk_5 = %s or SKU_Produk_6 = %s or SKU_Produk_7 = %s)', ['Bundle',sku,sku,sku,sku,sku,sku,sku])
            db.commit()
            print(sku)
            print(display)

    # if str(data_SKU['New_Price_List_NFI'][i]) != 'nan':

### kalau PL NFI dan harga cost
    # if str(data_SKU['SKU'][i]) in df['SKU'].astype(str).values:
    #     sku = str(data_SKU['SKU'][i])
    #     print(sku)
    #     nfi = str(int(float(data_SKU['New_Price_List_NFI'][i])))
    #     cost = nfi
    #     # cost = str(int(float(data_SKU['Harga_Cost_rev'][i])))
    #     # active = str(data_SKU['Cek aktive'][i])
    #     # brand = str(data_SKU['cek Brand'][i])
    #     # kode = str(data_SKU['Kode'][i])

    #     # cursor.execute('UPDATE data_sku SET Active = %s WHERE SKU = %s', [active, sku])
    #     # cursor.execute('UPDATE data_sku SET Price_List_NFI = %s, Active = %s, Brand = %s, Kode = %s WHERE SKU = %s', [nfi, active, brand, kode, sku])

    #     cursor.execute('UPDATE data_sku SET Price_List_NFI = %s WHERE SKU = %s', [nfi, sku])
    #     cursor.execute('UPDATE data_sku SET Harga_Cost = %s WHERE SKU = %s', [cost, sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_1 = %s, Harga_Cost_1 = %s WHERE SKU_Produk_1 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_1 = CAST(Price_List_NFI_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE SKU_Produk_1 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_1 = CAST(Harga_Cost_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE SKU_Produk_1 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_2 = %s, Harga_Cost_2 = %s WHERE SKU_Produk_2 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_2 = CAST(Price_List_NFI_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE SKU_Produk_2 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_2 = CAST(Harga_Cost_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE SKU_Produk_2 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_3 = %s, Harga_Cost_3 = %s WHERE SKU_Produk_3 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_3 = CAST(Price_List_NFI_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE SKU_Produk_3 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_3 = CAST(Harga_Cost_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE SKU_Produk_3 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_4 = %s, Harga_Cost_4 = %s WHERE SKU_Produk_4 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_4 = CAST(Price_List_NFI_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE SKU_Produk_4 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_4 = CAST(Harga_Cost_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE SKU_Produk_4 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_5 = %s, Harga_Cost_5 = %s WHERE SKU_Produk_5 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_5 = CAST(Price_List_NFI_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE SKU_Produk_5 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_5 = CAST(Harga_Cost_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE SKU_Produk_5 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_6 = %s, Harga_Cost_6 = %s WHERE SKU_Produk_6 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_6 = CAST(Price_List_NFI_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE SKU_Produk_6 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_6 = CAST(Harga_Cost_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE SKU_Produk_6 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI_7 = %s, Harga_Cost_7 = %s WHERE SKU_Produk_7 = %s', [nfi,cost,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Subtotal_Produk_7 = CAST(Price_List_NFI_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE SKU_Produk_7 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost_7 = CAST(Harga_Cost_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE SKU_Produk_7 = %s', [sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Price_List_NFI = Subtotal_Produk_1  + Subtotal_Produk_2  + Subtotal_Produk_3  + Subtotal_Produk_4  + Subtotal_Produk_5  + Subtotal_Produk_6 + Subtotal_Produk_7 Where Brand = %s and (SKU_Produk_1 = %s or SKU_Produk_2 = %s or SKU_Produk_3 = %s or SKU_Produk_4 = %s or SKU_Produk_5 = %s or SKU_Produk_6 = %s or SKU_Produk_7 = %s)', ['Bundle',sku,sku,sku,sku,sku,sku,sku])

    #     cursor = db.cursor()
    #     cursor.execute('UPDATE data_sku SET Harga_Cost = Harga_Cost_1 + Harga_Cost_2  + Harga_Cost_3 + Harga_Cost_4  + Harga_Cost_5 + Harga_Cost_6  + Harga_Cost_7  Where Brand = %s and (SKU_Produk_1 = %s or SKU_Produk_2 = %s or SKU_Produk_3 = %s or SKU_Produk_4 = %s or SKU_Produk_5 = %s or SKU_Produk_6 = %s or SKU_Produk_7 = %s)', ['Bundle',sku,sku,sku,sku,sku,sku,sku])

    #     db.commit()
    #     print(sku)
    #     print(nfi)
    #     print(cost)
    #     # print(active)

#### sampai sini

# cursor.execute('commit')
# db.commit()

# sku = '2305551288'
# # print(sku)
# nfi = str(275000)
# display = str(419000)
# cost = str(275000)
# cursor.execute('Start Transaction')
# cursor.execute('UPDATE data_sku SET Price_List_NFI = %s, Harga_Cost = %s, Harga_Display = %s WHERE SKU = %s', [nfi, cost, display, sku])

# cursor.execute('UPDATE data_sku SET Price_List_NFI_1 = %s, Harga_Cost_1 = %s, Harga_Display_1 = %s WHERE SKU_Produk_1 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_1 = CAST(Price_List_NFI_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE SKU_Produk_1 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_1 = CAST(Harga_Cost_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE SKU_Produk_1 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_1 = CAST(Harga_Display_1 AS UNSIGNED) * CAST(PCS_Produk_1 AS UNSIGNED) WHERE SKU_Produk_1 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI_2 = %s, Harga_Cost_2 = %s, Harga_Display_2 = %s WHERE SKU_Produk_2 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_2 = CAST(Price_List_NFI_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE SKU_Produk_2 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_2 = CAST(Harga_Cost_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE SKU_Produk_2 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_2 = CAST(Harga_Display_2 AS UNSIGNED) * CAST(PCS_Produk_2 AS UNSIGNED) WHERE SKU_Produk_2 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI_3 = %s, Harga_Cost_3 = %s, Harga_Display_3 = %s WHERE SKU_Produk_3 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_3 = CAST(Price_List_NFI_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE SKU_Produk_3 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_3 = CAST(Harga_Cost_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE SKU_Produk_3 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_3 = CAST(Harga_Display_3 AS UNSIGNED) * CAST(PCS_Produk_3 AS UNSIGNED) WHERE SKU_Produk_3 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI_4 = %s, Harga_Cost_4 = %s, Harga_Display_4 = %s WHERE SKU_Produk_4 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_4 = CAST(Price_List_NFI_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE SKU_Produk_4 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_4 = CAST(Harga_Cost_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE SKU_Produk_4 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_4 = CAST(Harga_Display_4 AS UNSIGNED) * CAST(PCS_Produk_4 AS UNSIGNED) WHERE SKU_Produk_4 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI_5 = %s, Harga_Cost_5 = %s, Harga_Display_5 = %s WHERE SKU_Produk_5 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_5 = CAST(Price_List_NFI_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE SKU_Produk_5 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_5 = CAST(Harga_Cost_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE SKU_Produk_5 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_5 = CAST(Harga_Display_5 AS UNSIGNED) * CAST(PCS_Produk_5 AS UNSIGNED) WHERE SKU_Produk_5 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI_6 = %s, Harga_Cost_6 = %s, Harga_Display_6 = %s WHERE SKU_Produk_6 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_6 = CAST(Price_List_NFI_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE SKU_Produk_6 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_6 = CAST(Harga_Cost_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE SKU_Produk_6 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_6 = CAST(Harga_Display_6 AS UNSIGNED) * CAST(PCS_Produk_6 AS UNSIGNED) WHERE SKU_Produk_6 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI_7 = %s, Harga_Cost_7 = %s, Harga_Display_7 = %s WHERE SKU_Produk_7 = %s', [nfi, cost, display,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Subtotal_Produk_7 = CAST(Price_List_NFI_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE SKU_Produk_7 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Price_List_NFI = Subtotal_Produk_1 + Subtotal_Produk_2 + Subtotal_Produk_3 + Subtotal_Produk_4 + Subtotal_Produk_5 + Subtotal_Produk_6 + Subtotal_Produk_7 Where Brand = %s and (SKU_Produk_1 = %s or SKU_Produk_2 = %s or SKU_Produk_3 = %s or SKU_Produk_4 = %s or SKU_Produk_5 = %s or SKU_Produk_6 = %s or SKU_Produk_7 = %s)', ['Bundle',sku,sku,sku,sku,sku,sku,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Cost_7 = CAST(Harga_Cost_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE SKU_Produk_7 = %s', [sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display_7 = CAST(Harga_Display_7 AS UNSIGNED) * CAST(PCS_Produk_7 AS UNSIGNED) WHERE SKU_Produk_7 = %s', [sku])

# cursor.execute('UPDATE data_sku SET Harga_Cost = Harga_Cost_1 + Harga_Cost_2  + Harga_Cost_3 + Harga_Cost_4  + Harga_Cost_5 + Harga_Cost_6  + Harga_Cost_7  Where Brand = %s and (SKU_Produk_1 = %s or SKU_Produk_2 = %s or SKU_Produk_3 = %s or SKU_Produk_4 = %s or SKU_Produk_5 = %s or SKU_Produk_6 = %s or SKU_Produk_7 = %s)', ['Bundle',sku,sku,sku,sku,sku,sku,sku])

# cursor = db.cursor()
# cursor.execute('UPDATE data_sku SET Harga_Display = Harga_Display_1  + Harga_Display_2  + Harga_Display_3  + Harga_Display_4  + Harga_Display_5  + Harga_Display_6+ Harga_Display_7 Where Brand = %s and (SKU_Produk_1 = %s or SKU_Produk_2 = %s or SKU_Produk_3 = %s or SKU_Produk_4 = %s or SKU_Produk_5 = %s or SKU_Produk_6 = %s or SKU_Produk_7 = %s)', ['Bundle',sku,sku,sku,sku,sku,sku,sku])
# db.commit()

# print(sku)
