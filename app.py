# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import datetime
from PIL import Image

def main():
    """
    코드 작성
    """

    st.title("Hello World")

    st.text('this is {}'.format('good'))

    st.header('This is header')

    st.subheader('This is Sub Header')

    st.markdown('## This is Markdown Header')

    # Colored Text
    st.success('성공')
    st.warning('위엄함')
    st.info('This is information')
    st.error('This is error')
    st.exception('This is an exception')

    # 수퍼펑션
    st.write(1+1)
    st.write(type("normal"))
    st.write(type(3))

    a = 1
    b = 2 
    st.write(a+b)

    st.write(dir(str))
    st.help(range)

    iris = pd.read_csv("data/iris.csv")
    st.dataframe(iris, 200, 100)

    # 색상 추가
    st.title('Adding Color on Table')
    st.dataframe(iris.style.highlight_max(axis=0)) 

    # static table show
    st.table(iris.head(30))

    # st.write
    st.write(iris)

    # 나의 코드 보여주기
    myCode = """
    def hello()
        print("Hello World!")
    """
    st.code(myCode, language = 'Python')

    # Widgets, 버튼, 체크박스
    name = "Yuchan"
    if st.button('Submit'):
        st.write(f'name : {name.upper()}')

    if st.button('Submit', key = 'new02'):
        st.write(f'name : {name.lower()}')

    # Radio button
    status = st.radio("Status", ("활성화", "비활성화"))
    st.write(status)
    if status == "활성화":
        st.success("활성화 상태")
    elif status == "비활성화":
        st.info("비활성화 상태")
    else:
        pass

    # Check box
    if st.checkbox('Show/Hide'):
        st.text('보여줘!')

    d = st.date_input(
        "When\'s your birthday",
        datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)

    # selectbox
    programings = ['Python', 'Java', 'HTML', 'CSS', 'JS']
    choice = st.selectbox ('프로그래밍 언어:', programings)
    st.write(f'{choice} 언어를 선택함')

    # Multiple Selection
    spoken_lang = ("영어", "일본어", "중국어", "독일어")
    mylangchoice = st.multiselect("언어 선택", spoken_lang, default = "영어")
    st.write("선택:", mylangchoice)

    # Slider 
    age = st.slider('나이', 1, 120, 60)
    st.write(age)
 
    # color = st.select_slider('색상 선택:',
    #                          options = ['노란색', '빨간색', '파란색', '검정색', '흰색'],
    #                          value = ("노란색", "흰색"))
    # st.write(color)
    start_color, end_color = st.select_slider('색상 선택:',
                             options = ['노란색', '빨간색', '파란색', '검정색', '흰색'],
                             value = ("노란색", "흰색"))
    st.write(start_color, end_color)
                                      
    ## 멀티 미디어 파일
    img = Image.open('data/image_03.jpg')
    st.image(img)

    img_url = 'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png'
    st.image(img_url)

    # 비디오 출력
    # 컨텍스트 매니저 : chaptgpt
    with open('data/secret_of_success.mp4', 'rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time=1)
    
    # 오디오 출력
    with open('data/song.mp3', 'rb') as rb:
        audio_file = rb.read()
        st.audio(audio_file, format='audio/mp3')

    # text 파일
    fname = st.text_input('입력해주세요')
    st.title(fname)

    message = st.text_area('입력해주세요', height = 100)
    st.write(message)

    nums = st.number_input('숫자 입력')
    st.write(nums)

    mytime = st.time_input('시간')
    st.write(mytime)

    # Color Picker

    color  = st.color_picker('색상 선택')
    st.write(color)

    # YouTube
    st.video('https://youtu.be/x3zFoghaKBM')

if __name__ == "__main__":
    main()