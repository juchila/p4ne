import json
import pprint
import requests
import flask

# c cisco получаем данные в виде json, print выводит строку, поэтому json.dumps делает строку из json
# template обрабатывает json, поэтому список данных трансформируем через jsonify в json
#
app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template("topology.html")


@app.route('/api/topology')
def topology():
    return flask.jsonify(responce.json()['response'])


def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)
    return response.json()['response']['serviceTicket']


if __name__ == '__main__':
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/host?limit=5&offset=1"
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    responce = requests.get(url, headers=header, verify=False)
    print("Hosts = ")
    pprint.pprint(json.dumps(responce.json()))

    url = "https://" + controller + "/api/v1/network-device?limit=5&offset=1"
    print("Devices = ")
    #pprint.pprint(json.dumps(responce.json()))
    responce = requests.get(url, headers=header, verify=False)
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    responce = requests.get(url, headers=header, verify=False)
    print("Topology = ")
    #pprint.pprint(json.dumps(responce.json()))
    print("Topology = ")
    print(json.dumps(responce.json()))
    app.run(debug=True)


