# -*- coding:utf-8 -*-

import base64

def auth_encode(user, password, mode='Basic'):
    print('user: {}, pwd: {}, mode: {}'.format(user, password, mode))
    encode_str = '{}:{}'.format(user, password)
    encode_str = encode_str.encode('utf-8')
    encode_result = base64.b64encode(encode_str)
    #return mode + ' ' + encode_result
    return '{} {}'.format(mode, encode_result)

def auth_decode(auth):
    auth_mode, auth_base64 = auth.split(' ', 1)
    print('auth_mode: {}, auth_base64: {}'.format(auth_mode, auth_base64))
    auth_username, auth_password = auth_base64.decode('base64').split(':', 1)
    print('auth_username: {}, auth_password: {}'.format(auth_username, auth_password))

def base_auth_valid(auth, base_auth_user, base_auth_passwd, mode='Basic'):
    auth_mode, auth_base64 = auth.split(' ', 1)
    #print('auth_mode: {}, auth_base64: {}'.format(auth_mode, auth_base64))
    if auth_mode != mode:
        return False
    auth_username, auth_password = auth_base64.decode('base64').split(':', 1)
    #print('auth_username: {}, auth_password: {}'.format(auth_username, auth_password))
    if auth_username == base_auth_user and auth_password == base_auth_passwd:
        return True
    else:
        return False

def test(user, pwd):
    auth = auth_encode(user, pwd)
    auth_decode(auth)
    print('base_auth_valid: {}\n'.format(base_auth_valid(auth, user, pwd)))

test('root', '123456')
test('root12345678', 'abcdefgh')


