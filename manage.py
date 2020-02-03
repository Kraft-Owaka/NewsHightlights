from app import create_app
from flask_script import Manager,Server

#app instance
app = create_app('production')

manager=Manager(app)

manager.add_command('server', Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TestTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    manager.run()