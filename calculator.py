import streamlit as st
import math

def main():
    st.title("Scientific Calculator")

    st.write("### Input:")
    operation = st.selectbox(
        "Choose an operation:",
        ["Addition", "Subtraction", "Multiplication", "Division", "Square Root", "Exponentiation", "Logarithm"]
    )

    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number (if applicable):", value=0.0)

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    elif operation == "Square Root":
        result = math.sqrt(num1)
    elif operation == "Exponentiation":
        result = math.pow(num1, num2)
    elif operation == "Logarithm":
        if num1 > 0:
            result = math.log(num1, num2)
        else:
            result = "Logarithm base must be greater than 0"

    st.write("### Result:")
    st.write(result)

if __name__ == "__main__":
    main()