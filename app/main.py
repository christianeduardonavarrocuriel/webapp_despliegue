import web

urls = (
    '/', 'Index'
)

render = web.template.render("templates/")

app = web.application(urls, globals())

class Index:
    def GET(self):
        data = {
            "message": "El primer despliegue"
            }
        return render.index(data)

application = app.wsgifunc()

if __name__ == "__main__":
    app.run()