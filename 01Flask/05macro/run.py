from app import app
#将str 改成全局变量
app.add_template_global(str,'str')
app.run(debug=True)
