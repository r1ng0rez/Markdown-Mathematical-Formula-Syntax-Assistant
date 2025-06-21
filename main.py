from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# 更全面的公式字典
formulas = {
    "数学符号": [
        ("加减乘除", "+ - \\times \\div"),
        ("分数", "\\frac{a}{b}"),
        ("平方根", "\\sqrt{x}"),
        ("n次方根", "\\sqrt[n]{x}"),
        ("幂和指数", "x^2, e^{x}"),
        ("极限", "\\lim_{x \\to \\infty} f(x)"),
        ("求和", "\\sum_{i=1}^n i^2"),
        ("积分", "\\int_a^b f(x)dx"),
        ("偏微分", "\\frac{\\partial f}{\\partial x}"),
    ],
    "希腊字母": [
        ("Alpha", "\\Alpha, \\alpha"),
        ("Beta", "\\Beta, \\beta"),
        ("Gamma", "\\Gamma, \\gamma"),
        ("Delta", "\\Delta, \\delta"),
        ("Epsilon", "\\Epsilon, \\epsilon"),
        ("Theta", "\\Theta, \\theta"),
        ("Pi", "\\Pi, \\pi"),
        ("Sigma", "\\Sigma, \\sigma"),
        ("Omega", "\\Omega, \\omega"),
    ],
    "矩阵与行列式": [
        ("矩阵", "\\begin{matrix} a & b \\\\ c & d \\end{matrix}"),
        ("带括号矩阵", "\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}"),
        ("行列式", "\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}"),
        ("方程组", "\\begin{cases} x + y = 1 \\\\ x - y = 0 \\end{cases}"),
    ],
    "常用公式": [
        ("二次方程求根", "x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}"),
        ("欧拉公式", "e^{i\\pi} + 1 = 0"),
        ("二项式定理", "(a + b)^n = \\sum_{k=0}^n C_n^k a^{n-k}b^k"),
        ("泰勒展开", "f(x) = \\sum_{n=0}^\\infty \\frac{f^{(n)}(a)}{n!}(x-a)^n"),
    ],
    "关系符号": [
        ("等于不等于", "= \\neq"),
        ("约等于", "\\approx"),
        ("大于小于", "> < \\geq \\leq"),
        ("属于", "\\in \\notin"),
    ]
}


@app.route('/')
def index():
    return render_template('index.html',
                           formulas=formulas,
                           updated=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []

    for category, items in formulas.items():
        for name, formula in items:
            if query in name.lower() or query in formula.lower():
                results.append({
                    'category': category,
                    'name': name,
                    'formula': formula
                })

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)