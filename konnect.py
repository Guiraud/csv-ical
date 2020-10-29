# -*- coding: utf-8 -*-
import keyring
import configparser
config = configparser.ConfigParser()




def define_local_passwords():
    """
    Description : définition des mots de passe locaux
    """
    config.read('/etc/config.python')
    for section in config.sections():
	    for clé,valeur in config.items(section):
		    keyring.set_password(section,clé,valeur.strip('\"'))
    
    logins = {}
    logins['pass'] = keyring.get_password("name",
                                          "pass")
    #print(logins['db_tableau_pass_localhost'] + " / "+logins['db_tableau_user_localhost'] + "@ " + logins['local_host'])
    return logins
