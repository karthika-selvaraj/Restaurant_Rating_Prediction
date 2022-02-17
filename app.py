import streamlit as st
import pickle 
RF_pickle=open('RF_Regressor.pkl','rb')
Regressor_Model=pickle.load(RF_pickle)

def restaurant(online_order,book_table,votes,rest_type,dish_liked,cuisines,cost,reviews_list,type):
    if (online_order=='Yes'):  #online order
        online_order=1
    else:
        online_order=0
    if (book_table=='Yes'): #book_table
        book_table=1
    else:
        book_table=0
    if (rest_type=='Casual Dining'): #rest_type
        rest_type=1    
    else:
        rest_type=0       
    if (dish_liked=='Masala Dosa'): #dish_liked
        dish_liked=1
    else:
        dish_liked=0
    if (cuisines=='North Indian'): #cuisines
        cuisines=1
    else:
        cuisines=0
    if (reviews_list=='Great food'): #reviews_list
        reviews_list=1
    else:
        reviews_list=0
    if (type=='Buffet'): #type
        type=1
    else:
        type=0
    
    prediction=Regressor_Model.predict([[online_order,book_table,votes,rest_type,dish_liked,cuisines,cost,reviews_list,type]])
    output = round(prediction[0], 2)
    print(output)
    return output

#main function
def main():
    #st.title('Restaurant Rating Prediction')
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Restaurant Rating Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    online_order=st.selectbox('Is online order availabe?', ('Yes','No'))
    book_table=st.selectbox('Is table booking available?',('Yes','No'))
    votes=st.number_input('Votes',min_value=0,max_value=20000)
    rest_type=st.text_input('Restaurant Type',"")
    dish_liked=st.text_input('Most Liked Dish',"")
    cuisines=st.text_input('Cuisines',"")
    cost=st.number_input('Cost',min_value=0,max_value=20000)
    reviews_list=st.text_input('Review',"")
    type=st.selectbox('Type',('Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out','Drinks & nightlife', 'Pubs and bars'))
    
    result=""
    if st.button('Predict'):
        result=restaurant(online_order,book_table,votes,rest_type,dish_liked,cuisines,cost,reviews_list,type)
        st.success("The Predicted Rating is {}".format(result))
        st.write('Created by Karthika Selvaraj')


if __name__=='__main__':
    main()