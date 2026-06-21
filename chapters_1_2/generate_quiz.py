import json

questions = [
    # Concepts and Vocabulary
    {"q": "Let \\(f(x)\\) be an invertible function. If the domain of \\(f(x)\\) is \\((-2, \\infty)\\) and the range is \\([4, 10]\\), what are the domain and range of \\(f^{-1}(x)\\)?", "category": "Concepts and Vocabulary", "options": ["Domain: \\((-2, \\infty)\\), Range: \\([4, 10]\\)", "Domain: \\([4, 10]\\), Range: \\((-2, \\infty)\\)", "Domain: \\((-\\infty, 2)\\), Range: \\([-10, -4]\\)", "Cannot be determined without the equation."], "answer": 1, "explanation": "The domain of an inverse function is exactly the range of the original function, and its range is the domain of the original function."},
    {"q": "Which of the following statements about complex conjugates is ALWAYS true for any complex number \\(z = a + bi\\)?", "category": "Concepts and Vocabulary", "options": ["\\(z + \\bar{z}\\) is purely imaginary.", "\\(z - \\bar{z}\\) is purely real.", "\\(z \\cdot \\bar{z}\\) is a non-negative real number.", "\\(z / \\bar{z}\\) is always 1."], "answer": 2, "explanation": "\\(z \\cdot \\bar{z} = (a+bi)(a-bi) = a^2 - (bi)^2 = a^2 + b^2\\). Since \\(a\\) and \\(b\\) are real, \\(a^2 + b^2\\) is a sum of squares, which is always a non-negative real number."},
    {"q": "What is the primary purpose of the discriminant in the quadratic formula?", "category": "Concepts and Vocabulary", "options": ["To find the vertex of the parabola.", "To determine the number and type of roots of the equation.", "To calculate the y-intercept of the quadratic function.", "To complete the square geometrically."], "answer": 1, "explanation": "The discriminant \\(\\Delta = b^2 - 4ac\\) determines if the roots are real and distinct (positive), real and repeated (zero), or complex conjugates (negative)."},
    
    # Building Skills
    {"q": "Solve for x: \\(\\frac{3}{x+2} - \\frac{1}{x-2} = \\frac{12}{x^2 - 4}\\)", "category": "Building Skills", "options": ["x = 5", "x = 4", "x = -1", "No solution"], "answer": 0, "explanation": "The LCD is \\((x+2)(x-2)\\). Multiplying everything by the LCD yields: \\(3(x-2) - 1(x+2) = 12 \\implies 3x - 6 - x - 2 = 12 \\implies 2x - 8 = 12 \\implies 2x = 20 \\implies x = 10\\). Wait, the options don't have 10? Let's recalculate: \\(3(x-2) - (x+2) = 12 \\implies 2x - 8 = 12 \\implies x = 10\\). Let me fix the answer choices! Ah, if the answer is x=10, the correct option should be 10. Let me use x=10 for option 0.", "options": ["x = 10", "x = 4", "x = -1", "No solution"]},
    {"q": "Solve for x: \\(\\frac{3}{x+2} - \\frac{1}{x-2} = \\frac{12}{x^2 - 4}\\)", "category": "Building Skills", "options": ["x = 10", "x = 4", "x = -1", "No solution"], "answer": 0, "explanation": "The LCD is \\((x+2)(x-2)\\). Multiplying everything by the LCD yields: \\(3(x-2) - 1(x+2) = 12 \\implies 3x - 6 - x - 2 = 12 \\implies 2x - 8 = 12 \\implies 2x = 20 \\implies x = 10\\)."},
    {"q": "Rationalize the denominator and simplify: \\(\\frac{5 - \\sqrt{3}}{2 + \\sqrt{3}}\\)", "category": "Building Skills", "options": ["\\(13 - 7\\sqrt{3}\\)", "\\(7 - 3\\sqrt{3}\\)", "\\(10 - 2\\sqrt{3}\\)", "\\(13 + 7\\sqrt{3}\\)"], "answer": 0, "explanation": "Multiply numerator and denominator by \\(2 - \\sqrt{3}\\). Denominator becomes \\(4 - 3 = 1\\). Numerator becomes \\((5 - \\sqrt{3})(2 - \\sqrt{3}) = 10 - 5\\sqrt{3} - 2\\sqrt{3} + 3 = 13 - 7\\sqrt{3}\\)."},
    {"q": "Find the inverse function \\(f^{-1}(x)\\) for \\(f(x) = \\frac{4x - 1}{2x + 3}\\)", "category": "Building Skills", "options": ["\\(f^{-1}(x) = \\frac{2x + 3}{4x - 1}\\)", "\\(f^{-1}(x) = \\frac{3x + 1}{4 - 2x}\\)", "\\(f^{-1}(x) = \\frac{3x - 1}{4 + 2x}\\)", "\\(f^{-1}(x) = \\frac{4x + 1}{2x - 3}\\)"], "answer": 1, "explanation": "Let \\(y = \\frac{4x-1}{2x+3}\\). Swap: \\(x = \\frac{4y-1}{2y+3}\\). Multiply: \\(2xy + 3x = 4y - 1\\). Isolate y terms: \\(2xy - 4y = -3x - 1 \\implies y(2x - 4) = -3x - 1 \\implies y = \\frac{-3x - 1}{2x - 4} = \\frac{3x + 1}{4 - 2x}\\)."},

    # Applying the Concepts
    {"q": "A chemist needs 10 liters of a 30% acid solution. They only have 10% and 50% acid solutions in the lab. How many liters of the 50% solution should they mix with the 10% solution?", "category": "Applying the Concepts", "options": ["2.5 L", "4 L", "5 L", "7.5 L"], "answer": 2, "explanation": "Let \\(x\\) be the liters of 50% solution, so \\(10-x\\) is the 10% solution. Equation: \\(0.50x + 0.10(10-x) = 0.30(10)\\). \\(0.50x + 1 - 0.10x = 3 \\implies 0.40x = 2 \\implies x = 5\\)."},
    {"q": "A ball is thrown straight up. Its height \\(h\\) in feet after \\(t\\) seconds is given by \\(h(t) = -16t^2 + 64t + 80\\). How long will it take for the ball to hit the ground?", "category": "Applying the Concepts", "options": ["2 seconds", "4 seconds", "5 seconds", "8 seconds"], "answer": 2, "explanation": "Set \\(h(t) = 0\\). \\(-16t^2 + 64t + 80 = 0\\). Divide by -16: \\(t^2 - 4t - 5 = 0\\). Factor: \\((t-5)(t+1) = 0\\). Since \\(t > 0\\), \\(t = 5\\) seconds."},
    {"q": "A rectangle is inscribed in a semicircle of radius 10. If the length of the rectangle on the diameter is \\(2x\\), express the area of the rectangle as a function of \\(x\\).", "category": "Applying the Concepts", "options": ["\\(A(x) = x\\sqrt{100 - x^2}\\)", "\\(A(x) = 2x\\sqrt{100 - x^2}\\)", "\\(A(x) = 2x(100 - x^2)\\)", "\\(A(x) = x(100 - x^2)\\)"], "answer": 1, "explanation": "The coordinates of the top right corner of the rectangle on the circle are \\((x, y)\\). The equation of the circle is \\(x^2 + y^2 = 100\\), so \\(y = \\sqrt{100 - x^2}\\). The base of the rectangle is \\(2x\\) and height is \\(y\\). Area \\(A = 2xy = 2x\\sqrt{100 - x^2}\\)."},

    # Beyond the Basics
    {"q": "Solve the inequality: \\(\\frac{x^2 - x - 6}{x^2 + 4x + 4} \\ge 0\\)", "category": "Beyond the Basics", "options": ["\\((-\\infty, -2) \\cup (-2, 3]\\)", "\\((-\\infty, -2) \\cup [3, \\infty)\\)", "\\([-2, 3]\\)", "\\((-\\infty, -2) \\cup (-2, -2] \\cup [3, \\infty)\\) -> actually (-inf, -2) U ( -2, 3]"], "answer": 1, "explanation": "Let's fix options! Factoring gives \\(\\frac{(x-3)(x+2)}{(x+2)^2} \\ge 0\\). The \\((x+2)\\) factor cancels partially, giving \\(\\frac{x-3}{x+2} \\ge 0\\) with a hole at \\(x=-2\\). The critical points are -2 (vertical asymptote/hole) and 3 (root). Sign analysis on intervals \\((-\\infty, -2)\\), \\((-2, 3)\\), \\((3, \\infty)\\) gives positive, negative, positive. Thus \\((-\\infty, -2) \\cup [3, \\infty)\\).", "options": ["\\((-\\infty, -2) \\cup (-2, 3]\\)", "\\((-\\infty, -2) \\cup [3, \\infty)\\)", "\\((-\\infty, -2) \\cup [3, \\infty)\\) Wait, duplicate. Let's fix.", "\\([-2, 3]\\)"]},
    {"q": "Solve the inequality: \\(\\frac{x^2 - x - 6}{x^2 + 4x + 4} \\ge 0\\)", "category": "Beyond the Basics", "options": ["\\((-\\infty, -2) \\cup (-2, 3]\\)", "\\((-\\infty, -2) \\cup [3, \\infty)\\)", "\\([-2, 3]\\)", "\\([3, \\infty)\\)"], "answer": 1, "explanation": "Factor the numerator and denominator: \\(\\frac{(x-3)(x+2)}{(x+2)^2} \\ge 0\\). This simplifies to \\(\\frac{x-3}{x+2} \\ge 0\\) where \\(x \\neq -2\\). The boundary points are \\(x = 3\\) (numerator) and \\(x = -2\\) (denominator). Testing regions gives positive on \\((-\\infty, -2)\\) and \\([3, \\infty)\\)."},
    {"q": "Find all real solutions to the equation: \\(x^{2/3} - 5x^{1/3} + 6 = 0\\)", "category": "Beyond the Basics", "options": ["\\(x = 2, 3\\)", "\\(x = 4, 9\\)", "\\(x = 8, 27\\)", "\\(x = \\sqrt{2}, \\sqrt{3}\\)"], "answer": 2, "explanation": "This is quadratic in form. Let \\(u = x^{1/3}\\). The equation is \\(u^2 - 5u + 6 = 0\\), which factors to \\((u-2)(u-3)=0\\). Thus \\(u=2\\) or \\(u=3\\). Since \\(u = x^{1/3}\\), cubing both sides gives \\(x = 2^3 = 8\\) and \\(x = 3^3 = 27\\)."},
    {"q": "Determine the end behavior and maximum number of turning points for \\(f(x) = -3x^5 + 4x^3 - x + 1\\).", "category": "Beyond the Basics", "options": ["As \\(x \\to \\infty, y \\to \\infty\\); As \\(x \\to -\\infty, y \\to -\\infty\\); 5 turning points", "As \\(x \\to \\infty, y \\to -\\infty\\); As \\(x \\to -\\infty, y \\to \\infty\\); 4 turning points", "As \\(x \\to \\pm\\infty, y \\to -\\infty\\); 4 turning points", "As \\(x \\to \\infty, y \\to -\\infty\\); As \\(x \\to -\\infty, y \\to \\infty\\); 5 turning points"], "answer": 1, "explanation": "The leading term is \\(-3x^5\\) (odd degree, negative coefficient). This means it rises to the left and falls to the right (\\(y \\to \\infty\\) as \\(x \\to -\\infty\\) and \\(y \\to -\\infty\\) as \\(x \\to \\infty\\)). A polynomial of degree \\(n\\) has at most \\(n-1\\) turning points, so \\(5-1 = 4\\)."},

    # Critical Thinking / Discussion / Writing
    {"q": "Consider the function \\(f(x) = \\sqrt{1 - x^2}\\). Without graphing, logically deduce why this function is NOT one-to-one, and therefore does not have a global inverse.", "category": "Critical Thinking / Discussion / Writing", "options": ["Because its domain is restricted to \\([-1, 1]\\).", "Because it contains a square root, and square roots inherently have two answers.", "Because \\(f(x)\\) is an even function, meaning \\(f(-x) = f(x)\\), so two different inputs yield the same output.", "Because the range only contains positive numbers."], "answer": 2, "explanation": "A function is one-to-one if \\(f(a) = f(b) \\implies a = b\\). Since \\(f(x) = \\sqrt{1-x^2}\\) is an even function, \\(f(0.5) = f(-0.5) = \\sqrt{0.75}\\). Since two different x-values produce the same y-value, it fails the horizontal line test and is not one-to-one."},
    {"q": "A student solves \\(\\sqrt{x+6} = x\\) by squaring both sides to get \\(x+6 = x^2\\), leading to roots \\(x = 3\\) and \\(x = -2\\). They declare both as solutions. Why is this logically flawed?", "category": "Critical Thinking / Discussion / Writing", "options": ["Squaring both sides is an invalid mathematical operation.", "The student factored the quadratic equation incorrectly.", "Squaring both sides creates a new equation where the principal square root is forced to equal a negative number, introducing extraneous solutions. (\\(\\sqrt{4} \\neq -2\\))", "The domain of the original equation does not include positive numbers."], "answer": 2, "explanation": "Squaring is a non-reversible operation if signs aren't restricted. Plugging \\(x=-2\\) back into the original gives \\(\\sqrt{4} = -2\\), which is false because the radical symbol denotes the *principal* (positive) root."},
    {"q": "Explain algebraically why the composition of two odd functions is always an odd function.", "category": "Critical Thinking / Discussion / Writing", "options": ["If \\(f\\) and \\(g\\) are odd, \\(f(g(-x)) = f(-g(x)) = -f(g(x))\\).", "If \\(f\\) and \\(g\\) are odd, \\(f(g(-x)) = -f(-g(x)) = f(g(x))\\).", "Odd functions have odd powers, and multiplying odd powers creates odd powers.", "It is not always an odd function; it depends on the coefficients."], "answer": 0, "explanation": "Let \\(f\\) and \\(g\\) be odd, meaning \\(g(-x) = -g(x)\\) and \\(f(-x) = -f(x)\\). Then the composition evaluated at \\(-x\\) is \\((f \\circ g)(-x) = f(g(-x)) = f(-g(x)) = -f(g(x)) = -(f \\circ g)(x)\\). This perfectly defines an odd function."}
]

# We need to drop the dummy duplicates we introduced during generation above. I'll construct a clean list.
clean_questions = [
    # Concepts and Vocabulary
    {"q": "Let \\(f(x)\\) be an invertible function. If the domain of \\(f(x)\\) is \\((-2, \\infty)\\) and the range is \\([4, 10]\\), what are the domain and range of \\(f^{-1}(x)\\)?", "category": "Concepts and Vocabulary", "options": ["Domain: \\((-2, \\infty)\\), Range: \\([4, 10]\\)", "Domain: \\([4, 10]\\), Range: \\((-2, \\infty)\\)", "Domain: \\((-\\infty, 2)\\), Range: \\([-10, -4]\\)", "Cannot be determined without the equation."], "answer": 1, "explanation": "The domain of an inverse function is exactly the range of the original function, and its range is the domain of the original function."},
    {"q": "Which of the following statements about complex conjugates is ALWAYS true for any complex number \\(z = a + bi\\)?", "category": "Concepts and Vocabulary", "options": ["\\(z + \\bar{z}\\) is purely imaginary.", "\\(z - \\bar{z}\\) is purely real.", "\\(z \\cdot \\bar{z}\\) is a non-negative real number.", "\\(z / \\bar{z}\\) is always 1."], "answer": 2, "explanation": "\\(z \\cdot \\bar{z} = (a+bi)(a-bi) = a^2 - (bi)^2 = a^2 + b^2\\). Since \\(a\\) and \\(b\\) are real, \\(a^2 + b^2\\) is a sum of squares, which is always a non-negative real number."},
    {"q": "What is the primary purpose of the discriminant in the quadratic formula?", "category": "Concepts and Vocabulary", "options": ["To find the vertex of the parabola.", "To determine the number and type of roots of the equation.", "To calculate the y-intercept of the quadratic function.", "To complete the square geometrically."], "answer": 1, "explanation": "The discriminant \\(\\Delta = b^2 - 4ac\\) determines if the roots are real and distinct (positive), real and repeated (zero), or complex conjugates (negative)."},
    
    # Building Skills
    {"q": "Solve for x: \\(\\frac{3}{x+2} - \\frac{1}{x-2} = \\frac{12}{x^2 - 4}\\)", "category": "Building Skills", "options": ["x = 10", "x = 4", "x = -1", "No solution"], "answer": 0, "explanation": "The LCD is \\((x+2)(x-2)\\). Multiplying everything by the LCD yields: \\(3(x-2) - 1(x+2) = 12 \\implies 3x - 6 - x - 2 = 12 \\implies 2x - 8 = 12 \\implies 2x = 20 \\implies x = 10\\)."},
    {"q": "Rationalize the denominator and simplify: \\(\\frac{5 - \\sqrt{3}}{2 + \\sqrt{3}}\\)", "category": "Building Skills", "options": ["\\(13 - 7\\sqrt{3}\\)", "\\(7 - 3\\sqrt{3}\\)", "\\(10 - 2\\sqrt{3}\\)", "\\(13 + 7\\sqrt{3}\\)"], "answer": 0, "explanation": "Multiply numerator and denominator by \\(2 - \\sqrt{3}\\). Denominator becomes \\(4 - 3 = 1\\). Numerator becomes \\((5 - \\sqrt{3})(2 - \\sqrt{3}) = 10 - 5\\sqrt{3} - 2\\sqrt{3} + 3 = 13 - 7\\sqrt{3}\\)."},
    {"q": "Find the inverse function \\(f^{-1}(x)\\) for \\(f(x) = \\frac{4x - 1}{2x + 3}\\)", "category": "Building Skills", "options": ["\\(f^{-1}(x) = \\frac{2x + 3}{4x - 1}\\)", "\\(f^{-1}(x) = \\frac{3x + 1}{4 - 2x}\\)", "\\(f^{-1}(x) = \\frac{3x - 1}{4 + 2x}\\)", "\\(f^{-1}(x) = \\frac{4x + 1}{2x - 3}\\)"], "answer": 1, "explanation": "Let \\(y = \\frac{4x-1}{2x+3}\\). Swap: \\(x = \\frac{4y-1}{2y+3}\\). Multiply: \\(2xy + 3x = 4y - 1\\). Isolate y terms: \\(2xy - 4y = -3x - 1 \\implies y(2x - 4) = -3x - 1 \\implies y = \\frac{-3x - 1}{2x - 4} = \\frac{3x + 1}{4 - 2x}\\)."},

    # Applying the Concepts
    {"q": "A chemist needs 10 liters of a 30% acid solution. They only have 10% and 50% acid solutions in the lab. How many liters of the 50% solution should they mix with the 10% solution?", "category": "Applying the Concepts", "options": ["2.5 L", "4 L", "5 L", "7.5 L"], "answer": 2, "explanation": "Let \\(x\\) be the liters of 50% solution, so \\(10-x\\) is the 10% solution. Equation: \\(0.50x + 0.10(10-x) = 0.30(10)\\). \\(0.50x + 1 - 0.10x = 3 \\implies 0.40x = 2 \\implies x = 5\\)."},
    {"q": "A ball is thrown straight up. Its height \\(h\\) in feet after \\(t\\) seconds is given by \\(h(t) = -16t^2 + 64t + 80\\). How long will it take for the ball to hit the ground?", "category": "Applying the Concepts", "options": ["2 seconds", "4 seconds", "5 seconds", "8 seconds"], "answer": 2, "explanation": "Set \\(h(t) = 0\\). \\(-16t^2 + 64t + 80 = 0\\). Divide by -16: \\(t^2 - 4t - 5 = 0\\). Factor: \\((t-5)(t+1) = 0\\). Since \\(t > 0\\), \\(t = 5\\) seconds."},
    {"q": "A rectangle is inscribed in a semicircle of radius 10. If the length of the rectangle on the diameter is \\(2x\\), express the area of the rectangle as a function of \\(x\\).", "category": "Applying the Concepts", "options": ["\\(A(x) = x\\sqrt{100 - x^2}\\)", "\\(A(x) = 2x\\sqrt{100 - x^2}\\)", "\\(A(x) = 2x(100 - x^2)\\)", "\\(A(x) = x(100 - x^2)\\)"], "answer": 1, "explanation": "The coordinates of the top right corner of the rectangle on the circle are \\((x, y)\\). The equation of the circle is \\(x^2 + y^2 = 100\\), so \\(y = \\sqrt{100 - x^2}\\). The base of the rectangle is \\(2x\\) and height is \\(y\\). Area \\(A = 2xy = 2x\\sqrt{100 - x^2}\\)."},

    # Beyond the Basics
    {"q": "Solve the inequality: \\(\\frac{x^2 - x - 6}{x^2 + 4x + 4} \\ge 0\\)", "category": "Beyond the Basics", "options": ["\\((-\\infty, -2) \\cup (-2, 3]\\)", "\\((-\\infty, -2) \\cup [3, \\infty)\\)", "\\([-2, 3]\\)", "\\([3, \\infty)\\)"], "answer": 1, "explanation": "Factor the numerator and denominator: \\(\\frac{(x-3)(x+2)}{(x+2)^2} \\ge 0\\). This simplifies to \\(\\frac{x-3}{x+2} \\ge 0\\) where \\(x \\neq -2\\). The boundary points are \\(x = 3\\) (numerator) and \\(x = -2\\) (denominator). Testing regions gives positive on \\((-\\infty, -2)\\) and \\([3, \\infty)\\)."},
    {"q": "Find all real solutions to the equation: \\(x^{2/3} - 5x^{1/3} + 6 = 0\\)", "category": "Beyond the Basics", "options": ["\\(x = 2, 3\\)", "\\(x = 4, 9\\)", "\\(x = 8, 27\\)", "\\(x = \\sqrt{2}, \\sqrt{3}\\)"], "answer": 2, "explanation": "This is quadratic in form. Let \\(u = x^{1/3}\\). The equation is \\(u^2 - 5u + 6 = 0\\), which factors to \\((u-2)(u-3)=0\\). Thus \\(u=2\\) or \\(u=3\\). Since \\(u = x^{1/3}\\), cubing both sides gives \\(x = 2^3 = 8\\) and \\(x = 3^3 = 27\\)."},
    {"q": "Determine the end behavior and maximum number of turning points for \\(f(x) = -3x^5 + 4x^3 - x + 1\\).", "category": "Beyond the Basics", "options": ["As \\(x \\to \\infty, y \\to \\infty\\); As \\(x \\to -\\infty, y \\to -\\infty\\); 5 turning points", "As \\(x \\to \\infty, y \\to -\\infty\\); As \\(x \\to -\\infty, y \\to \\infty\\); 4 turning points", "As \\(x \\to \\pm\\infty, y \\to -\\infty\\); 4 turning points", "As \\(x \\to \\infty, y \\to -\\infty\\); As \\(x \\to -\\infty, y \\to \\infty\\); 5 turning points"], "answer": 1, "explanation": "The leading term is \\(-3x^5\\) (odd degree, negative coefficient). This means it rises to the left and falls to the right (\\(y \\to \\infty\\) as \\(x \\to -\\infty\\) and \\(y \\to -\\infty\\) as \\(x \\to \\infty\\)). A polynomial of degree \\(n\\) has at most \\(n-1\\) turning points, so \\(5-1 = 4\\)."},

    # Critical Thinking / Discussion / Writing
    {"q": "Consider the function \\(f(x) = \\sqrt{1 - x^2}\\). Without graphing, logically deduce why this function is NOT one-to-one, and therefore does not have a global inverse.", "category": "Critical Thinking / Discussion / Writing", "options": ["Because its domain is restricted to \\([-1, 1]\\).", "Because it contains a square root, and square roots inherently have two answers.", "Because \\(f(x)\\) is an even function, meaning \\(f(-x) = f(x)\\), so two different inputs yield the same output.", "Because the range only contains positive numbers."], "answer": 2, "explanation": "A function is one-to-one if \\(f(a) = f(b) \\implies a = b\\). Since \\(f(x) = \\sqrt{1-x^2}\\) is an even function, \\(f(0.5) = f(-0.5) = \\sqrt{0.75}\\). Since two different x-values produce the same y-value, it fails the horizontal line test and is not one-to-one."},
    {"q": "A student solves \\(\\sqrt{x+6} = x\\) by squaring both sides to get \\(x+6 = x^2\\), leading to roots \\(x = 3\\) and \\(x = -2\\). They declare both as solutions. Why is this logically flawed?", "category": "Critical Thinking / Discussion / Writing", "options": ["Squaring both sides is an invalid mathematical operation.", "The student factored the quadratic equation incorrectly.", "Squaring both sides creates a new equation where the principal square root is forced to equal a negative number, introducing extraneous solutions.", "The domain of the original equation does not include positive numbers."], "answer": 2, "explanation": "Squaring is a non-reversible operation if signs aren't restricted. Plugging \\(x=-2\\) back into the original gives \\(\\sqrt{4} = -2\\), which is false because the radical symbol denotes the *principal* (positive) root."},
    {"q": "Explain algebraically why the composition of two odd functions is always an odd function.", "category": "Critical Thinking / Discussion / Writing", "options": ["If \\(f\\) and \\(g\\) are odd, \\(f(g(-x)) = f(-g(x)) = -f(g(x))\\).", "If \\(f\\) and \\(g\\) are odd, \\(f(g(-x)) = -f(-g(x)) = f(g(x))\\).", "Odd functions have odd powers, and multiplying odd powers creates odd powers.", "It is not always an odd function; it depends on the coefficients."], "answer": 0, "explanation": "Let \\(f\\) and \\(g\\) be odd, meaning \\(g(-x) = -g(x)\\) and \\(f(-x) = -f(x)\\). Then the composition evaluated at \\(-x\\) is \\((f \\circ g)(-x) = f(g(-x)) = f(-g(x)) = -f(g(x)) = -(f \\circ g)(x)\\). This perfectly defines an odd function."}
]

html_template = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precalculus Mastery Quiz (Categorized)</title>
    <!-- MathJax for rendering math equations beautifully -->
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    
    <style>
        :root {
            --primary-color: #0f172a;
            --accent-color: #3b82f6;
            --success-color: #22c55e;
            --danger-color: #ef4444;
            --bg-color: #f1f5f9;
            --card-bg: #ffffff;
            --text-color: #1e293b;
            --border-color: #cbd5e1;
        }

        body {
            font-family: 'Inter', system-ui, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 900px;
            padding: 2rem;
            box-sizing: border-box;
        }

        h1 {
            text-align: center;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
            font-size: 2.5rem;
        }

        .subtitle {
            text-align: center;
            color: #64748b;
            margin-bottom: 2rem;
        }

        .score-board {
            position: sticky;
            top: 1rem;
            background: var(--primary-color);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            z-index: 100;
            margin-bottom: 2rem;
        }

        .score-board h3 { margin: 0; font-size: 1.2rem; }
        
        .category-header {
            background-color: #e2e8f0;
            color: var(--primary-color);
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            font-size: 1.4rem;
            font-weight: bold;
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            border-left: 5px solid var(--accent-color);
        }

        .question-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 1.5rem 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
        }

        .question-text {
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .options-list {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .option-btn {
            background: transparent;
            border: 2px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 1rem;
            text-align: left;
            font-size: 1rem;
            color: var(--text-color);
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .option-btn:hover:not(:disabled) {
            border-color: var(--accent-color);
            background: #eff6ff;
        }

        .option-btn:disabled {
            cursor: not-allowed;
            opacity: 0.8;
        }

        .option-btn.correct {
            background-color: #dcfce7;
            border-color: var(--success-color);
            color: #166534;
        }

        .option-btn.wrong {
            background-color: #fee2e2;
            border-color: var(--danger-color);
            color: #991b1b;
        }

        .explanation {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 0.5rem;
            background: #f8fafc;
            border-left: 4px solid var(--accent-color);
            display: none;
            font-size: 0.95rem;
        }

        .explanation.show {
            display: block;
            animation: fadeIn 0.4s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .actions {
            display: flex;
            justify-content: center;
            margin-top: 3rem;
            margin-bottom: 5rem;
        }

        .btn {
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1.1rem;
            font-weight: bold;
            border-radius: 0.5rem;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            transition: background 0.2s;
        }

        .btn:hover {
            background: #2563eb;
        }
        
        /* Summary Modal */
        #summary-modal {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: white;
            padding: 3rem;
            border-radius: 1rem;
            text-align: center;
            max-width: 400px;
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
        }
        .modal-content h2 { color: var(--primary-color); font-size: 2rem; margin-top:0; }
        .modal-content .final-score { font-size: 4rem; font-weight: bold; color: var(--accent-color); margin: 1rem 0; }
    </style>
</head>
<body>

    <div class="container">
        <h1>Precalculus Mastery Quiz</h1>
        <p class="subtitle">High-Difficulty Questions by Textbook Exercise Categories</p>

        <div class="score-board">
            <h3>Score: <span id="current-score">0</span> / 15</h3>
            <h3>Attempted: <span id="attempted-count">0</span></h3>
        </div>

        <div id="quiz-container"></div>

        <div class="actions">
            <button class="btn" onclick="finishQuiz()">Finish Quiz</button>
            <button class="btn" style="margin-left:1rem; background-color:var(--primary-color)" onclick="restartQuiz()">Restart Quiz</button>
        </div>
    </div>

    <div id="summary-modal">
        <div class="modal-content">
            <h2>Quiz Complete!</h2>
            <p>Your Final Score:</p>
            <div class="final-score" id="final-score-display">0%</div>
            <p id="score-message"></p>
            <button class="btn" style="margin-top:2rem;" onclick="restartQuiz()">Take Again</button>
        </div>
    </div>

    <script>
        const questionsData = REPLACE_ME_WITH_JSON;
        
        let score = 0;
        let attempted = 0;
        let answeredQuestions = new Set();

        const quizContainer = document.getElementById('quiz-container');
        const scoreElement = document.getElementById('current-score');
        const attemptedElement = document.getElementById('attempted-count');
        const summaryModal = document.getElementById('summary-modal');

        function initQuiz() {
            quizContainer.innerHTML = '';
            score = 0;
            attempted = 0;
            answeredQuestions.clear();
            updateScoreBoard();
            summaryModal.style.display = 'none';

            let currentCategory = "";

            questionsData.forEach((q, index) => {
                if (q.category !== currentCategory) {
                    currentCategory = q.category;
                    const catHeader = document.createElement('div');
                    catHeader.className = 'category-header';
                    catHeader.innerText = currentCategory;
                    quizContainer.appendChild(catHeader);
                }

                const card = document.createElement('div');
                card.className = 'question-card';
                card.id = `q-card-${index}`;

                let optionsHtml = '';
                q.options.forEach((opt, optIndex) => {
                    optionsHtml += `<button class="option-btn" id="q${index}-opt${optIndex}" onclick="checkAnswer(${index}, ${optIndex})">${opt}</button>`;
                });

                card.innerHTML = `
                    <div class="question-text">${index + 1}. ${q.q}</div>
                    <div class="options-list">
                        ${optionsHtml}
                    </div>
                    <div class="explanation" id="exp-${index}">
                        <strong>Explanation:</strong> ${q.explanation}
                    </div>
                `;
                quizContainer.appendChild(card);
            });
            
            // Re-render MathJax
            if(window.MathJax) {
                MathJax.typesetPromise();
            }
        }

        function checkAnswer(qIndex, selectedOptIndex) {
            if (answeredQuestions.has(qIndex)) return;

            const q = questionsData[qIndex];
            const isCorrect = (selectedOptIndex === q.answer);
            
            // Update buttons
            const selectedBtn = document.getElementById(`q${qIndex}-opt${selectedOptIndex}`);
            const correctBtn = document.getElementById(`q${qIndex}-opt${q.answer}`);

            if (isCorrect) {
                selectedBtn.classList.add('correct');
                score++;
            } else {
                selectedBtn.classList.add('wrong');
                correctBtn.classList.add('correct'); // Show correct answer
            }

            // Disable all options for this question
            q.options.forEach((_, idx) => {
                document.getElementById(`q${qIndex}-opt${idx}`).disabled = true;
            });

            // Show explanation
            document.getElementById(`exp-${qIndex}`).classList.add('show');

            answeredQuestions.add(qIndex);
            attempted++;
            updateScoreBoard();
        }

        function updateScoreBoard() {
            scoreElement.innerText = score;
            attemptedElement.innerText = attempted;
        }

        function finishQuiz() {
            const percentage = Math.round((score / questionsData.length) * 100);
            document.getElementById('final-score-display').innerText = percentage + '%';
            
            let message = '';
            if(percentage >= 90) message = "Outstanding! You possess Ultrathink mastery.";
            else if(percentage >= 70) message = "Great job! A very solid understanding of advanced concepts.";
            else if(percentage >= 50) message = "Good effort! Review the notes to solidify your fundamentals.";
            else message = "Keep practicing! Use the revision notes to brush up.";
            
            document.getElementById('score-message').innerText = message;
            summaryModal.style.display = 'flex';
        }

        function restartQuiz() {
            window.scrollTo(0,0);
            initQuiz();
        }

        // Initialize on load
        window.onload = initQuiz;
    </script>
</body>
</html>
"""

html_out = html_template.replace("REPLACE_ME_WITH_JSON", json.dumps(clean_questions))

with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/quiz.html", "w") as f:
    f.write(html_out)

print("quiz.html generated successfully!")
