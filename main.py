import pandas as pd
import streamlit as st


# df = pd.DataFrame(pd.read_csv('wholefood.csv'))
df = pd.DataFrame(pd.read_csv('data1.csv'))

title = "<h1 style='text-align: center;color: #FBEEAC; background-color:#1D5D9B;'>My Food History</h1>"
st.markdown(title, unsafe_allow_html=True)
st.divider()
st.write('')
st.write('')
st.write('')
st.write('')
with st.expander('섭취정보 입력'):
    eat_day = st.date_input('섭취 :blue[날짜]를 입력하세요')
    eat_time = st.time_input('섭취 :blue[시간]을 입력하세요')
    food_list = df.식품명.to_list()
    foot_names = st.multiselect('섭취한 음식을 입력하세요',food_list)
    quantity = st.slider('몇 인분 먹었나요?',1,20,1)
st.divider()
st.write('')
st.write('')
st.write('')
st.write('')
df_res = pd.DataFrame({'섭취일':[],'섭취시간':[],'식품명':[],'에너지(kcal)':[]},'탄수화물(g)':[],'단백질(g)':[],'지질(g)':[],'콜레스트롤(g)':[],'나트륨(g)':[])
# df_res = pd.DataFrame({'섭취일':[],'섭취시간':[],'식품명':[],'에너지(kcal)':[],'탄수화물(g)':[],'단백질(g)':[],'지질(g)':[],'콜레스트롤(g)':[],'나트륨(mg)':[],'식품코드':[]})
for i in foot_names:
    ddf = df[df['식품명']==i].loc[:,['식품명','에너지(kcal)','탄수화물(g)','단백질(g)','지질(g)','콜레스트롤(g)','나트륨(g)','식품코드']]
    df_res = pd.concat([df_res,ddf])
    df_res['섭취일'] = eat_day
    df_res['섭취시간'] = eat_time
    
st.subheader(f"섭취한 음식의 총 칼로리는 :red[{(df_res['에너지(kcal)'].sum())*quantity} Kcal]입니다.(:red[{quantity}]인분 기준)")
col1,col2,col3 = st.columns(3)
with col2:
    save_button = st.button(':green[섭취 기록 저장]',use_container_width=True)
if save_button:
    # df_res.to_csv('save_data.csv',mode='a',header=False,index=False)
    pass



# data_dict = {'섭취일':eat_day,'섭취시간':eat_time,'음식명':foot_names}

