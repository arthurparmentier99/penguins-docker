import streamlit as st
import requests

def add_fruit_to_server(fruit):
    url = f"http://server:8000/add/{fruit}"
    # response = requests.get(url)
    # return response.json()
    return requests.get(url)

def get_all_fruits_from_server():
    url = "http://server:8000/list"
    # response = requests.get(url)
    # return response.json()["data"]["fruits"]
    return requests.get(url).json()

def main():
    st.title("Fruit Adder")

    # Input for the fruit
    fruit = st.text_input("Enter a fruit:")
    
    # Button to add the fruit
    if st.button("Add Fruit"):
        if fruit:
            result = add_fruit_to_server(fruit)
            if result.status_code == 200:
                st.success("Fruit added successfully!")
            else:
                st.error("Error adding fruit.")
        else:
            st.warning("Please enter a fruit.")

    # Display the list of fruits
    fruits = get_all_fruits_from_server()
    st.header("List of Fruits in MongoDB:")
    st.write(fruits)

if __name__ == "__main__":
    main()
