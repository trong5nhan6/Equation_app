import streamlit as st
import math

from equation import solve_quadratic
from equation import solve_cubic
from equation import solve_quartic
from equation import solve_linear_system_2
from equation import solve_linear_system_3
from equation import solve_linear_system_4

def main():
    st.title('Equation Calculator')

    equation_type = st.radio('Select equation type:', ('Quadratic', 'Cubic', 'Quartic'))

    if equation_type == 'Quadratic':
        st.subheader('Quadratic Equation Solver')
        a = st.number_input("Enter coefficient a:")
        b = st.number_input("Enter coefficient b:")
        c = st.number_input("Enter coefficient c:")

        if st.button("Calculate"):
            result = solve_quadratic(a,b,c)
            st.write(result)
            st.balloons()

    elif equation_type == 'Cubic':
        st.subheader('Cubic Equation Solver')
        a = st.number_input('Enter coefficient a:')
        b = st.number_input('Enter coefficient b:')
        c = st.number_input('Enter coefficient c:')
        d = st.number_input('Enter coefficient d:')
        
        if st.button('Solve'):
            solutions = solve_cubic(a, b, c, d)
            st.write(solutions)

    elif equation_type == 'Quartic':
        st.subheader('Quartic Equation Solver')
        a = st.number_input('Enter coefficient a:')
        b = st.number_input('Enter coefficient b:')
        c = st.number_input('Enter coefficient c:')
        d = st.number_input('Enter coefficient d:')
        e = st.number_input('Enter coefficient e:')
        
        if st.button('Solve'):
            solutions = solve_quartic(a, b, c, d, e)
            st.write(solutions)

    equation_type = st.radio('Select equation:', ('Linear_system_2','Linear_system_3','Linear_system_4'))

    if equation_type == 'Linear_system_2':
        st.subheader('Linear_system_2')
        a = st.number_input("Enter coefficient a1:")
        b = st.number_input("Enter coefficient b1:")
        c = st.number_input("Enter coefficient c1:")
        a1 = st.number_input("Enter coefficient a2:")
        b1 = st.number_input("Enter coefficient b2:")
        c1 = st.number_input("Enter coefficient c2:")

        if st.button("Ok"):
            result = solve_linear_system_2(a,b,c,a1,b1,c1)
            st.write(result)
            st.balloons()

    elif equation_type == 'Linear_system_3':
        st.subheader('Linear_system_3')
        a = st.number_input("Enter coefficient a1:")
        b = st.number_input("Enter coefficient b1:")
        c = st.number_input("Enter coefficient c1:")
        d = st.number_input("Enter coefficient d1:")

        a1 = st.number_input("Enter coefficient a2:")
        b1 = st.number_input("Enter coefficient b2:")
        c1 = st.number_input("Enter coefficient c2:")
        d1 = st.number_input("Enter coefficient d2:")

        a2 = st.number_input("Enter coefficient a3:")
        b2 = st.number_input("Enter coefficient b3:")
        c2 = st.number_input("Enter coefficient c3:")
        d2 = st.number_input("Enter coefficient d3:")


        if st.button("Ok"):
            result = solve_linear_system_2(a,b,c,d,a1,b1,c1,d1,a2,b2,c2,d2)
            st.write(result)
            st.balloons()

    elif equation_type == 'Linear_system_4':
        st.subheader('Linear_system_3')

        a = st.number_input("Enter coefficient a1:")
        b = st.number_input("Enter coefficient b1:")
        c = st.number_input("Enter coefficient c1:")
        d = st.number_input("Enter coefficient d1:")
        e = st.number_input("Enter coefficient e1:")

        a1 = st.number_input("Enter coefficient a2:")
        b1 = st.number_input("Enter coefficient b2:")
        c1 = st.number_input("Enter coefficient c2:")
        d1 = st.number_input("Enter coefficient d2:")
        e1 = st.number_input("Enter coefficient e2:")

        a2 = st.number_input("Enter coefficient a3:")
        b2 = st.number_input("Enter coefficient b3:")
        c2 = st.number_input("Enter coefficient c3:")
        d2 = st.number_input("Enter coefficient d3:")
        e2 = st.number_input("Enter coefficient e3:")
        
        a3 = st.number_input("Enter coefficient a4:")
        b3 = st.number_input("Enter coefficient b4:")
        c3 = st.number_input("Enter coefficient c4:")
        d3 = st.number_input("Enter coefficient d4:")
        e3 = st.number_input("Enter coefficient e4:")

        if st.button("Ok"):
            result = solve_linear_system_2(a, b, c, d, e, a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3)
            st.write(result)
            st.balloons()

if __name__ == "__main__":
    main()