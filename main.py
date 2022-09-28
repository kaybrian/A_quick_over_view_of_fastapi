from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get('/blog')
def index(limit=10,published : bool = True, sort: Optional[str]=None):
    # only get ten published blogs
    if published:
        return {"data":f"blog list has only {limit} published blogs"}
    else:
        return {"data":"A few blogs sent out "}


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
    

