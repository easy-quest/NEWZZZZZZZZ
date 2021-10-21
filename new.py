# examples/things.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon


# Falcon следует архитектурному стилю REST, что означает (среди прочего) то,
# что вы думаете с точки зрения ресурсов и переходов между
# состояниями, которые отображаются на глаголы HTTP.
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # Это состояние по умолчанию
        resp.content_type = falcon.MEDIA_TEXT  # По умолчанию JSON, поэтому переопределить
        resp.text = ('\nБольше всего меня трепещут две вещи: звездное небо'
                     'надо мной и моральный закон внутри меня.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')


# Экземпляры falcon.App - это вызываемые приложения WSGI,
# в более крупных приложениях приложение создается в отдельном файле.
app = falcon.App()

# Ресурсы представлены долгоживущими экземплярами классов
things = ThingsResource()

# Things будет обрабатывать все запросы к URL path '/things'
app.add_route('/things', things)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
