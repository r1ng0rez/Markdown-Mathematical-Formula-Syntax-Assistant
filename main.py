from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# 定义公式字典
formulas = {
    "上下标": [
        ("下标", "a_0, a_{pre}"),
        ("上标", "a^0, a^{[0]}"),
    ],
    "括号与取整": [
        ("基本括号", "( ), [ ], \\langle \\rangle"),
        ("竖线和双竖线", "\\lvert \\rvert, \\lVert \\rVert"),
        ("花括号", "\\lbrace \\rbrace 或 \\{ \\}"),
        ("取整符号", "\\lfloor \\rfloor, \\lceil \\rceil"),
        ("增大括号", "\\big( \\Big( \\bigg( \\Bigg("),
        ("嵌套括号示例", "\\Bigg[\\bigg[\\Big[\\big[[x]\\big]\\Big]\\bigg]\\Bigg]"),
    ],
    "分数与开方": [
        ("分数", "\\frac{a}{b}"),
        ("连分数", "x = a_0 + \\frac{1}{a_1 + \\frac{1}{a_2 + \\frac{1}{a_3}}}"),
        ("平方根", "\\sqrt{x}"),
        ("n次方根", "\\sqrt[n]{x}"),
    ],
    "累加累乘与积分": [
        ("累加", "\\sum_{i=1}^n i^2"),
        ("累乘", "\\prod_{i=1}^n x_i"),
        ("积分", "\\int_a^b f(x)dx"),
        ("多重积分", "\\iint, \\iiint, \\oint"),
    ],
    "三角函数": [
        ("基本函数", "\\sin, \\cos, \\tan, \\cot"),
        ("其他函数", "\\sec, \\csc"),
        ("角度表示", "30^\\circ"),
    ],
    "对数函数": [
        ("自然对数", "\\ln(x)"),
        ("对数", "\\log_{a}(b)"),
        ("常用对数", "\\lg(x)"),
    ],
    "二元运算符": [
        ("算术运算", "\\pm, \\mp, \\times, \\div"),
        ("点运算", "\\cdot, \\bullet, \\circ"),
        ("圆圈运算", "\\odot, \\otimes, \\oplus"),
        ("其他运算", "\\star, \\ast, \\dagger"),
    ],
    "关系符号": [
        ("比较", "=, \\neq, <, >, \\leq, \\geq"),
        ("约等于", "\\approx, \\simeq, \\cong"),
        ("其他关系", "\\sim, \\propto, \\parallel, \\perp"),
    ],
    "极限与微积分": [
        ("极限", "\\lim_{x \\to \\infty} f(x)"),
        ("导数", "f'(x), f''(x)"),
        ("偏导", "\\frac{\\partial f}{\\partial x}"),
        ("梯度", "\\nabla f"),
    ],
    "向量与箭头": [
        ("向量", "\\vec{a}"),
        ("箭头", "\\rightarrow, \\leftarrow, \\Rightarrow, \\Leftarrow"),
        ("长箭头", "\\longrightarrow, \\Longrightarrow"),
        ("其他箭头", "\\mapsto, \\hookrightarrow"),
    ],
    "集合运算": [
        ("基本符号", "\\in, \\notin, \\subset, \\subseteq"),
        ("集合运算", "\\cup, \\cap, \\bigcup, \\bigcap"),
        ("空集", "\\emptyset"),
    ],
    "逻辑运算": [
        ("基本逻辑", "\\land, \\lor, \\neg"),
        ("量词", "\\forall, \\exists"),
        ("推导", "\\because, \\therefore"),
    ],
    "修饰符号": [
        ("上划线", "\\overline{a+b}"),
        ("下划线", "\\underline{a+b}"),
        ("箭头标记", "\\overrightarrow{AB}"),
        ("帽子符号", "\\hat{a}, \\widehat{abc}"),
    ],
    "希腊字母": [
        ("小写", "\\alpha, \\beta, \\gamma, \\delta"),
        ("大写", "\\Alpha, \\Beta, \\Gamma, \\Delta"),
        ("常用字母", "\\pi, \\theta, \\sigma, \\omega"),
    ],
    "矩阵": [
        ("基本矩阵", "\\begin{matrix} a & b \\\\ c & d \\end{matrix}"),
        ("括号矩阵", "\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}"),
        ("行列式", "\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}"),
        ("带省略号矩阵",
         "\\begin{bmatrix} a & \\cdots & b \\\\ \\vdots & \\ddots & \\vdots \\\\ c & \\cdots & d \\end{bmatrix}"),
    ],
    "分段函数": [
        ("基本分段", "f(x) = \\begin{cases} x & x \\geq 0 \\\\ -x & x < 0 \\end{cases}"),
        ("多条件分段", "\\operatorname{sgn}(x) = \\begin{cases} -1 & x < 0 \\\\ 0 & x = 0 \\\\ 1 & x > 0 \\end{cases}"),
    ],
    "其他符号": [
        ("省略号", "\\dots, \\cdots, \\vdots, \\ddots"),
        ("空格", "\\, \\; \\quad \\qquad"),
        ("特殊符号", "\\aleph, \\hbar, \\infty, \\nabla"),
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