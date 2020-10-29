# -*- coding: utf-8 -*-
import keyring


def define_local_passwords():
    """
    Description : définition des mots de passe locaux
    """

    logins = {}
    logins['pass'] = keyring.get_password("name",
                                          "pass")
    #print(logins['db_tableau_pass_localhost'] + " / "+logins['db_tableau_user_localhost'] + "@ " + logins['local_host'])
    return logins
