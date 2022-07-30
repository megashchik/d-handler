from setuptools import setup


setup(
    name='d-handler',
    version='0.0.1',
    description='simple util to create and control processes',
    long_description='simple util to create and control processes',
    packages=[
        'd_handler', 'd_handler.process_tools'
    ],
    # packages=['daemon_handler', 'daemon_handler.process_tools', 'daemon_handler.main', 'daemon_handler.process_tools.'],
    entry_points={'console_scripts':[
        'd-handler=d_handler.main:main'
    ]},
    url='https://github.com/megashchik/daemon-handler',
    author='Ivan Chizhikov',
    author_email='megashchik@gmail.com',
    license='Apache 2 License'
)