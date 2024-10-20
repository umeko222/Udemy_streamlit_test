import streamlit as st
import pandas as pd


st.title("Hellow World:angel:")  # コロンで囲むと絵文字が書ける
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

st.link_button(
    "Click here",
    "https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/",
)

st.header("Hellow World", divider="rainbow")

code = """print("hellow")"""
st.code(code, language="pytehen")

agree = st.checkbox("I agree")
if agree:
    st.write("Okay")

options = st.multiselect("好きな色は何でしょうか？", ["赤", "緑", "黄", "青"])

st.write("あなたが選んだ色は：", options)

options = st.radio("好きな色は何でしょうか？", ["赤", "緑", "黄", "青"])

st.write("あなたが選んだ色は：", options)

df = pd.DataFrame(
    [
        {"colors": "赤", "rating": 4},
        {"colors": "緑", "rating": 5},
        {"colors": "黄", "rating": 31},
        {"colors": "青", "rating": 8},
    ]
)
edited_df = st.data_editor(df)
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])


df = pd.DataFrame(
    [
        {"colors": "赤", "rating": 4, "mark": True},
        {"colors": "緑", "rating": 5, "mark": True},
        {"colors": "黄", "rating": 3, "mark": True},
        {"colors": "青", "rating": 8, "mark": True},
    ]
)
edited_df = st.data_editor(df)
edited_df = edited_df[edited_df["mark"] == True]
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

# ダウンロードボタン
csv = edited_df.to_csv().encode("utf-8")

st.download_button(
    label="csvをダウンロード", data=csv, file_name="sample_df.csv", mime="text/csv"
)

# プログレスバー
df = pd.DataFrame(
    {
        "sales": [20, 55, 100, 80],
        "progress_sales": [20, 55, 100, 80],
    }
)
st.data_editor(
    df,
    column_config={
        "progress_sales": st.column_config.ProgressColumn(
            min_value=0,
            max_value=100,
        ),
    },
)
# 時系列バー表示
df = pd.DataFrame({"sales": [[0, 4, 26, 30, 60, 80, 100], [3, 50, 0, 80, 40, 30, 100]]})
st.data_editor(df)

st.data_editor(
    df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min=0,
            y_max=100,
        ),
    },
)

# 時系列折れ線グラフ

st.data_editor(
    df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min=0,
            y_max=100,
        ),
    },
)

#スライダーのインプット
age = st.slider("あなたは何歳ですか？",0,130,40)
st.write("私は",age,"です。")

#日付選択
import datetime
date = st.date_input("あなたが生まれたのはいつですか？",datetime.date(2000,1,1))
st.write("私は",date,"に生まれました。")
#ユーザーの自由記述
text = st.text_input("入力してください","xxxxxxx")
st.write(text)

#カラムを分ける
col1,col2 = st.columns(2)
with col1:
    st.title("column1")
    st.write("これはカラム1です")
with col2:
    st.title("column2")
    st.write("これはカラム2です")

#タブを分ける
tab1,tab2 = st.tabs(["tab1","tab2"])
with tab1:
    st.title("tab1")
    st.write("これはタブ1です")
with tab2:
    st.title("tab2")
    st.write("これはタブ2です")

#アコーディオン表示
with st.expander("もっと詳しく見る"):
    st.write("xxxxxxx")

#ポップアップ表示
with st.popover("もっと詳しく見る"):
    st.write("xxxxxxx")
    st.write("GGGGGGG")
    st.write("SSSSSSS")

#サイドバー
with st.sidebar:
    st.write("xxxxxxx")
    st.write("GGGGGGG")
    st.write("SSSSSSS")

#notification
agree = st.checkbox("同意しますか？")
if agree:
    st.toast("Thank you", icon="👍")

#エフェクト
birthday = st.checkbox("今日はあなたの誕生日ですか")
if birthday:
    st.toast("お誕生日おめでとう！",icon="💛")
    st.balloons()

#複数ページ実装
st.page_link("app.py",label = "Home",icon="🏠")
st.page_link("pages/page1.py",label="Page1")
st.page_link("pages/page2.py",label="Page2")
st.page_link("https://qiita.com/MK32A/items/b7984f0419b7dd8d679c",label="QiitaのStreamlit基本操作")

