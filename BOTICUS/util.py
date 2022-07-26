from BOTICUS import app
@app.template_filter('dict_but')
def dict_but(d, **kwargs):
    return { **d, **kwargs }