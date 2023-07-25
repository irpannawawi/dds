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

wb = load_workbook(filename='list/panjalu/sandingtaman/list_sandingtaman_1.xlsx',data_only=True)
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
# ********************** end function *****************************

i=2
while i <= len(sheet['A']) :
    time_loop1 = t.time()

    tanggal = sheet['B' + str(i)].value
    nama = sheet['C' + str(i)].value
    dusun = sheet['D' + str(i)].value
    rt = str(sheet['E' + str(i)].value)
    rw = str(sheet['F' + str(i)].value)
    desa = sheet['G' + str(i)].value
    k = sheet['H' + str(i)].value
    try:
        keterangan = k.replace('$nama', nama) 
        keterangan = keterangan.replace('$dusun', dusun) 
        keterangan = keterangan.replace('$rt', rt) 
        keterangan = keterangan.replace('$rw', rw) 
        keterangan = keterangan.replace('$desa', desa) 
    except:
        print("err")

    print('*************** LOOP '+str(i)+' ====================')
    print('Nama : '+nama)
    i+=1
    # expand
    wait_until('//*[@id="form_dds_warga"]/div[5]/span')
    select_el('//*[@id="form_dds_warga"]/div[5]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[4]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[3]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[2]/span').click()
    select_el('//*[@id="form_dds_warga"]/div[1]/span').click()
    t.sleep(1)

    try:
        # set nama
        select_el_byId('nama_kepala_keluarga').send_keys(nama)
        select_el_byId('detail_alamat_kepala_keluarga').send_keys(dusun)
        # kosongkan rt rw

        select_el_byId('rt_kepala_keluarga').send_keys(Keys.BACKSPACE)
        select_el_byId('rt_kepala_keluarga').send_keys(rt)
        select_el_byId('rw_kepala_keluarga').send_keys(Keys.BACKSPACE)
        select_el_byId('rw_kepala_keluarga').send_keys(rw)
        print('berhasil set kepala keluarga')
    except:
        print('gagal form 1')

    # +++++++++++++++++++TAB 2++++++++++++++++++++++++++
    try:
        tgl = "document.getElementById('tanggal').value="+"'"+tanggal+"'" 
        driver.execute_script(tgl)
        print('berhasil set tanggal', tgl, sep=':')
    except:
        print('gagal set tanggal')
    

    # +++++++++++++++++++TAB 3++++++++++++++++++++++++++
    try:
        select_el_byId('nama_penerima_kunjungan').send_keys(nama)
        selectStatus = select_el_byId('status_penerima_kunjungan')
        select = Select(selectStatus)
        select.select_by_value('kepala keluarga')
        print('berhasil set status penerima')
    except:
        print('gagal set status penerima')


    # +++++++++++++++++++TAB 4++++++++++++++++++++++++++
    try:
        # fill Bidang Keluhan = EKONOMI
        selectBidang = driver.find_element(By.NAME, 'pendapat[0][bidang_pendapat]')
        select = Select(selectBidang)
        select.select_by_value('EKONOMI')
        print('berhasil set kategori')
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
        t.sleep(6)
        wait_until('//*[@id="select2-keyword_keluhan-results"]/li[1]')
        select_el('//*[@id="select2-keyword_keluhan-results"]/li[1]').click()
        print('berhasil set keyword 1')
    except:
        print('gagal set keyword 1')


    # +++++++++++++++++++TAB 5++++++++++++++++++++++++++
    try:
        # set alamat
        # open console 
        pyautogui.hotkey('ctrl', 'shift', 'i')
        t.sleep(1)

        # paste code
        pyautogui.hotkey('ctrl','v')
        t.sleep(1)

        # run code
        pyautogui.press('enter')
        t.sleep(1)

        # close console
        pyautogui.hotkey('ctrl', 'shift', 'i')
        print('berhasil set alamat')
    except:
        print('gagal set alamat')

# isi deteksi dini
    try:
        pyautogui.press('tab')
        pyautogui.press('right')
        pyautogui.press('right')

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write('Ekonomi')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        print('berhasil set keyword 2')
    except:
        print('gagal set keyword 2')

    # swal2-confirm swal2-styled
    wait_until('/html/body/div[3]/div/div[3]/button[1]')
    print('berhasil insert')
    sheet['J' + str(i)].value = 'Done'
    wb.save('list.xlsx')
    select_el('/html/body/div[3]/div/div[3]/button[1]').click()
    wait_until('//*[@id="table-dds-warga_length"]/div/div/a')
    select_el('//*[@id="table-dds-warga_length"]/div/div/a').click()
    time_loop2 = t.time()
    print('Loop time : ', time_loop2-time_loop1)
    print('======================================')


print("Exceuted in ", t2-t1)