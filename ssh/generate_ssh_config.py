#!/usr/bin/python
# -*- coding: utf-8 -*- 

from os import path

# Usage: python generate_ssh_config.py

def generate_ssh_config(label, user, ip_list, file="", port=22, 
                        env="prod", config_file="config", mode="a+"):
    with open(config_file, mode) as f:
        name = label
        if env != "":
            name = "{}-{}".format(env, label)
        if mode == "w+":
            f.write("# {} generate by {}\n".format(config_file, path.basename(__file__)))
            f.write("# cp {} ~/.ssh/config\n\n".format(config_file))
        f.write("###### {}\n".format(name))
        f.write("Host {}*\n".format(name))
        f.write("    User {}\n".format(user))
        f.write("    Port {}\n".format(port))
        if file != "":
            f.write("    IdentityFile {}\n".format(file))
        f.write("\n")
        index = 1
        for ip in ip_list:
            f.write("Host {}{}\n".format(name, index))
            f.write("    HostName {}\n".format(ip))
            index += 1
        f.writelines("\n")
        f.close()


def main():
    config_file = "config"  

    # mainnet
    #env="prod"
    identity_file_path = "~/.ssh/test.pem"
    bp_nodes = ["123.57.128.163", "123.57.219.234","39.105.91.74", "47.93.216.131", "39.106.34.255",
        "161.117.230.14", "161.117.224.200"]
    generate_ssh_config(label="bp", user="dev", ip_list=bp_nodes, file=identity_file_path, mode="w+")

    fn_nodes = ["60.205.201.27", "47.94.81.85"]
    generate_ssh_config(label="fn", user="dev", ip_list=fn_nodes, file=identity_file_path)

    faucet_nodes = ["47.93.58.236", "101.201.57.51", "161.117.183.170", "161.117.229.144"]
    generate_ssh_config(label="faucet", user="dev", ip_list=faucet_nodes, file=identity_file_path)

    db_nodes = ["182.92.164.121"]
    generate_ssh_config(label="db", user="dev", ip_list=db_nodes, file=identity_file_path)

    monitor_nodes = ["123.57.19.148"] # testnet + prod 
    generate_ssh_config(label="monitor", user="dev", ip_list=monitor_nodes, file=identity_file_path)

    # testnet
    env = "test"
    #identity_file_path = "~/.ssh/test.pem"
    bp_nodes = ["123.56.104.245", "182.92.163.55", "101.200.217.70", "101.200.218.234", "47.93.52.224"]
    generate_ssh_config(label="bp", user="root", ip_list=bp_nodes, file=identity_file_path, env=env)

    fn_nodes = ["123.57.16.132", "123.56.98.47"]
    generate_ssh_config(label="fn", user="root", ip_list=fn_nodes, file=identity_file_path, env=env)

    faucet_nodes = ["123.57.16.132", "123.56.98.47"]
    generate_ssh_config(label="faucet", user="root", ip_list=faucet_nodes, file=identity_file_path, env=env)

    db_nodes = ["182.92.163.55"] # mysql + mongo
    generate_ssh_config(label="db", user="root", ip_list=db_nodes, file=identity_file_path, env=env)


if __name__ == "__main__":
    main()

