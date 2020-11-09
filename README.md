# inouk_ufw_status_json
A python script that generate a json output of 'ufw status'

# License

MIT

# Requirements

* Python 3
* ufw must be installed 
* You must use a Python interpreter in which ufw is installed (eg. default python)

# Usage

    sudo python3 inouk_ufw_status_json.py

    brouette-cyril:~$ sudo python3 inouk_ufw_status_json.py 
    {
        "ufw_get_status_json_version": "0.1",
        "ufw_version": "0.36",
        "ufw_active": false,
        "rules": [
            {
                "remove": false,
                "updated": false,
                "v6": false,
                "dst": "0.0.0.0/0",
                "src": "8.99.999.41",
                "dport": "any",
                "sport": "any",
                "protocol": "any",
                "multi": false,
                "dapp": "",
                "sapp": "",
                "action": "allow",
                "position": 0,
                "logtype": "",
                "interface_in": "",
                "interface_out": "",
                "direction": "in",
                "forward": false,
                "comment": "",
                "number": 1,
                "command": "allow from 8.99.999.41"
            },
            {
                "remove": false,
                "updated": false,
                "v6": false,
                "dst": "0.0.0.0/0",
                "src": "8.8.8.8",
                "dport": "any",
                "sport": "any",
                "protocol": "any",
                "multi": false,
                "dapp": "",
                "sapp": "",
                "action": "allow",
                "position": 0,
                "logtype": "",
                "interface_in": "",
                "interface_out": "",
                "direction": "in",
                "forward": false,
                "comment": "",
                "number": 2,
                "command": "allow from 8.8.8.8"
            }
        ],
        "warnings": [
            "uid is 0 but '/home/ternian/inouk_ufw_status_json/inouk_ufw_status_json.py' is owned by 1001",
            "/home/ternian/inouk_ufw_status_json/inouk_ufw_status_json.py is group writable!",
            "uid is 0 but '/home/ternian/inouk_ufw_status_json' is owned by 1001",
            "/home/ternian/inouk_ufw_status_json is group writable!",
            "uid is 0 but '/home/ternian' is owned by 1001"
        ]
    }


