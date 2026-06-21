import os

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precalculus Revision Notes - Chapters P, 1, 2</title>
    <!-- MathJax for rendering math equations beautifully -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    
    <style>
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --bg-color: #f8fafc;
            --text-color: #1e293b;
            --sidebar-bg: #ffffff;
            --border-color: #e2e8f0;
            --accent-bg: #eff6ff;
            --card-bg: #ffffff;
        }

        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            line-height: 1.6;
        }

        /* Sidebar Navigation */
        .sidebar {
            width: 280px;
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--border-color);
            height: 100vh;
            position: fixed;
            overflow-y: auto;
            padding: 2rem 1rem;
            box-sizing: border-box;
        }

        .sidebar h2 {
            font-size: 1.25rem;
            margin-bottom: 1.5rem;
            color: var(--primary-color);
        }

        .sidebar ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .sidebar li {
            margin-bottom: 0.5rem;
        }

        .sidebar a {
            text-decoration: none;
            color: var(--text-color);
            display: block;
            padding: 0.5rem;
            border-radius: 0.375rem;
            transition: all 0.2s;
            font-size: 0.95rem;
        }

        .sidebar a:hover {
            background-color: var(--accent-bg);
            color: var(--primary-color);
        }

        .sidebar .chapter-title {
            font-weight: bold;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            font-size: 0.8rem;
            color: #64748b;
            letter-spacing: 0.05em;
        }

        /* Main Content */
        .main-content {
            margin-left: 280px;
            padding: 3rem 4rem;
            max-width: 900px;
            width: 100%;
            box-sizing: border-box;
        }

        h1 {
            font-size: 2.5rem;
            color: var(--primary-color);
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }

        h2.section-title {
            font-size: 2rem;
            color: var(--secondary-color);
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
        }

        h3 {
            font-size: 1.5rem;
            color: var(--text-color);
            margin-top: 2rem;
        }

        .concept-card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .concept-card h4 {
            margin-top: 0;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .formula-box {
            background-color: var(--accent-bg);
            border-left: 4px solid var(--primary-color);
            padding: 1rem 1.5rem;
            margin: 1rem 0;
            border-radius: 0 0.5rem 0.5rem 0;
            font-size: 1.1rem;
            overflow-x: auto;
        }

        .example-box {
            background-color: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 0.5rem;
            padding: 1rem 1.5rem;
            margin: 1rem 0;
        }

        .example-title {
            font-weight: bold;
            color: #166534;
            margin-bottom: 0.5rem;
        }

        .qa-box {
            background-color: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 0.5rem;
            padding: 1rem 1.5rem;
            margin: 1rem 0;
        }

        .qa-title {
            font-weight: bold;
            color: #b45309;
            margin-bottom: 0.5rem;
        }

        .first-principles {
            font-style: italic;
            color: #475569;
            background: #f8fafc;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }

        /* Diagrams */
        .diagram-container {
            text-align: center;
            margin: 2rem 0;
            padding: 1rem;
            background: white;
            border-radius: 0.5rem;
            border: 1px solid var(--border-color);
        }

        .coordinate-plane {
            position: relative;
            width: 300px;
            height: 300px;
            margin: 0 auto;
            border: 1px solid #cbd5e1;
            background-image: 
                linear-gradient(#f1f5f9 1px, transparent 1px),
                linear-gradient(90deg, #f1f5f9 1px, transparent 1px);
            background-size: 30px 30px;
        }
        
        .axis-x { position: absolute; top: 150px; left: 0; width: 100%; height: 2px; background: black; }
        .axis-y { position: absolute; left: 150px; top: 0; height: 100%; width: 2px; background: black; }
        .point { position: absolute; width: 8px; height: 8px; background: red; border-radius: 50%; transform: translate(-50%, -50%); }

        @media (max-width: 768px) {
            .sidebar { display: none; }
            .main-content { margin-left: 0; padding: 1.5rem; }
        }
    </style>
</head>
<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <h2>📚 Precalculus Notes</h2>
        <ul>
            <li class="chapter-title">Chapter P: Basic Algebra</li>
            <li><a href="#p1">P.1 Real Numbers</a></li>
            <li><a href="#p2">P.2 Exponents & Notation</a></li>
            <li><a href="#p3">P.3 Polynomials</a></li>
            <li><a href="#p4">P.4 Factoring</a></li>
            <li><a href="#p5">P.5 Rational Expressions</a></li>
            <li><a href="#p6">P.6 Radicals & Exponents</a></li>

            <li class="chapter-title">Chapter 1: Equations & Inequalities</li>
            <li><a href="#1-1">1.1 Linear Equations</a></li>
            <li><a href="#1-2">1.2 Applications/Modeling</a></li>
            <li><a href="#1-3">1.3 Quadratic Equations</a></li>
            <li><a href="#1-4">1.4 Complex Numbers</a></li>
            <li><a href="#1-5">1.5 Other Equations</a></li>
            <li><a href="#1-6">1.6 Inequalities</a></li>
            <li><a href="#1-7">1.7 Absolute Value</a></li>

            <li class="chapter-title">Chapter 2: Graphs & Functions</li>
            <li><a href="#2-1">2.1 Coordinate Plane</a></li>
            <li><a href="#2-2">2.2 Graphs of Equations</a></li>
            <li><a href="#2-3">2.3 Lines</a></li>
            <li><a href="#2-4">2.4 Functions</a></li>
            <li><a href="#2-5">2.5 Properties of Functions</a></li>
            <li><a href="#2-6">2.6 Library of Functions</a></li>
            <li><a href="#2-7">2.7 Transformations</a></li>
            <li><a href="#2-8">2.8 Composite Functions</a></li>
            <li><a href="#2-9">2.9 Inverse Functions</a></li>
        </ul>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <h1>Precalculus Comprehensive Revision Notes</h1>
        <p>A complete, self-contained guide for Chapters P, 1, and 2. Use the sidebar to navigate to specific topics.</p>

        <!-- CHAPTER P -->
        <h2 class="section-title" id="chapter-p">Chapter P: Basic Concepts of Algebra</h2>

        <div class="concept-card" id="p1">
            <h4>P.1 The Real Numbers and Their Properties</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Numbers evolved from simple counting (1, 2, 3) to include nothingness (0), debts/opposites (negatives), fractions (rationals), and finally numbers that cannot be written as simple fractions like \(\pi\) (irrationals). All these together form the real number line.
            </div>
            <p><strong>Summary:</strong> The real number system \(\mathbb{R}\) includes Natural numbers (\(\mathbb{N}\)), Whole numbers (\(\mathbb{W}\)), Integers (\(\mathbb{Z}\)), Rational numbers (\(\mathbb{Q}\)), and Irrational numbers (\(\mathbb{I}\)). Properties like Commutative, Associative, and Distributive govern operations on these numbers.</p>
            
            <div class="formula-box">
                Distributive Property: \( a(b + c) = ab + ac \) <br>
                Absolute Value: \( |x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases} \)<br>
                Distance between \(a\) and \(b\): \( d(a,b) = |b - a| \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Distance</div>
                Find the distance between \(-5\) and \(3\) on the real number line.<br>
                \( d = |3 - (-5)| = |3 + 5| = |8| = 8 \)
            </div>

            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Is \(\sqrt{2}\) a rational or irrational number? Why?<br>
                <strong>A:</strong> It is irrational. It cannot be expressed as a ratio of two integers \(p/q\), and its decimal expansion neither terminates nor repeats.
            </div>
        </div>

        <div class="concept-card" id="p2">
            <h4>P.2 Integer Exponents and Scientific Notation</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Multiplication is repeated addition. Exponents are simply repeated multiplication! \(x^n\) just means multiplying \(x\) by itself \(n\) times.
            </div>
            <p><strong>Summary:</strong> Rules of exponents allow us to simplify complex expressions quickly. Scientific notation uses powers of 10 to express very large or very small numbers compactly.</p>
            
            <div class="formula-box">
                Product Rule: \( a^m \cdot a^n = a^{m+n} \) <br>
                Quotient Rule: \( \frac{a^m}{a^n} = a^{m-n} \) <br>
                Power Rule: \( (a^m)^n = a^{mn} \) <br>
                Negative Exponent: \( a^{-n} = \frac{1}{a^n} \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Simplifying Exponents</div>
                Simplify \( (2x^3y^{-2})^3 \)<br>
                \( = 2^3 \cdot (x^3)^3 \cdot (y^{-2})^3 = 8x^9y^{-6} = \frac{8x^9}{y^6} \)
            </div>

            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Write \( 0.00045 \) in scientific notation.<br>
                <strong>A:</strong> Move the decimal 4 places to the right: \( 4.5 \times 10^{-4} \).
            </div>
        </div>

        <div class="concept-card" id="p3">
            <h4>P.3 Polynomials</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> A polynomial is an expression built from variables and constants using only addition, subtraction, and multiplication (and non-negative integer exponents). Think of them as building blocks of algebraic expressions.
            </div>
            <p><strong>Summary:</strong> Polynomials are classified by their degree (highest exponent). Operations include addition (combine like terms), subtraction, and multiplication (FOIL method for binomials).</p>
            
            <div class="formula-box">
                Difference of Squares: \( (a - b)(a + b) = a^2 - b^2 \) <br>
                Perfect Square Trinomial: \( (a \pm b)^2 = a^2 \pm 2ab + b^2 \) <br>
                Difference of Cubes: \( a^3 - b^3 = (a - b)(a^2 + ab + b^2) \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: FOIL Method</div>
                Multiply \( (2x + 3)(x - 4) \)<br>
                First: \( 2x \cdot x = 2x^2 \) <br>
                Outer: \( 2x \cdot (-4) = -8x \) <br>
                Inner: \( 3 \cdot x = 3x \) <br>
                Last: \( 3 \cdot (-4) = -12 \) <br>
                Combine: \( 2x^2 - 5x - 12 \)
            </div>

            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What is the degree of the polynomial \( 4x^3 - 5x^5 + 2x - 7 \)?<br>
                <strong>A:</strong> The degree is 5, as it is the highest exponent of the variable \(x\).
            </div>
        </div>

        <div class="concept-card" id="p4">
            <h4>P.4 Factoring Polynomials</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Factoring is the reverse of multiplication. If multiplication is taking pieces and combining them into a block, factoring is breaking the block back into its fundamental pieces.
            </div>
            <p><strong>Summary:</strong> Techniques include finding the Greatest Common Factor (GCF), grouping, factoring trinomials (\(ax^2+bx+c\)), and recognizing special forms (like difference of squares).</p>
            
            <div class="example-box">
                <div class="example-title">Example: Factoring a Trinomial</div>
                Factor \( x^2 - 5x + 6 \)<br>
                We need two numbers that multiply to \(6\) and add to \(-5\). These are \(-2\) and \(-3\).<br>
                Result: \( (x - 2)(x - 3) \)
            </div>

            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Factor \( 4x^2 - 9 \).<br>
                <strong>A:</strong> This is a difference of squares: \( (2x)^2 - (3)^2 = (2x - 3)(2x + 3) \).
            </div>
        </div>

        <div class="concept-card" id="p5">
            <h4>P.5 Rational Expressions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> A rational expression is just a fraction where the numerator and/or the denominator are polynomials. All the rules of regular fractions apply here!
            </div>
            <p><strong>Summary:</strong> Operations on rational expressions require finding common denominators for addition/subtraction. For multiplication, multiply across. Always simplify by factoring and canceling common factors.</p>

            <div class="formula-box">
                Division: \( \frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C} \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Simplifying</div>
                Simplify \( \frac{x^2 - 1}{x^2 + x} \)<br>
                Factor numerator: \( (x - 1)(x + 1) \)<br>
                Factor denominator: \( x(x + 1) \)<br>
                Cancel \( (x + 1) \): Result is \( \frac{x - 1}{x} \), where \( x \neq -1, 0 \).
            </div>

            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What must you do before adding \( \frac{1}{x} + \frac{2}{x-1} \)?<br>
                <strong>A:</strong> Find a common denominator, which is \( x(x-1) \).
            </div>
        </div>

        <div class="concept-card" id="p6">
            <h4>P.6 Rational Exponents and Radicals</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Fractional exponents are just another way to write roots. A denominator in an exponent signifies a root, while the numerator signifies a power.
            </div>
            <p><strong>Summary:</strong> Converting between radical notation and exponent notation makes evaluating expressions easier. Rationalizing the denominator removes radicals from the bottom of a fraction.</p>
            
            <div class="formula-box">
                Rational Exponent: \( a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m \)<br>
                Product Rule for Radicals: \( \sqrt[n]{ab} = \sqrt[n]{a}\sqrt[n]{b} \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Rationalizing Denominator</div>
                Rationalize \( \frac{2}{\sqrt{3}} \)<br>
                Multiply top and bottom by \( \sqrt{3} \): \( \frac{2\sqrt{3}}{\sqrt{3}\sqrt{3}} = \frac{2\sqrt{3}}{3} \)
            </div>

            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Evaluate \( 8^{2/3} \).<br>
                <strong>A:</strong> Take the cube root first: \(\sqrt[3]{8} = 2\). Then square it: \( 2^2 = 4 \).
            </div>
        </div>

        <!-- CHAPTER 1 -->
        <h2 class="section-title" id="chapter-1">Chapter 1: Equations and Inequalities</h2>

        <div class="concept-card" id="1-1">
            <h4>1.1 Linear Equations in One Variable</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> An equation is like a balanced scale. Whatever you do to one side, you must do to the other to keep it balanced. Our goal is to isolate the unknown variable.
            </div>
            <p><strong>Summary:</strong> A linear equation can be written in the form \(ax + b = 0\). Solutions can be a single value (conditional), all real numbers (identity), or no solution (inconsistent).</p>

            <div class="example-box">
                <div class="example-title">Example: Solving a Linear Equation</div>
                Solve \( 3(x - 2) = 15 \)<br>
                Distribute: \( 3x - 6 = 15 \)<br>
                Add 6: \( 3x = 21 \)<br>
                Divide by 3: \( x = 7 \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What is an identity equation?<br>
                <strong>A:</strong> An equation that is true for all values of the variable, e.g., \( 2x + 2 = 2(x + 1) \).
            </div>
        </div>

        <div class="concept-card" id="1-2">
            <h4>1.2 Applications of Linear Equations: Modeling</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Math is a language. Modeling is the process of translating real-world word problems from English into Math, solving them, and translating back.
            </div>
            <p><strong>Summary:</strong> Common models include Geometry, Finance (Simple Interest), Uniform Motion (Distance = Rate x Time), Work Rate, and Mixture problems.</p>
            
            <div class="formula-box">
                Simple Interest: \( I = P \cdot r \cdot t \) <br>
                Uniform Motion: \( d = r \cdot t \) <br>
                Work Rate: \( \frac{1}{t_1} + \frac{1}{t_2} = \frac{1}{t_{total}} \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Uniform Motion</div>
                A car travels 120 miles in 2 hours. Find its rate.<br>
                \( 120 = r \cdot 2 \implies r = 60 \) mph.
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> If Alice paints a room in 3 hours, what is her work rate per hour?<br>
                <strong>A:</strong> \( \frac{1}{3} \) of the room per hour.
            </div>
        </div>

        <div class="concept-card" id="1-3">
            <h4>1.3 Quadratic Equations</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> A quadratic equation (\(ax^2+bx+c=0\)) represents a parabola. Finding the solution (roots) means finding where the parabola crosses the x-axis.
            </div>
            <p><strong>Summary:</strong> Methods to solve include Factoring, Square Root Method, Completing the Square, and the Quadratic Formula. The discriminant tells us the number and type of solutions.</p>
            
            <div class="formula-box">
                Quadratic Formula: \( x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \) <br>
                Discriminant: \( \Delta = b^2 - 4ac \)
                <ul>
                    <li>\( \Delta > 0 \): 2 real solutions</li>
                    <li>\( \Delta = 0 \): 1 real solution</li>
                    <li>\( \Delta < 0 \): 0 real (2 complex) solutions</li>
                </ul>
            </div>

            <div class="example-box">
                <div class="example-title">Example: Quadratic Formula</div>
                Solve \( x^2 - 3x + 2 = 0 \)<br>
                \( x = \frac{3 \pm \sqrt{(-3)^2 - 4(1)(2)}}{2} = \frac{3 \pm \sqrt{1}}{2} \)<br>
                \( x = 2 \) or \( x = 1 \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> How many real solutions does \( x^2 + 1 = 0 \) have?<br>
                <strong>A:</strong> Zero, because the discriminant is \( 0^2 - 4(1)(1) = -4 < 0 \).
            </div>
        </div>

        <div class="concept-card" id="1-4">
            <h4>1.4 Complex Numbers</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> What happens if we try to take the square root of a negative number? We invent a new number, \(i\), where \(i^2 = -1\). This expands our number system to 2D!
            </div>
            <p><strong>Summary:</strong> A complex number has the form \( a + bi \). Operations include addition, subtraction, multiplication (using FOIL and \(i^2=-1\)), and division (using the complex conjugate).</p>

            <div class="formula-box">
                Imaginary Unit: \( i = \sqrt{-1} \implies i^2 = -1 \) <br>
                Complex Conjugate of \( a + bi \) is \( a - bi \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Multiplication</div>
                Multiply \( (2 + 3i)(1 - 2i) \)<br>
                \( 2 - 4i + 3i - 6i^2 = 2 - i - 6(-1) = 2 - i + 6 = 8 - i \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Divide \( \frac{1}{i} \).<br>
                <strong>A:</strong> Multiply top and bottom by \( -i \): \( \frac{-i}{-i^2} = \frac{-i}{1} = -i \).
            </div>
        </div>

        <div class="concept-card" id="1-5">
            <h4>1.5 Solving Other Types of Equations</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> We can solve complex equations by disguising them as simpler equations we already know how to solve! For example, by substituting \( u = x^2 \).
            </div>
            <p><strong>Summary:</strong> Includes Radical equations (isolate radical, raise to power), Rational equations (multiply by LCD), and Equations Quadratic in Form.</p>

            <div class="example-box">
                <div class="example-title">Example: Radical Equation</div>
                Solve \( \sqrt{x - 1} = 3 \)<br>
                Square both sides: \( x - 1 = 9 \implies x = 10 \).<br>
                Check: \( \sqrt{10-1} = \sqrt{9} = 3 \). Valid!
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What is an extraneous solution?<br>
                <strong>A:</strong> A solution that emerges from the process of solving (like squaring both sides) but doesn't make the original equation true. Always check your answers!
            </div>
        </div>

        <div class="concept-card" id="1-6">
            <h4>1.6 Inequalities</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Inequalities represent a range of solutions rather than a single point. If an equation is "where the target is exactly", an inequality is "anywhere past the line".
            </div>
            <p><strong>Summary:</strong> When solving linear inequalities, if you multiply or divide by a negative number, you MUST flip the inequality sign. Test points are used for non-linear inequalities.</p>

            <div class="formula-box">
                Interval Notation: <br>
                \( a < x \le b \implies (a, b] \) <br>
                \( x \ge a \implies [a, \infty) \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Solving Inequality</div>
                Solve \( -2x + 4 < 10 \)<br>
                Subtract 4: \( -2x < 6 \)<br>
                Divide by -2 (FLIP SIGN!): \( x > -3 \)<br>
                Interval: \( (-3, \infty) \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Why do we flip the sign when dividing by a negative?<br>
                <strong>A:</strong> Because negatives reverse order. Since \( 2 < 5 \), multiplying by -1 reflects them across zero, making \( -2 > -5 \).
            </div>
        </div>

        <div class="concept-card" id="1-7">
            <h4>1.7 Absolute Value Equations and Inequalities</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Absolute value means "distance from zero". \( |x| < 3 \) means "all numbers whose distance from 0 is less than 3".
            </div>
            <p><strong>Summary:</strong> To solve \(|X| = a\), set \(X=a\) and \(X=-a\). To solve \(|X| < a\), set \(-a < X < a\). To solve \(|X| > a\), set \(X < -a\) OR \(X > a\).</p>

            <div class="example-box">
                <div class="example-title">Example: Absolute Value Inequality</div>
                Solve \( |2x - 1| \le 5 \)<br>
                Rewrite: \( -5 \le 2x - 1 \le 5 \)<br>
                Add 1: \( -4 \le 2x \le 6 \)<br>
                Divide 2: \( -2 \le x \le 3 \)<br>
                Interval: \( [-2, 3] \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Solve \( |x| = -5 \).<br>
                <strong>A:</strong> No solution. Distance cannot be negative.
            </div>
        </div>

        <!-- CHAPTER 2 -->
        <h2 class="section-title" id="chapter-2">Chapter 2: Graphs and Functions</h2>

        <div class="concept-card" id="2-1">
            <h4>2.1 The Coordinate Plane</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Rene Descartes merged Algebra and Geometry by placing a grid over space. Now, equations (algebra) can be drawn as pictures (geometry), and shapes can be analyzed using numbers.
            </div>
            <p><strong>Summary:</strong> The Cartesian plane has an x-axis and y-axis. Key formulas define the geometry of points on this plane.</p>

            <div class="diagram-container">
                <div class="coordinate-plane">
                    <div class="axis-x"></div>
                    <div class="axis-y"></div>
                    <div class="point" style="left: 210px; top: 90px;"></div>
                    <span style="position: absolute; left: 220px; top: 70px;">(2, 2)</span>
                </div>
                <p><em>The Cartesian Coordinate System</em></p>
            </div>

            <div class="formula-box">
                Distance Formula: \( d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \) <br>
                Midpoint Formula: \( M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right) \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Midpoint</div>
                Find midpoint of \((0, 0)\) and \((4, 6)\).<br>
                \( M = \left(\frac{0+4}{2}, \frac{0+6}{2}\right) = (2, 3) \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> Which quadrant contains the point \((-3, 4)\)?<br>
                <strong>A:</strong> Quadrant II (x is negative, y is positive).
            </div>
        </div>

        <div class="concept-card" id="2-2">
            <h4>2.2 Graphs of Equations</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> A graph is simply the visual collection of ALL points \((x,y)\) that make an equation true.
            </div>
            <p><strong>Summary:</strong> We analyze graphs by finding intercepts (where they cross axes) and symmetry (reflection across axes or origin). Circles have a specific standard equation.</p>

            <div class="formula-box">
                x-intercept: Set \(y=0\), solve for \(x\)<br>
                y-intercept: Set \(x=0\), solve for \(y\)<br>
                Equation of a Circle: \( (x - h)^2 + (y - k)^2 = r^2 \) where center is \((h,k)\)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Circle</div>
                Find center and radius of \( (x - 2)^2 + (y + 3)^2 = 16 \)<br>
                Center: \( (2, -3) \), Radius: \( \sqrt{16} = 4 \).
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What kind of symmetry does \(y = x^2\) have?<br>
                <strong>A:</strong> y-axis symmetry, because replacing \(x\) with \(-x\) doesn't change the equation.
            </div>
        </div>

        <div class="concept-card" id="2-3">
            <h4>2.3 Lines</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> A line represents a constant rate of change. The slope tells us exactly how much \(y\) changes for every unit change in \(x\).
            </div>
            <p><strong>Summary:</strong> Lines can be represented in various forms. Parallel lines have equal slopes; perpendicular lines have negative reciprocal slopes.</p>

            <div class="formula-box">
                Slope (\(m\)): \( m = \frac{y_2 - y_1}{x_2 - x_1} \) <br>
                Slope-Intercept: \( y = mx + b \) <br>
                Point-Slope: \( y - y_1 = m(x - x_1) \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Equation of a Line</div>
                Find equation of line through \((1, 2)\) with slope \(3\).<br>
                \( y - 2 = 3(x - 1) \implies y - 2 = 3x - 3 \implies y = 3x - 1 \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What is the slope of a horizontal line? A vertical line?<br>
                <strong>A:</strong> Horizontal: \(m=0\). Vertical: \(m\) is undefined.
            </div>
        </div>

        <div class="concept-card" id="2-4">
            <h4>2.4 Functions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Think of a function as a machine. You drop an input (\(x\)) into the machine, it does some work on it, and spits out exactly ONE output (\(y\)).
            </div>
            <p><strong>Summary:</strong> A relation is a function if each input has exactly one output (Vertical Line Test). Domain = allowed inputs (x), Range = possible outputs (y). We use function notation \(f(x)\).</p>

            <div class="example-box">
                <div class="example-title">Example: Domain</div>
                Find the domain of \( f(x) = \frac{1}{x - 2} \)<br>
                Denominator cannot be zero. \( x - 2 \neq 0 \implies x \neq 2 \).<br>
                Domain: \( (-\infty, 2) \cup (2, \infty) \)
            </div>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> If \(f(x) = x^2 + 1\), what is \(f(-3)\)?<br>
                <strong>A:</strong> \( (-3)^2 + 1 = 9 + 1 = 10 \).
            </div>
        </div>

        <div class="concept-card" id="2-5">
            <h4>2.5 Properties of Functions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> We can analyze the "behavior" of the function machine by looking at its graph. Is it going up (increasing)? Going down (decreasing)?
            </div>
            <p><strong>Summary:</strong> Functions can be increasing, decreasing, or constant over intervals. Relative maximums/minimums are the peaks and valleys. Even functions have y-axis symmetry, Odd functions have origin symmetry.</p>

            <div class="formula-box">
                Average Rate of Change: \( \frac{f(x_2) - f(x_1)}{x_2 - x_1} \) (This is just slope!)<br>
                Even: \( f(-x) = f(x) \)<br>
                Odd: \( f(-x) = -f(x) \)
            </div>

            <div class="example-box">
                <div class="example-title">Example: Even or Odd?</div>
                Is \( f(x) = x^3 \) even, odd, or neither?<br>
                \( f(-x) = (-x)^3 = -x^3 = -f(x) \). Therefore, it is Odd.
            </div>
        </div>

        <div class="concept-card" id="2-6">
            <h4>2.6 A Library of Functions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Just like letters form the alphabet, there is a fundamental alphabet of basic function shapes. Knowing these "parent graphs" allows us to build complex ones.
            </div>
            <p><strong>Summary:</strong> Key functions to memorize: Constant (\(y=c\)), Linear (\(y=x\)), Quadratic (\(y=x^2\)), Cubic (\(y=x^3\)), Square Root (\(y=\sqrt{x}\)), Absolute Value (\(y=|x|\)).</p>
            
            <div class="qa-box">
                <div class="qa-title">Q&A Checkpoint</div>
                <strong>Q:</strong> What is a piecewise function?<br>
                <strong>A:</strong> A function defined by different equations over different parts of its domain.
            </div>
        </div>

        <div class="concept-card" id="2-7">
            <h4>2.7 Transformations of Functions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> Instead of graphing complex functions from scratch, we take a basic "parent graph" and shift, stretch, or flip it.
            </div>
            <p><strong>Summary:</strong> Transformations alter the parent graph \(y=f(x)\):<br>
            - \( f(x) + c \) (Shift UP)<br>
            - \( f(x - c) \) (Shift RIGHT)<br>
            - \( -f(x) \) (Reflect over x-axis)<br>
            - \( af(x) \) (Vertical stretch if \(a>1\))</p>

            <div class="example-box">
                <div class="example-title">Example: Describing Transformation</div>
                Describe the graph of \( y = (x - 3)^2 + 2 \) relative to \(y=x^2\).<br>
                It is the standard parabola shifted RIGHT 3 units and UP 2 units.
            </div>
        </div>

        <div class="concept-card" id="2-8">
            <h4>2.8 Combining Functions; Composite Functions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> We can chain function machines together! The output of the first machine becomes the input of the second machine.
            </div>
            <p><strong>Summary:</strong> We can add, subtract, multiply, and divide functions. Composition \( (f \circ g)(x) \) means \( f(g(x)) \).</p>

            <div class="example-box">
                <div class="example-title">Example: Composition</div>
                If \( f(x) = 2x \) and \( g(x) = x + 1 \). Find \( (f \circ g)(x) \).<br>
                \( f(g(x)) = f(x + 1) = 2(x + 1) = 2x + 2 \)
            </div>
        </div>

        <div class="concept-card" id="2-9">
            <h4>2.9 Inverse Functions</h4>
            <div class="first-principles">
                <strong>First Principles:</strong> An inverse function is a machine that runs backward. It undoes whatever the original function did, turning outputs back into the original inputs.
            </div>
            <p><strong>Summary:</strong> A function has an inverse only if it is one-to-one (passes Horizontal Line Test). Denoted \(f^{-1}(x)\). The domain of \(f\) becomes the range of \(f^{-1}\).</p>

            <div class="formula-box">
                Property of Inverses: \( f(f^{-1}(x)) = x \) and \( f^{-1}(f(x)) = x \)<br>
                To find inverse algebraically: Swap \(x\) and \(y\), then solve for \(y\).
            </div>

            <div class="example-box">
                <div class="example-title">Example: Finding Inverse</div>
                Find inverse of \( f(x) = 2x + 3 \).<br>
                1. \( y = 2x + 3 \)<br>
                2. Swap: \( x = 2y + 3 \)<br>
                3. Solve for y: \( 2y = x - 3 \implies y = \frac{x - 3}{2} \)<br>
                \( f^{-1}(x) = \frac{x - 3}{2} \)
            </div>
        </div>

        <br><br><br><br>
    </div>

</body>
</html>"""

with open("/Users/ntnmathur/Desktop/aarav_precalc/revision_notes.html", "w") as f:
    f.write(html_content)

print("revision_notes.html generated successfully!")
