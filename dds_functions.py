from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import hashlib
import pyautogui
import time as t
from openpyxl import load_workbook
kecamatan = 'panjalu'
desa = 'sandingtaman'
part = '2'
wb = load_workbook(filename='list/'+kecamatan+'/'+desa+'/list_'+desa+'_'+part+'.xlsx',data_only=True)
sheet = wb['Sheet1']

options = Options() 

options.add_argument('--user-data-dir=C:/Users/Irpan/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Default')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get("https://bos.polri.go.id/laporan/dds-warga/create")

# ********************* function ***********************
wait = WebDriverWait(driver, timeout=3000)

def wait_until(xpath):
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

def select_el(x_path):
    return driver.find_element(By.XPATH, x_path)

def select_el_byId(elId):
    return driver.find_element(By.ID, elId)

def set_select(xpath, data_value):
    selectEl = select_el(xpath)
    select = Select(selectEl)
    select.select_by_value(data_value)

def set_value(k):
    try:
        keterangan = k.replace('$nama', nama) 
        keterangan = keterangan.replace('$dusun', dusun) 
        keterangan = keterangan.replace('$rt', rt) 
        keterangan = keterangan.replace('$rw', rw) 
        keterangan = keterangan.replace('$desa', desa) 
        return keterangan
    except:
        print("err") 

def expand_element():
    # expand
    wait_until('//*[@id="form_dds_warga"]/div[5]/span')
    select_el('//*[@id="form_dds_warga"]/div[5]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[4]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[3]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[2]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[1]/span').click()
    t.sleep(1)

def fill_form_kepala_keluarga(nama, dusun, rt, rw,desa, kecamatan):
    # set nama
    try:
        select_el_byId('nama_kepala_keluarga').send_keys(nama)
        select_el_byId('detail_alamat_kepala_keluarga').send_keys(dusun)
        # kosongkan rt rw

        select_el_byId('rt_kepala_keluarga').send_keys(Keys.BACKSPACE)
        select_el_byId('rt_kepala_keluarga').send_keys(rt)
        select_el_byId('rw_kepala_keluarga').send_keys(Keys.BACKSPACE)
        select_el_byId('rw_kepala_keluarga').send_keys(rw)

        # select provinsi
        set_select('//*[@id="provinsi"]', 'JAWA BARAT')
        # select kabupaten
        wait_until('//*[@id="3207"]')
        set_select('//*[@id="kabupaten"]', 'KABUPATEN CIAMIS')

        # select KECAMATAN
        if(kecamatan=='rajadesa'):
            kode_kec='320713'
        elif kecamatan=='panjalu':
            kode_kec='320708'
        elif kecamatan=='sukamantri':
            kode_kec='320733'

        xpath = '//*[@id="'+kode_kec+' "]'
        wait_until(xpath)
        set_select('//*[@id="kecamatan"]', kecamatan.upper())

        # select desa
        if(desa.lower()=='tanjungsari'):
            kode_ds = 3207132003

        elif desa.lower() == 'sukaharja':
            kode_ds = 3207132006

        elif desa.lower() == 'sirnabaya':
            kode_ds = 3207132009

        elif desa.lower() == 'sukamantri':
            kode_ds = 3207332001

        elif desa.lower() == 'sandingtaman':
            kode_ds = 3207082004

        elif desa.lower() == 'mekarwangi':
            kode_ds = 3207332005

        wait_until('//*[@id="'+str(kode_ds)+'"]')
        set_select('//*[@id="desa"]', desa)

        # isi dusun rt rw
        select_el('//*[@id="detail_alamat"]').send_keys(dusun)
        select_el('//*[@id="rt"]').send_keys(rt)
        select_el('//*[@id="rw"]').send_keys(rw)
    except:
        print('gagal form 1')

def fill_catatan_kunjungan(tanggal):
    tgl = "document.getElementById('tanggal').value="+"'"+tanggal+"'" 
    driver.execute_script(tgl)

def fill_status_penerima_kunjungan(nama):
    try:
        select_el_byId('nama_penerima_kunjungan').send_keys(nama)
        selectStatus = select_el_byId('status_penerima_kunjungan')
        select = Select(selectStatus)
        select.select_by_value('kepala keluarga')
    except:
        print('gagal set status penerima')

def fill_pendapat_warga(keterangan):
    try:
        # fill Bidang Keluhan = EKONOMI
        selectBidang = driver.find_element(By.NAME, 'pendapat[0][bidang_pendapat]')
        select = Select(selectBidang)
        select.select_by_value('EKONOMI')
    except:
        print('gagal set kategori')

    try:
        # FILL KELUHAN
        selectKeluhan = select_el_byId('uraian-keluhan')
        selectKeluhan.send_keys(keterangan)
    except:
        print('gagal set uraian')

    try:
        # fill keyword
        # selectKeyword = select_el('//*[@id="wrapper-keluhan-warga"]/div[3]/span/span[1]').click()
        pyautogui.moveTo(100, 800)
        t.sleep(1)
        pyautogui.click()
        t.sleep(1)
        pyautogui.scroll(10000)
        pyautogui.scroll(-1400)
        pyautogui.moveTo(300, 800)
        pyautogui.click()
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write('Ekonomi')
        t.sleep(8)
        wait_until('//*[@id="select2-keyword_keluhan-results"]/li[1]')
        select_el('//*[@id="select2-keyword_keluhan-results"]/li[1]').click()
    except:
        print('gagal set keyword 1')

def fill_deteksi_dini(keterangan):
    try:
        pyautogui.press('tab')
        pyautogui.press('right')
        pyautogui.press('right')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(keterangan)

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write('Ekonomi')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
    except:
        print('gagal set keyword 2')
# ********************** end function *****************************
t_all1 = t.time()

i=2
while i <= 46 :
    t1 = t.time()
    tanggal = sheet['B' + str(i)].value
    nama = sheet['C' + str(i)].value
    dusun = sheet['D' + str(i)].value
    rt = str(sheet['E' + str(i)].value)
    rw = str(sheet['F' + str(i)].value)
    desa = sheet['G' + str(i)].value
    k = sheet['H' + str(i)].value
    i+=1
    # step 1 - relace keterangan
    keterangan = set_value(k)

    # step 2 - expand
    expand_element()
    
    # step 3 - fill form pertama @param nama, dusun, rt, rw, kecamatan
    fill_form_kepala_keluarga(nama, dusun, rt, rw, desa, kecamatan) 

    # step 4 - fill catatan kunjungan @param 'tanggal'
    fill_catatan_kunjungan(tanggal)

    # step 5 - status penerima kunjungan @param 'nama'
    fill_status_penerima_kunjungan(nama)

    # step 6 - fill pendapat warga
    fill_pendapat_warga(keterangan)

    # step 7 - fill deteksi dini
    fill_deteksi_dini(keterangan)

# isi deteksi dini


    # swal2-confirm swal2-styled
    wait_until('/html/body/div[3]/div/div[3]/button[1]')
    print('berhasil insert')
    sheet['J' + str(i)].value = 'Done'
    wb.save('list.xlsx')
    select_el('/html/body/div[3]/div/div[3]/button[1]').click()
    wait_until('//*[@id="table-dds-warga_length"]/div/div/a')
    select_el('//*[@id="table-dds-warga_length"]/div/div/a').click()
    t2 = t.time()
    print('Round', str(i), ' : ', t2-t1)
t_all2 = t.time()

print('Total : ', (t_all2-t_all1)/60)