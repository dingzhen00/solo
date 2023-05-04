import os
from django.conf import settings
from django.test import Client
from django.test.runner import DiscoverRunner
from django.urls import reverse
from django.apps import apps
import behave_webdriver
from selenium import webdriver


def before_all(context):
    # 设置环境变量
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    use_fixture(django_setup, context)

    # 加载 Django 应用程序
    django.setup()
    context.runner = DiscoverRunner()
    context.runner.setup_test_environment()
    context.old_db_config = context.runner.setup_databases()

    # 加载 Django 应用程序
    apps.populate(settings.INSTALLED_APPS)
    django.setup()

    # 设置 Behave Webdriver
    context.behave_driver = behave_webdriver.Chrome()

    # 创建 Django 测试客户端
    context.client = Client()

    # 其他设置代码
    # ...


def after_all(context):
    # 关闭 Behave Webdriver
    context.behave_driver.close()

    # 销毁测试数据库
    context.runner.teardown_databases(context.old_db_config)

    # 销毁测试环境
    context.runner.teardown_test_environment()


def django_setup(context):
    behave_webdriver.register(context.behave_driver)
    context.behave_driver.set_window_size(1280, 720)


def before_feature(context, feature):
    # 加载 fixtures 数据
    context.fixtures = []
    if 'fixtures' in feature.tags:
        for tag in feature.tags:
            if tag.startswith('fixtures-'):
                fixture_name = tag[len('fixtures-'):]
                context.fixtures.append(fixture_name)
        if context.fixtures:
            call_command('loaddata', *context.fixtures, verbosity=0)


def after_feature(context, feature):
    # 卸载 fixtures 数据
    if 'fixtures' in feature.tags and context.fixtures:
        call_command('flush', verbosity=0, interactive=False)


def before_scenario(context, scenario):
    # 设置 Webdriver
    if 'selenium' in scenario.tags:
        context.behave_driver.switch_to_window(0)


def after_scenario(context, scenario):
    # 清空 Django Session
    context.client.session.flush()

    # 删除 Webdriver cookies
    if 'selenium' in scenario.tags:
        context.behave_driver.delete_all_cookies()


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_tag(context, tag):
    pass


def before_tag(context, tag):
    pass

