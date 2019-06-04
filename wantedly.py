#coding:utf-8
import time
import pandas as pd

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options

# オプションの設定
#opts = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
#opts.set_headless(True)
# ブラウザを起動する(chromedriverへのpathを指定), オプションの設定を有効化
#driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=opts)
driver = webdriver.Chrome()

# Wantedly のトップ画面を開く。
driver.get('https://www.wantedly.com/')
# タイトルに'Wantedly'が含まれていることを確認する。
assert 'Wantedly' in driver.title

# csvファイルの読み込み、念のため別ファイルで保存
#user_file = pd.read_csv('{ユーザーファイルまでのpath}/user_file.csv')

# 複数人でやることは規約違反なのでやめてください。
# ログインIDとパスワードを記入
#user_id = "itayu021252@gmail.com".iloc[0, 0]
#user_pass = "itayu0212".iloc[0, 1]
user_id = "itayu021252@gmail.com"
user_pass = "itayu0212"
# ログインボタンをクリック
driver.find_element_by_class_name('ui-show-modal').click()
driver.implicitly_wait(2)

# ユーザーIDとパスワードを入力してログイン
uid = driver.find_element_by_id('login_user_email')
password = driver.find_element_by_id('login_user_password')
uid.send_keys(user_id)
password.send_keys(user_pass)
driver.find_element_by_name('commit').click()

# "あなたの会社名"のページに移動する(ログインしてもしなくてもURLは同じ)
driver.get('https://www.wantedly.com/projects/317855')
time.sleep(1)

# プロフィールからログイン出来ているか確認する
profile_btn = driver.find_elements_by_class_name('user-profile-photo')

if (len(profile_btn) > 0): # ログインできている場合
    support_btn = driver.find_elements_by_css_selector('.wt-button.blue.noborder.project-support-link')

    if (len(support_btn) > 0): # 「応援する」ボタンがある。
        driver.find_element_by_css_selector('.wt-button.blue.noborder.project-support-link').click()
        time.sleep(2)
        driver.find_element_by_class_name('ProjectSupportModal__FacebookButton-at4y5v-13').click()
        driver.find_element_by_css_selector('.inputtext _55r1 inputtext inputtext').send_keys(user_id)
        driver.find_element_by_css_selector('.inputtext _55r1 inputtext inputtext').send_keys(user_pass)
    else: # 「応援する」ボタンがない
        # すでに「応援する」ボタンを押していれば何もせずに終了
        print(user_id + " already pressed support button!")

    time.sleep(2) #ページの遷移を待つ
    # ログアウトする
    driver.find_element_by_class_name('user-profile-photo').click()
    driver.implicitly_wait(1)
    driver.find_element_by_id('menu-user-logout').click()
    time.sleep(1)

else: # ログイン出来ていない場合
    print('failed to login with ' + user_id + '!')
    #continue # この場合はログインをスキップ


driver.quit()  # ブラウザーを終了する。これは必要みたいです。
