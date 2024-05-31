import math
import numpy as np
import sympy as sp

def solve_quadratic(a,b,c):
    result = None

    if a == 0:
        if b == 0:
            if c == 0:
                result = f'Infinite Solutions'
            else:
                result = f'No Solution'
        else:
            result = f'x = {-c/b}' 
    
    else:
        denta = b**2 - 4*a*c
        if denta < 0:
            result = f'No Solution'
        elif denta == 0:
            result = f'x = {-b/(2*a)}'
        else:
            x1 = (-b + math.sqrt(denta)) / 2*a
            x2 = (-b - math.sqrt(denta)) / 2*a
            result = f' x1 = {x1} x2 = {x2}'

    return result

def solve_cubic(a,b,c,d):
    result = None

    denta = b**2 - 3*a*c
    if denta != 0:
        k = (9*a*b*c - 2*b**3 - 27*a**2*d) / (2*math.sqrt(abs(denta)**3))

    if a == 0:
        solve_quadratic(b,c,d)

    else: 
        if denta > 0:
            if abs(k) <= 1:
                beta = 2*math.sqrt(denta)*math.cos(math.acos(k)/3)
                beta1 = beta - b
                x1 = beta1 / (3*a)
                x2 = (2*math.sqrt(denta)*math.cos(math.acos(k)/3 - (2*math.pi)/3) - b) / (3*a)
                x3 = (2*math.sqrt(denta)*math.cos(math.acos(k)/3 + (2*math.pi)/3) - b) / (3*a)
                if x1 < 1e-10:
                    x1 = 0
                if x2 < 1e-10:
                    x2 = 0
                if x3 < 1e-10:
                    x3 = 0
                result = f'x1 = {x1}, x2 = {x2}, x3 = {x3}'

            if abs(k) > 1:
                x = ((math.sqrt(denta)*abs(k)) / (3*a*k)) * ((abs(k) + math.sqrt(k**2 - 1))**(1/3) + (abs(k) - math.sqrt(k**2 - 1))**(1/3)) - (b/(3*a))   
                result = f'x = {x}' 
        
        elif denta == 0:
            beta = b**3 - 27*(a**2)*d
            if beta == 0:
                x = -b/(3*a)
                result = f'x = {x}' 


            if beta != 0:
                # python kh thể tính căn bậc 3 của số âm nên cần xử lí bước trung gian
                beta_cube_root = -abs(beta)**(1/3) if beta < 0 else beta**(1/3)
                x = (-b + (beta)**(1/3)) / (3*a)
                result = f'x = {x}'

        elif denta < 0:
            # Tính toán giá trị k - sqrt(k^2 + 1)
            value = k - math.sqrt(k**2 + 1)

            # Xử lý căn bậc ba của số âm
            cube_root_value = -abs(value)**(1 / 3) if value < 0 else value**(1 / 3)

            x = ((math.sqrt(abs(denta))) / (3*a)) * ((k + math.sqrt(k**2 + 1))**(1/3) + cube_root_value) - (b/(3*a))   
            result = f'x = {x}'
             
    return result    

def solve_quartic(a, b, c, d, e):
    result = None

    x = sp.symbols('x')
    equation = a * x**4 + b * x**3 + c * x**2 + d * x + e
    solutions = sp.solve(equation, x)

    if not solutions:
        result = "No Solution "

    elif len(solutions) == 1:
        sol = solutions[0]
        if sol.is_real:
            sol = sol.evalf()
            if sp.re(sol).is_integer:
                result = f"x = {int(sol)}"
            else:
                result = f"x = {sol}"
        else:
            result = "Infinite Solution "

    else:
        result = ''
        for i, sol in enumerate(solutions):
            sol = sol.evalf()
            if sp.re(sol).is_integer:
                result += f"x{i + 1} = {int(sp.re(sol))} "
            else:
                result += f"x{i + 1} = {sol} "

    return result

def solve_linear_system_2(a,b,c,a1,b1,c1):
    result = None
    # Tạo ma trận hệ số và ma trận kết quả
    coefficients = np.array([[a, b], [a1, b1]])
    results = np.array([c, c1])

    # Tính định thức của ma trận hệ số
    det = np.linalg.det(coefficients)

    if det == 0:
        # Kiểm tra hệ số tỷ lệ
        if a*b1 == b*a1 and a*c1 == a1*c and b*c1 == c*b1:
            result = 'Infinite Solution'
        else:
            result = 'No Solution'

    else:
        # Giải hệ phương trình bằng cách nhân ma trận nghịch đảo với ma trận kết quả
        solution = np.linalg.solve(coefficients, results)
        x, y = solution
        result = f"x = {x}, y = {y}"
    
    return result

def solve_linear_system_3(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    result = None
    coefficients = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    results = np.array([d1, d2, d3])

    try:
        solution = np.linalg.solve(coefficients, results)
        result = f"x = {solution[0]} y = {solution[1]} z = {solution[2]}"

    except np.linalg.LinAlgError:
        det = np.linalg.det(coefficients)
        if det == 0:
            # Kiểm tra vô số nghiệm hay vô nghiệm
            augmented_matrix = np.column_stack((coefficients, results))
            rank_coefficients = np.linalg.matrix_rank(coefficients)
            rank_augmented = np.linalg.matrix_rank(augmented_matrix)
            if rank_coefficients == rank_augmented:
                result = "Infinite Solution"
            else:
                result = "No Solution"
        else:
            result = "No Solution"

    return result

def solve_linear_system_4(a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3, a4, b4, c4, d4, e4):
    result = None
    coefficients = np.array([[a1, b1, c1, d1], [a2, b2, c2, d2], [a3, b3, c3, d3], [a4, b4, c4, d4]])
    results = np.array([e1, e2, e3, e4])

    try:
        solution = np.linalg.solve(coefficients, results)
        result = ''
        for i, sol in enumerate(solution):
            # Chỉ in phần thực nếu số thực là một số nguyên
            if np.isclose(sol, round(sol)):
                sol = round(sol)
            result += f"x{i + 1} = {sol}"
            
    except np.linalg.LinAlgError:
        det = np.linalg.det(coefficients)
        if det == 0:
            # Kiểm tra vô số nghiệm hay vô nghiệm
            augmented_matrix = np.column_stack((coefficients, results))
            rank_coefficients = np.linalg.matrix_rank(coefficients)
            rank_augmented = np.linalg.matrix_rank(augmented_matrix)
            if rank_coefficients == rank_augmented:
                result = "Infinite Solution"
            else:
                result = "No Solution"
        else:
            result = "No Solution"

    return result

print(solve_linear_system_3(2,4,3,6,4,12,6,8,9,7,6,16))