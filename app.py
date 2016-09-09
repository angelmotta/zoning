from flask import Flask, render_template, request, redirect, url_for, flash  
import genzone
from forms import wwnForm, wwnFormPure
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    return redirect(url_for('zonepower'))

@app.route('/zonepower', methods=['GET', 'POST'])
def zonepower():
    form = wwnForm()
    if form.validate_on_submit():
        wwn1, wwn2, wwn3, wwn4 = genzone.wwnparse(form.wwn.data)
        vios = form.vios.data
        hostserver = form.host.data
        lpar_alias1, lpar_alias2, lpar_alias3, lpar_alias4 = genzone.lpar_alias(hostserver, vios)
        zone1, vsp_port1, fabric1 = genzone.zonename1(lpar_alias1)
        zone2, vsp_port2, fabric2 = genzone.zonename2(lpar_alias2)
        zone3, vsp_port3 = genzone.zonename3(lpar_alias3)
        zone4, vsp_port4 = genzone.zonename4(lpar_alias4)
        return render_template('result.html', wwn1=wwn1, zone1=zone1, lpar_alias1=lpar_alias1, vsp_port1=vsp_port1, fabric1=fabric1, 
                               wwn2=wwn2, zone2=zone2, lpar_alias2=lpar_alias2, vsp_port2=vsp_port2, fabric2=fabric2,  
                               wwn3=wwn3, zone3=zone3, lpar_alias3=lpar_alias3, vsp_port3=vsp_port3,  
                               wwn4=wwn4, zone4=zone4, lpar_alias4=lpar_alias4, vsp_port4=vsp_port4)
    return render_template('index.html', form=form)

@app.route('/zonepure', methods=['GET', 'POST'])
def zonepure():
    form = wwnFormPure()
    if form.validate_on_submit():
        wwn1, wwn2 = genzone.wwnparsepure(form.wwn.data)
        vios = form.vios.data
        hostserver = form.host.data
        lpar_alias1, lpar_alias2 = genzone.alias_pure(hostserver, vios)
        zone1, vsp_port1, fabric1 = genzone.zonepure1(lpar_alias1)
        zone2, vsp_port2, fabric2 = genzone.zonepure2(lpar_alias2)
        return render_template('resultpure.html', wwn1=wwn1, zone1=zone1, lpar_alias1=lpar_alias1, vsp_port1=vsp_port1, fabric1=fabric1, 
                               wwn2=wwn2, zone2=zone2, lpar_alias2=lpar_alias2, vsp_port2=vsp_port2, fabric2=fabric2)
    return render_template('pure.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
