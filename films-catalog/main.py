from fastapi import FastAPI, Request

app = FastAPI(
    title='Films Catalog'
)


@app.get('/')
def read_docs(request: Request):
    docs_url = request.url.replace(
        path='/docs',
    )

    return {
        'docs': str(docs_url)
    }