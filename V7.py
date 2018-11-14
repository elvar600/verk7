import pymysql
from bottle import *

@get('/')
def index():
    return template('index')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    # Conn...
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user="kennitala", passwd='mypassword', db='2303012980_vef_demo')
    # curosr
    cur = conn.cursor()

    #
    #
    cur.execute("SELECT count(*) FROM 2303012980_vef_demo.users where user=%s",(u))
    # Fetch
    result = cur.fetchone()

    #notandi er ekki til
    if result[0] == 0:
        cur.execute("INSERT INFO 2303012980_vef_demo.users Values(%s,%s,%s)",(u, p, n))
        # commit
        conn.commit()
        cur.close()
        #lokum
        conn.close()
        return u, "hefur verið skráður <br><a href='/'>Heim</a>"
    else:
        return u, "er ekki frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nýskrá</a>"

@route('/doinnskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='kennitala', passwd='mypassword', db='2303012980_vef_demo')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 2303012980_vef_demo.users where user=%s and pass=%s",(u ,p))
    result = cur.fetchone()
    print(result)
    # er u og p til í db?
    if result[0] == 1:

        cur.close()
        conn.close()
        return template('leyni',u=u)
    else:
        return template('ekkileyni')

#

try:
    run(host="0.0.0.0", port=os.environ.get('POST'))
except:
    run(debug=True)
