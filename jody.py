# Import the packages
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.let_it_rain import rain
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.colored_header import colored_header
from PIL import Image

import pandas as pd
import numpy as np
import emoji
from datetime import date

# Add app title
st.title("MEET JO! :information_desk_person:")
# colored_header(
#    label="My New Pretty Colored Header",
#    description="This is a description",
#    color_name="violet-70",
# )

img= Image.open("coffeecup.jpg")

today = date.today().strftime("%A, %B %d %Y")
st.markdown(f"Today is {today}")


with st.sidebar:
    st.subheader("Thanks for working with JO!\nThe Joyful Observer's assistant Web App")
    st.write("Buy us coffee :coffee:!")
    st.write("Scan GCash QR below")
    st.image(img,width=180)
    

tab1, tab2, tab3 = st.tabs(["Meeting Areas","Psychological Safety","Summary"])

with tab1:

    timeliness = st.slider("**How is the timeliness of the meeting?**",min_value=1.0, max_value=5.0, step=0.5)
    
    with st.expander("See guide"):
        st.write("""
        Did the meeting start & finish on time?
        """)
        
    timeliness_comments = st.text_area("Timeliness comments here:")

    agenda = st.slider("**Were all the set agenda covered?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Did we state the objectives of the meeting and did we meet them?\n
        Did we keep to the topic? Were parking lots used for off-topics?
        """)
        
    agenda_comments = st.text_area("Agenda comments here:")

    equal_voice = st.slider("**Did everyone had the chance to speak?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Did everyone speak? Did someone speak most than others unnecessarily?
        """)
    
    equal_voice_comments = st.text_area("Equal Voice comments here:")

    data_driven = st.slider("**Were presentations data-driven?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Were the discussions backed up with facts and actual stats?
        """)
    
    data_driven_comments = st.text_area("Data Driven comments here:")

    follow_through = st.slider("**How did the team do with the follow-through items?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Were action items (Responsible, Expected Get Back, Timeline) clearly stated at the end of the session? 
        Were the recommended direct/specific action verbs used?
        [For Recurring Meetings or Cadences] Were get backs on action items from previous sessions updated or closed?
        """)    
    
    follow_through_comments = st.text_area("Follow Through comments here:")

    mtg_area = [["Timeliness",timeliness],["Agenda",agenda],["Equal Voice",equal_voice],["Data-driven",data_driven],["Follow Through",follow_through]]
    df1 = pd.DataFrame(mtg_area,columns=["Areas","Scores"])
    mtg_area_score = (timeliness+agenda+equal_voice+data_driven+follow_through)/5



with tab2:

    inclusion = st.slider("**Was the meeting inclusive?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Is the meeting size just right to encourage conversational turn-taking?
        Did everyone get a chance to be heard?
        Did everyone pay attention and recognize inputs and contributions of each other?
        """)
        
    inclusion_comments = st.text_area("Inclusiveness comments here:")

    learner = st.slider("**How was the learner attitude of the team?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Did people feel safe to ask questions or clarifications without being judged?
        Did we take time to learn from mistakes/misses/callouts?
        Did we take time to hear the facts and opinions before making a decision? 
        """)
            
    learner_comments = st.text_area("Learner comments here:")

    contributor = st.slider("**Did everyone get to contribute his/her ideas?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Did the team feel safe to raise threats & call outs?
        Did people practice patience and not shoot the messenger for "bad/different" ideas?
        """)
            
    contributor_comments = st.text_area("Contributor comments here:")

    challenger = st.slider("**How were the challenges handled during the meeting?**",min_value=1.0, max_value=5.0, step=0.5)

    with st.expander("See guide"):
        st.write("""
        Did we create an environment where it is OK to correct and be corrected, challenge and be challenged, and to have different points of view? 
        Did we encourage out of the box thinking and encourage challenging the norm?
        """)
            
    challenger_comments = st.text_area("Challenger comments here:")

    psych_area = [["Inclusion",inclusion],["Learner",learner],["Contributor",contributor],["Challenger",challenger],["",""]]
    df2 = pd.DataFrame(psych_area,columns=["Areas","Scores"])
    psych_area_score = (inclusion+learner+contributor+challenger)/4





with tab3:

    col1,col2 = st.columns(2,gap="large")
    col1.metric(label="Meeting Score", value=mtg_area_score, delta=(mtg_area_score-5))
    col2.metric(label="Safety Score", value=psych_area_score, delta=(psych_area_score-5))
    style_metric_cards()

    
    rain(
    emoji="✨",
    font_size=30,
    falling_speed=3,
    animation_length="infinite",
    )

    with col1:
        # st.subheader(f"Meeting Score = **{mtg_area_score}**")
        st.write(df1)

        st.caption("Timeliness:")
        st.write(timeliness_comments)
        st.markdown("---")

        st.caption("Agenda:")
        st.write(agenda_comments)
        st.markdown("---")

        st.caption("Equal Voice:")
        st.write(equal_voice_comments)
        st.markdown("---")

        st.caption("Data Driven:")
        st.write(data_driven_comments)
        st.markdown("---")

        st.caption("Follow Through:")
        st.write(follow_through_comments)

            
    with col2:
        # st.subheader(f"Safety Score = **{psych_area_score}**")
        st.write(df2)

        st.caption("Inclusion:")
        st.write(inclusion_comments)
        st.markdown("---")

        st.caption("Learner:")
        st.write(learner_comments)
        st.markdown("---")

        st.caption("Contributor:")
        st.write(contributor_comments)
        st.markdown("---")

        st.caption("Challenger:")
        st.write(challenger_comments)
        
    mtg_df = df1.copy()
    mtg_txt = [timeliness_comments,agenda_comments,equal_voice_comments,
    data_driven_comments,follow_through_comments]
    mtg_df["Notes"] = mtg_txt
    mtg_df["Category"]="Meeting"
    
    # Add a Meeting Totals Row
    mtg_totals = {"Areas":[""],"Scores":[mtg_area_score],
    "Notes":[""],"Category":["Meeting Total Score:"],}
    mtg_totals = pd.DataFrame(mtg_totals)

    #mtg_df = mtg_df.append(mtg_totals)
    mtg_df = pd.concat([mtg_df,mtg_totals])

    psyc_df = df2.copy()
    psyc_txt = [inclusion_comments,learner_comments,
    contributor_comments,challenger_comments,""]
    psyc_df["Notes"]=psyc_txt
    psyc_df["Category"]="Psychological_Safety"
    psyc_df["Notes"].replace('', np.nan, inplace=True)
    psyc_df.dropna(subset=["Notes"],inplace=True)
    


    # Add a Psychological Safety Totals Row
    psyc_totals = {"Areas":[""],"Scores":[psych_area_score],
    "Notes":[""],"Category":["Psychological Safety Total Score:"],}
    psyc_totals = pd.DataFrame(psyc_totals)

    #psyc_df = psyc_df.append(psyc_totals)
    psyc_df = pd.concat([psyc_df,psyc_totals])

    mom = pd.concat([mtg_df,psyc_df])
    mom = mom[['Category','Areas','Scores','Notes']]
    mom["Date"]=today



    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    
    csv = convert_df(mom)

    st.download_button(
    "Download Meeting Details",
    csv,
    f"Meeting_Minutes_{today}.csv",
    "text/csv",
    key='download-csv'
    )
