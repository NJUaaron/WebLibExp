from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
import json


with open('data/DetectFile.json', 'r') as openfile:
    file_list = json.load(openfile)


# @view_config(route_name='lib_test', renderer='test_page.pt')
# def lib_testing(request):
#     index = int(request.matchdict['lib_index'])
#     lib_info = lib_list['results'][index]
#     lib_name = lib_info['name']
#     lib_path = lib_info['latest']
#     return dict(lib_name=lib_name, lib_path=lib_path)

@view_config(route_name='lib_test', renderer='test_page.pt')
def lib_testing(request):
    index = str(request.matchdict['file_index'])
    print(index)
    file_info = file_list[index]
    return dict(libname = file_info['libname'], 
                filename = file_info['filename'],
                url = file_info['url'],
                version = file_info['version'])




if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('lib_test', '/test/{file_index}')
        
        config.include('pyramid_chameleon')

        config.scan('app')
        config.add_static_view(name='static', path='static')
        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 6543, app)
    server.serve_forever()


# 127.0.0.1:6543/test/tween.js@18.6.4@tween.umd.min.js