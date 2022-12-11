# Import the packages
import streamlit as st
import pandas as pd
import emoji
from datetime import date

# Add app title
st.title("MEET JO! :information_desk_person:")

today = date.today().strftime("%A, %B %d %Y")
st.markdown(f"Today is **{today}**")


with st.sidebar:
    st.subheader("Thanks for working with JO!\nThe Joyful Observer's assistant Web App")
    st.text("Have a great meeting!")


tab1, tab2, tab3 = st.tabs(["Meeting Areas","Psychological Safety","Summary"])

with tab1:

    timeliness = st.slider("**How is the timeliness of the meeting?**",min_value=1.0, max_value=5.0, step=0.5)
    timeliness_comments = st.text_area("Timeliness comments here:")

    agenda = st.slider("**Were all the set agenda covered?**",min_value=1.0, max_value=5.0, step=0.5)
    agenda_comments = st.text_area("Agenda comments here:")

    equal_voice = st.slider("**Did everyone had the chance to speak?**",min_value=1.0, max_value=5.0, step=0.5)
    equal_voice_comments = st.text_area("Equal Voice comments here:")

    data_driven = st.slider("**Were presentations data-driven?**",min_value=1.0, max_value=5.0, step=0.5)
    data_driven_comments = st.text_area("Data Driven comments here:")

    follow_through = st.slider("**How did the team do with the follow-through items?**",min_value=1.0, max_value=5.0, step=0.5)
    follow_through_comments = st.text_area("Follow Through comments here:")

    mtg_area = [["Timeliness",timeliness],["Agenda",agenda],["Equal Voice",equal_voice],["Data-driven",data_driven],["Follow Through",follow_through]]
    df1 = pd.DataFrame(mtg_area,columns=["Areas","Scores"])
    mtg_area_score = (timeliness+agenda+equal_voice+data_driven+follow_through)/5



with tab2:

    inclusion = st.slider("**Was the meeting inclusive?**",min_value=1.0, max_value=5.0, step=0.5)
    inclusion_comments = st.text_area("Inclusiveness comments here:")

    learner = st.slider("**How was the learner attitude of the team?**",min_value=1.0, max_value=5.0, step=0.5)
    learner_comments = st.text_area("Learner comments here:")

    contributor = st.slider("**Did everyone get to contribute his/her ideas?**",min_value=1.0, max_value=5.0, step=0.5)
    contributor_comments = st.text_area("Contributor comments here:")

    challenger = st.slider("**How were the challenges handled during the meeting?**",min_value=1.0, max_value=5.0, step=0.5)
    challenger_comments = st.text_area("Challenger comments here:")

    psych_area = [["Inclusion",inclusion],["Learner",learner],["Contributor",contributor],["Challenger",challenger],["",""]]
    df2 = pd.DataFrame(psych_area,columns=["Areas","Scores"])
    psych_area_score = (inclusion+learner+contributor+challenger)/4





with tab3:

    col1,col2 = st.columns(2,gap="large")

    with col1:
        st.subheader(f"Meeting Score = **{mtg_area_score}**")
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
        st.subheader(f"Safety Score = **{psych_area_score}**")
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
