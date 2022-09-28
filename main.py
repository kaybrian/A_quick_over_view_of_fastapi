from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def index():
    return {"data":"blog list"}


@app.get('/blog/unpublished')
def unpublished():
    return {"data":"Unpublished Blogs"}


@app.get('/blog/{blog_id}')
def show(blog_id:int):
    # returns a blog of the same id
    return {
        "Blog":f"Blog ID number : {blog_id}"
    }


@app.get('/blog/{blog_id}/comments')
def comments(blog_id):
    # returns the blog comments 
    return {
        'data':{"comments":"there are no comments"}
    }
    
