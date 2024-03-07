from flask import Flask, render_template, redirect, request, url_for
 
app = Flask(__name__)
 
@app.route('/')
def main():
    return render_template('page1.html')
 
@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        # 여기에서 폼 데이터 처리 또는 필요한 작업 수행
        pass
    return render_template('page2.html')
@app.route('/page3', methods=['GET', 'POST'])
def page3():
    if request.method == 'POST':
        # 여기에서 폼 데이터 처리 또는 필요한 작업 수행
        pass
    return render_template('page3.html')
@app.route('/page4',methods=['GET','POST'])
def page4():
    if request.method=='POST':
        pass
    return render_template('page4.html')
@app.route('/page5',methods=['GET','POST'])
def page5():
    if request.method=='POST':
        pass
    return render_template('page5.html')
@app.route('/page6',methods=['GET','POST'])
def page6():
    if request.method=='POST':
        pass
    return render_template('page6.html')
if __name__ == "__main__":              
    app.run(debug=True)
