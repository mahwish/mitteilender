import sys
import os
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from sqlalchemy import engine_from_config
from pyck.ext import AdminController, add_admin_handler
from pyck.lib import get_models
import mitteilender

from models import DBSession

import importlib
from apps import enabled_apps


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    load_project_settings()

    session_factory = UnencryptedCookieSessionFactoryConfig(settings.get('session.secret', 'hello'))

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(session_factory=session_factory, settings=settings)
    config.add_tween('mitteilender.auth.authenticator')
    config.include('pyramid_handlers')
    config.add_view('pyramid.view.append_slash_notfound_view',
                context='pyramid.httpexceptions.HTTPNotFound')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('try', '{pname}/try')
    config.add_route('home', '/')
    config.add_route('contact', '/contact')
    config.add_route('add_project', '/add_project')
    
    config.add_route('item', '/item')
    config.add_route('dbshow', '/dbshow')
    config.add_route('mahi', '/mahi')
    config.add_route('p_list', '/p_list')
    config.add_route('json_project_list', 'json/project_list')
    config.add_route('json_project_details', 'json/project_details/{pname}')
    config.add_route('del_item', '{item_id}/del_item')
    config.add_route('show_image', '{item_id}/show_image')
    config.add_route('show_dbitem', '{item_id}/show_dbitem')
    config.add_route('edit_item', '{item_id}/edit_item')
    config.add_route('upload_image', '{pname}/upload_image')
    config.add_route('text_item', '{pname}/text_item')
    config.add_route('contact_item', '{pname}/contact_item')
    config.add_route('view_items', '{pname}/view_items')
    config.add_route('section_item', '{pname}/section_item')
    config.add_route('upload_f', '{pname}/upload_f')
    config.add_route('email', '{pname}/email')
    config.add_route('edit_dbitem', '{item_id}/{dbitem_id}/{rec_id}/edit_dbitem')
    config.add_route('del_rec', '{item_id}/{rec_id}/del_rec')
    config.add_route('del_dbitem', '{item_id}/del_dbitem')
    config.add_route('primary_display', '{item_id}/primary_display')
    config.add_route('swap_display_order', '{p_id}/swap_display_order')
    config.add_route('swap', '{item_id}/{direction}/swap')
    
    config.add_route('upload_csv', '{pname}/upload_csv')
    config.add_route('add', '{pname}/add')
    config.add_route('field_type', '{item_id}/field_type')
    config.add_route('show_f', '{pname}/show_f')
    config.add_route('more_items', '/more_items')
    config.add_route('field_save', '/field_save')
    config.add_route('image', 'json/image')
    config.add_route('new_input', '{item_id}/new_input')
    config.add_route('input_manage', '{item_id}/{input_id}/input_manage')
    config.add_route('show_input', '{p_id}/show_input')

    config.add_route('pyckauth_login', '/login')
    config.add_route('pyckauth_logout', '/logout')
    config.add_route('pyckauth_manager', '/auth')
    config.add_route('pyckauth_users', '/auth/users')
    config.add_route('pyckauth_permissions', '/auth/permissions')
    config.add_route('pyckauth_routes', '/auth/routes')
    
    
    add_admin_handler(config, DBSession, get_models(mitteilender), 'admin', '/admin', AdminController)
    configure_app_routes(config)
    configure_app_routes(config)

    config.scan()

    return config.make_wsgi_app()


def load_project_settings():
    here = os.path.dirname(__file__)
    sys.path.insert(0, here + '/apps')
    sys.path.insert(0, here)


def configure_app_routes(config):
    """
    Puggable - Application routes integration
    =========================================

    Integrates routes for all applications present in the apps folder and enabled (present in the enabled_apps
    list in apps.__init__.py).

    Normally each application is automatically given a route_prefix matching the
    application name. So for example, if you have an application named blog, its route_prefix would be /blog
    and all other application routes will also be prefixed with /blog. If you want to override the route_prefix
    and want the application accessible under some other route prefix (or no route prefix at all), use the
    app_route_prefixes dictionary present in this function to specify an alternate route for the application.
    Specify just / if you want the application routes to be accessible at the same level as the main project's
    routes.
    """

    # The app_route_prefixes dictionary for overriding app route prefixes
    app_route_prefixes = {
        #'blog': '/myblog'
    }

    for app_name in enabled_apps:
        app_route_prefix = app_route_prefixes.get(app_name, '/%s' % app_name)
        app_module = importlib.import_module(".apps.%s" % app_name, "mitteilender")

        try:
            config.include(app_module.application_routes, route_prefix=app_route_prefix)
        except Exception, e:
            print(repr(e))
